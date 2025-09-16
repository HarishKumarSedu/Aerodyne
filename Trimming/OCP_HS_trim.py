from dfttools import *
from time import sleep
import random

Test_Name = 'OCP_HS_TRIM'
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback


def ocp_hs_trim():
  Test_Name = 'OCP_HS_TRIM'

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

  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_ds_dvr_ocp_ref_hs_trim', 'length': 4, 'registers': [{'REG': '0xB6', 'POS': 4, 'RegisterName': 'OTP FIELDS 6', 'RegisterLength': 8, 'Name': 'otp_ds_dvr_ocp_ref_hs_trim[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x88', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0xF) #lower threshold to 750mV


  # Wait for device stabilization
  sleep(0.1)  # 100 µs
  i_force = - 3/4
  max_step = 15
  th = 1.8/2
  bit_width=4
  # @ATE "GND" = > "PGND"
  AFORCE(signal="OUTN", reference="GND", value=i_force, error_spread=0.01)  # 500mA ±5%
  trigger = VTRIG_LH(signal="IODATA0", reference="GND", threshold=1.8,expected_value=0) # digital signal trigger level is 1.8 
  sleep(0.5)

  if trigger:
      print("Errore: all’avvio il comparatore è già alto")
  else:
    # Code --> 0xF to 0x8 , 0x00 t0 0x7
      for code in list(list(range(2**bit_width -1 ,2**bit_width//2 -1,-1))+list(range(0,2**bit_width//2,1))):

          # 3. breve attesa per stabilizzare il circuito
          sleep(50e-6)  # 50 µs
          I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_ds_dvr_ocp_ref_hs_trim', 'length': 4, 'registers': [{'REG': '0xB6', 'POS': 4, 'RegisterName': 'OTP FIELDS 6', 'RegisterLength': 8, 'Name': 'otp_ds_dvr_ocp_ref_hs_trim[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x88', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=code)

          # 4. leggiamo di nuovo l’uscita del comparatore # @ATE "GND" = > "PGND"
          trigger = VTRIG_LH(signal="IODATA0", reference="GND", threshold=1.8,expected_value=0)

          # 5. se abbiamo superato la soglia, abbiamo finito
          if trigger:
              print(f"trim code = {code:.3f} ")
              break
          
    # @ATE "GND" = > "PGND"
  AFORCE(signal="OUTN", reference="GND", value=float('Inf'), error_spread=0.01)  # stop forcing

  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'spk_en', 'length': 1, 'registers': [{'REG': '0x9F', 'POS': 0, 'RegisterName': 'Enables settings 5', 'RegisterLength': 8, 'Name': 'spk_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000S', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0)  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0) #only bit 2 need to be changed
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_data_dwa', 'length': 9, 'registers': [{'REG': '0x11', 'POS': 0, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_data_dwa[8]', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 8, 'FieldLSB': 8, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0x12', 'POS': 0, 'RegisterName': 'DAC test 2', 'RegisterLength': 8, 'Name': 'tst_data_dwa[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_dac', 'length': 1, 'registers': [{'REG': '0x11', 'POS': 7, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_dac', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)

if __name__ == '__main__':
  ocp_hs_trim()