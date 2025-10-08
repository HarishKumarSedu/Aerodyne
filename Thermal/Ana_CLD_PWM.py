from dfttools import *
from time import sleep
import random

Test_Name = 'ana_reference_th'
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback
def ana_cld_pwm_th():
  print(f'............ {Test_Name} ........')
  startup()
  global_enable()
  playback()
  test_blk = {
    "Ibias_n"    : { "test_selection_code" : 0, "target" : 1e-6, "unit" : "A"  , "error_percentage": 2e-2},
    "vhi"        : { "test_selection_code" : 1, "target" : 0.75, "unit" : "A"  , "error_percentage": 2e-2},
    "vlow"       : { "test_selection_code" : 2, "target" : 0, "unit" : "V"  , "error_percentage": 2e-2},
    "Iramp_copy" : { "test_selection_code" : 3, "target" : 1.5e-6, "unit" : "V"  , "error_percentage": 2e-2},
  }
  BLCK_Set = 3.072e6  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_pwm_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 5, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'cld_pwm_test_en', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)  # Enable current test mode
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x00)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
  FREQFORCE(signal="IOCLK0",reference="GND",value=BLCK_Set)                            #BCLK frequency=3.072MHz
  # Enabling test page
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)  #Change page in regmap
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
  
  for pwm_test_name, pwm_test in test_blk.items():
    measured_value = 0 # default 
    # if the test is voltage measure select multimeter / if there is no unit default is ''
    if pwm_test.get('unit','') == 'V':
      I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=pwm_test.get('test_selection_code',1))
      sleep(0.01)
      target_value = pwm_test.get('target',0) # default is 0
      error_percentage = pwm_test.get('error_percentage',0) # default is 0
      measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=target_value,error_spread=target_value*error_percentage)
      VMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf')) # open switch 

    # current measurements 
    if pwm_test.get('unit','') == 'A':
      I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=pwm_test.get('test_selection_code',1)) # test selection 
      sleep(0.1)
      target_value = pwm_test.get('target',0) # default is 0
      error_percentage = pwm_test.get('error_percentage',0) # default is 0
      measured_value = AMEASURE(signal="IODATA1", reference="GND", expected_value=target_value,error_spread=target_value*error_percentage)
      I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pll_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'pll_test_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)   #enable ANA_TESTMUX1
      AMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf')) # open switch 


  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_pwm_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 5, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'cld_pwm_test_en', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)  # Enable current test mode
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x00)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)

  return test_blk
if __name__ == '__main__':
  ana_cld_pwm_th_thresults = ana_cld_pwm_th()
  print(ana_cld_pwm_th_thresults)