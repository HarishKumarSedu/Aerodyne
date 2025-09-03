from dfttools import *
from time import sleep
import random
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback


def ocp_ls_trim():
  Test_Name = 'OCP_LS_TRIM'

  print(f'............ {Test_Name} ........')
  startup()
  global_enable()
  playback() 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0)  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_drv_force', 'length': 1, 'registers': [{'REG': '0x9B', 'POS': 4, 'RegisterName': 'CLD analog setting reg 5', 'RegisterLength': 8, 'Name': 'cld_drv_force', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '0x81', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0xA)  # Turn on Cascode N, low side N mos trun on 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_sel_part_byp', 'length': 1, 'registers': [{'REG': '0x9A', 'POS': 5, 'RegisterName': 'CLD analog setting reg 4', 'RegisterLength': 8, 'Name': 'cld_sel_part_byp', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': 'NNNNNNNN', 'Default': '0x86', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x2) #only bit 2 need to be changed
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x4) # FSYN ana_ds_mid_up


  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_sel_part_m', 'length': 1, 'registers': [{'REG': '0x1B', 'POS': 4, 'RegisterName': 'Force registers 4', 'RegisterLength': 8, 'Name': 'cld_sel_part_m', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_sel_part_force', 'length': 1, 'registers': [{'REG': '0x1A', 'POS': 4, 'RegisterName': 'Force registers 3', 'RegisterLength': 8, 'Name': 'cld_sel_part_force', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_ds_dvr_ocp_ref_ls_trim', 'length': 4, 'registers': [{'REG': '0xB6', 'POS': 0, 'RegisterName': 'OTP FIELDS 6', 'RegisterLength': 8, 'Name': 'otp_ds_dvr_ocp_ref_ls_trim[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x88', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0xF) #lower threshold to 750mV


  # Wait for device stabilization
  sleep(0.1)  # 100 µs
  i_force = 3/4
  bit_width = 4 # width of the field 
  th = 1.8/2
  # @ATE, "GND" in the following instruction is "PGND"
  trigger = VTRIG_LH(signal="IODATA0", reference="GND", threshold=1.8,expected_value=0) # digital signal trigger level is 1.8 
  AFORCE(signal="OUTP", reference="GND", value=i_force, error_spread=0.01)  # 500mA ±5%
  sleep(0.00005) #50us

  if trigger:
      print("Errore: all’avvio il comparatore è già alto")
  else:
    # sweep code from 0xF to 0x8, then 0x0 to 0x7
      for code in list(list(range(2**bit_width -1,2**bit_width//2 -1,-1))+list(range(0,2**bit_width//2,1))) : 

          # 3. breve attesa per stabilizzare il circuito
          sleep(0.1)  # 50 µs
          I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_ds_dvr_ocp_ref_ls_trim', 'length': 4, 'registers': [{'REG': '0xB6', 'POS': 0, 'RegisterName': 'OTP FIELDS 6', 'RegisterLength': 8, 'Name': 'otp_ds_dvr_ocp_ref_ls_trim[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x88', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=code)
          # 4. leggiamo di nuovo l’uscita del comparatore
          trigger = VTRIG_LH(signal="IODATA0", reference="GND", threshold=1.8,expected_value=1.8) # digital signal trigger level is 1.8 

          # 5. se abbiamo superato la soglia, abbiamo finito
          if trigger:
              print(f"trim code = {hex(code)} ")
              break

  AFORCE(signal="OUTP", reference="GND", value=float('inf'), error_spread=0.05)  # stop forcing
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_drv_force', 'length': 1, 'registers': [{'REG': '0x9B', 'POS': 4, 'RegisterName': 'CLD analog setting reg 5', 'RegisterLength': 8, 'Name': 'cld_drv_force', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '0x81', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0)  

if __name__ == '__main__':
  ocp_ls_trim()