from dfttools import *
from time import sleep
import random

Test_Name = 'ana_reference_th'
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
# from Trimming.REF_BUF_OFF import offset
def ana_reference_th():
  print(f'............ {Test_Name} ........')
  startup()
  global_enable()
  target_value = 0.4 # 0.4V
  # buffer_offset = offset(target_value) # 10mV
  test_blk = {
    "as_vref_0v4_pvdd_uvlo" : { "test_selection" : 1, "target" : 0.4, "unit" : "V" },
    "feedback_res" :          { "test_selection" : 2, "target" : 0.4, "unit" : "V" },
    "as_bg_vref_1v2_gndref" : { "test_selection" : 4, "target" : 1.2, "unit" : "V" },
    "as_bg_vref_0v9_gndref" : { "test_selection" : 5, "target" : 0.9, "unit" : "V" },
    "as_bg_vref_0v6_gndref" : { "test_selection" : 6, "target" : 0.6, "unit" : "V" },
    "as_bg_vref_0v4_gndref" : { "test_selection" : 7, "target" : 0.4, "unit" : "V" },
    "as_ivbgr_1u_p2n_mirror2" : { "test_selection" : 8, "target" : 0.8e-6, "unit" : "A" },
    "ref_0v6"               : { "test_selection" : 9, "target" : 0.6, "unit" : "V" },
  }
  # Enabling test page
  I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1) # page 1
  # Enabling the analog TMUX
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
  for ref_test_name, ref_test in test_blk.items():
    print(ref_test)
  # I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x7)
  # I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)

  # error_spread = target_value*0.04 # 4% of target value
  # measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=target_value,error_spread=error_spread)
  # error = abs(measured_value - target_value)/abs(target_value) *100
  # print(f"Optimal measured value : {measured_value}V, Target value : {target_value}V")
  # print(f"Minimum Error: {error}%")
  # I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
  # I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
  # I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
  # I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
if __name__ == '__main__':
  ana_reference_th()