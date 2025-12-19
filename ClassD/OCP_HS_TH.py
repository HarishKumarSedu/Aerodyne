from dfttools import *
from time import sleep
import random

from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback


def ocp_hs_th():
  Test_Name = 'OCP_HS_TH'

  print(f'............ {Test_Name} ........')
  startup()
  global_enable()
  playback() 

  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'spk_gain', 'length': 3, 'registers': [{'REG': '0x92', 'POS': 0, 'RegisterName': 'SPK setting reg 1', 'RegisterLength': 8, 'Name': 'spk_gain[2:0]', 'Mask': '0x7', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': '000NNNNN', 'Default': '0x03', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x5)  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x2) #only bit 2 need to be changed
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x5) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_data_dwa', 'length': 9, 'registers': [{'REG': '0x11', 'POS': 0, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_data_dwa[8]', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 8, 'FieldLSB': 8, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0x12', 'POS': 0, 'RegisterName': 'DAC test 2', 'RegisterLength': 8, 'Name': 'tst_data_dwa[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x100)  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_dac', 'length': 1, 'registers': [{'REG': '0x11', 'POS': 7, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_dac', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)  

  # Wait for device stabilization
  sleep(0.0001)  # 100 µs
  i_start = 0.05
  i_step = 0.05
  i_end = 0.85
  AFORCE(signal="OUTN", reference="GND", value=-i_start, error_spread=0.01)  # 500mA ±5%
  sleep(0.00005) #50us
  # mid_up = 0 #debug
  ocp_status=I2C_READ(device_address="0x38",field_info={'fieldname': 'cld_ocp_state', 'length': 1, 'registers': [{'REG': '0x05', 'POS': 1, 'RegisterName': 'Interrupt status register 2', 'RegisterLength': 8, 'Name': 'cld_ocp_state', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'IIIIIIII', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]},expected_value=0)

  if ocp_status :
      print("Errore: all’avvio il comparatore è già alto")
  else:
      for code in range(15):
          i_force = code*i_step + i_start
          AFORCE(signal="OUTP", reference="GND", value=-i_force , error_spread=0.05) 
          sleep(50e-6)  # 50 µs
          print(f"current = {i_force :.3f} ")
          ocp_status =I2C_READ(device_address="0x38",field_info={'fieldname': 'cld_ocp_state', 'length': 1, 'registers': [{'REG': '0x05', 'POS': 1, 'RegisterName': 'Interrupt status register 2', 'RegisterLength': 8, 'Name': 'cld_ocp_state', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'IIIIIIII', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]},expected_value=1)
        
          if ocp_status:
              print(f"Threshold = {i_force :.3f} ")
              break
          elif i_force > i_end :
              print(f"Threshold corssed {i_end : .3f}A ")
              break
            
          
  AFORCE(signal="OUTP", reference="PGND", value=float('inf'), error_spread=0.05)  # stop forcing
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0) #only bit 2 need to be changed
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_dac', 'length': 1, 'registers': [{'REG': '0x11', 'POS': 7, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_dac', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_data_dwa', 'length': 9, 'registers': [{'REG': '0x11', 'POS': 0, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_data_dwa[8]', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 8, 'FieldLSB': 8, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0x12', 'POS': 0, 'RegisterName': 'DAC test 2', 'RegisterLength': 8, 'Name': 'tst_data_dwa[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)  

if __name__ == '__main__':
  ocp_hs_th()