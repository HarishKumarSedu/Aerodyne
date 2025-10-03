from dfttools import *
from time import sleep
import random

Test_Name = 'ana_reference_th'
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
def ana_pll_th():
  print(f'............ {Test_Name} ........')
  startup()
  global_enable()
  test_blk = {
    "pll_vco_v2i_core_current" : { "test_selection_code" : 0, "target" : 0.5e-6, "unit" : "A"  , "error_percentage": 1e-2},
    "VDD_VCO"                  : { "test_selection_code" : 1, "target" : 0.68, "unit" : "V"  , "error_percentage": 1e-2},
  }
  BLCK_Set = 3.072e6  
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_mode', 'length': 2, 'registers': [{'REG': '0x84', 'POS': 6, 'RegisterName': 'PLL_REG_5', 'RegisterLength': 8, 'Name': 'pll_mode[1:0]', 'Mask': '0xC0', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x17', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(2))      #dig_pll_freerun_en_vddd=0
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_p', 'length': 6, 'registers': [{'REG': '0x81', 'POS': 0, 'RegisterName': 'PLL reg 2', 'RegisterLength': 8, 'Name': 'pll_p[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': '00NNNNNN', 'Default': '0x06', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(6))         #dig_pll_prediv_vddd<5:0>=6d 
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_n', 'length': 6, 'registers': [{'REG': '0x82', 'POS': 0, 'RegisterName': 'PLL reg 3', 'RegisterLength': 8, 'Name': 'pll_n[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': '00NNNNNN', 'Default': '0x18', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(18))        #dig_pll_n<5:0>=24d 
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_ldet_cnt', 'length': 5, 'registers': [{'REG': '0x83', 'POS': 0, 'RegisterName': 'PLL reg 4', 'RegisterLength': 8, 'Name': 'pll_ldet_cnt[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': '000NNNNN', 'Default': '0x10', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(10)) #rfu_pll_ldet_cnt<4:0>=16d
  FREQFORCE(signal="IOCLK0",reference="GND",value=BLCK_Set)                            #BCLK frequency=3.072MHz
  # Enabling test page
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)  #Change page in regmap
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
  
  for ref_test_name, ref_test in test_blk.items():
    measured_value = 0 # default 
    # if the test is voltage measure select multimeter / if there is no unit default is ''
    if ref_test.get('unit','') == 'V':
      I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=ref_test.get('test_selection_code',1)) # test selection 
      I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pll_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'pll_test_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)   #enable ANA_TESTMUX1
      sleep(0.01)
      target_value = ref_test.get('target',0) # default is 0
      error_percentage = ref_test.get('error_percentage',0) # default is 0
      measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=target_value,error_spread=target_value*error_percentage)
      I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pll_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'pll_test_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)   #enable ANA_TESTMUX1
      VMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf')) # open switch 

    # current measurements 
    if ref_test.get('unit','') == 'A':
      I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=ref_test.get('test_selection_code',1)) # test selection 
      I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pll_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'pll_test_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)   #enable ANA_TESTMUX1
      sleep(0.1)
      target_value = ref_test.get('target',0) # default is 0
      error_percentage = ref_test.get('error_percentage',0) # default is 0
      measured_value = AMEASURE(signal="IODATA1", reference="GND", expected_value=target_value,error_spread=target_value*error_percentage)
      I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pll_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'pll_test_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)   #enable ANA_TESTMUX1
      AMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf')) # open switch 
    # update the measured value 
    ref_test.update(
      {
        "measured_value" : measured_value
      }
    )

    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pll_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'pll_test_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)   #enable ANA_TESTMUX1
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)   #enable "IODATA1"
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)      #enable VDD_VCO voltage test

  return test_blk
if __name__ == '__main__':
  ref_test_results = ana_pll_th()
  print(ana_pll_th)