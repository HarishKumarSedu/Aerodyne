from dfttools import *
from time import sleep
import random

Test_Name = 'ana_reference_th'
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback
def ana_cld_dac_lpf_th():
  print(f'............ {Test_Name} ........')
  startup()
  global_enable()
  test_blk = {
    "as_ibias_test_500n_p2n_vdda"    : { "test_selection_code" : 0, "target" : 500e-9, "unit" : "A"  , "error_percentage": 5e-2},
    "as_dac_iLSB_copy_590nA_n2p"     : { "test_selection_code" : 12, "target" : 590e-9, "unit" : "A"  , "error_percentage": 5e-2},
    "lpf_vcm"                        : { "test_selection_code" : 1, "target" : 1.5, "unit" : "V"  , "error_percentage": 5e-2},
    "ad_dac_outc"                    : { "test_selection_code" : 10, "target" : 1.85, "unit" : "V"  , "error_percentage": 5e-2},
  }
  BLCK_Set = 3.072e6  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dac_lpf_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 4, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'cld_dac_lpf_test_en', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)  # Enable current test mode
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x00)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
  FREQFORCE(signal="IOCLK0",reference="GND",value=BLCK_Set)                            #BCLK frequency=3.072MHz
  # Enabling test page
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)  #Change page in regmap
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
  
  for lpf_test_name, lpf_test in test_blk.items():
    measured_value = 0 # default 
    # if the test is voltage measure select multimeter / if there is no unit default is ''
    if lpf_test.get('unit','') == 'V':
      I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=lpf_test.get('test_selection_code',1))
      sleep(0.01)
      target_value = lpf_test.get('target',0) # default is 0
      error_percentage = lpf_test.get('error_percentage',0) # default is 0
      measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=target_value,error_spread=target_value*error_percentage)
      VMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf')) # open switch 

    # current measurements 
    if lpf_test_name == 'as_ibias_test_500n_p2n_vdda':
      I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=lpf_test.get('test_selection_code',1)) # test selection 
      sleep(0.1)
      target_value = lpf_test.get('target',0) # default is 0
      error_percentage = lpf_test.get('error_percentage',0) # default is 0
      measured_value = AMEASURE(signal="IODATA1", reference="GND", expected_value=target_value,error_spread=target_value*error_percentage)
      I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pll_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'pll_test_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)   #enable ANA_TESTMUX1
      AMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf')) # open switch 
    if lpf_test_name == 'as_dac_iLSB_copy_590nA_n2p':
      I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=lpf_test.get('test_selection_code',1)) # test selection 
      sleep(0.1)
      target_value = lpf_test.get('target',0) # default is 0
      error_percentage = lpf_test.get('error_percentage',0) # default is 0
      measured_value = AMEASURE(signal="VDD", reference="IODATA1", expected_value=target_value,error_spread=target_value*error_percentage)
      I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pll_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'pll_test_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)   #enable ANA_TESTMUX1
      AMEASURE(signal="VDD", reference="IODATA1", expected_value=float('Inf')) # open switch 
    # update the measured value 
    lpf_test.update(
      {
        "measured_value" : measured_value
      }
    )

  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dac_lpf_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 4, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'cld_dac_lpf_test_en', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)  # Enable current test mode
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x00)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)

  return test_blk
if __name__ == '__main__':
  ana_cld_dac_lpf_th_thresults = ana_cld_dac_lpf_th()
  print(ana_cld_dac_lpf_th_thresults)