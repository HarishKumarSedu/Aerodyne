from time import sleep
import os 
import sys
# example code to install python pacakage
# command = f"{sys.executable} -m pip uninstall dfttools -y"
# os.system(command)
# command = f"{sys.executable} -m pip install git+https://github.com/HarishKumarSedu/dfttools.git@main"
# os.system(command)

from dfttools import *
def startup():
  Test_Name = 'Startup'
  print(f'............ {Test_Name} ........')
  VFORCE(signal="VDD",reference="GND",value=1.8)
  VFORCE(signal="RESETB",reference="GND",value=1.8)
  VFORCE(signal="PVDD",reference="GND",value=3.7)

  sleep(0.2)

  
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_mode', 'length': 2, 'registers': [{'REG': '0x84', 'POS': 6, 'RegisterName': 'PLL_REG_5', 'RegisterLength': 8, 'Name': 'pll_mode[1:0]', 'Mask': '0xC0', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x17', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x2)
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_ldet_cnt', 'length': 5, 'registers': [{'REG': '0x83', 'POS': 0, 'RegisterName': 'PLL reg 4', 'RegisterLength': 8, 'Name': 'pll_ldet_cnt[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': '000NNNNN', 'Default': '0x10', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
  # Switch to page 1
  I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1)
  # Unlock test page 
  I2C_REG_WRITE( device_address="0x38", register_address=0x2F, write_value=0xAA,PageNo=1)
  I2C_REG_WRITE( device_address="0x38", register_address=0x2F, write_value=0xBB,PageNo=1)
  # Switch to page 0
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'iopad0_hyst', 'length': 1, 'registers': [{'REG': '0x38', 'POS': 0, 'RegisterName': 'IOPAD0 pad config', 'RegisterLength': 8, 'Name': 'iopad0_hyst', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNN000N', 'Default': '0x00', 'User': '00YYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'iodata1_hyst', 'length': 1, 'registers': [{'REG': '0x39', 'POS': 3, 'RegisterName': 'IODATA1 pad config', 'RegisterLength': 8, 'Name': 'iodata1_hyst', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NN00N0NN', 'Default': '0x00', 'User': '00YYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ioclk1_hyst', 'length': 1, 'registers': [{'REG': '0x3A', 'POS': 3, 'RegisterName': 'IOCLK1 pad config', 'RegisterLength': 8, 'Name': 'ioclk1_hyst', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNN0NN', 'Default': '0x00', 'User': '00YYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ioclk2_hyst', 'length': 1, 'registers': [{'REG': '0x3C', 'POS': 3, 'RegisterName': 'IOCLK2 pad config', 'RegisterLength': 8, 'Name': 'ioclk2_hyst', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNN0NN', 'Default': '0x00', 'User': '00YYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
  cal_meas_code = I2C_READ(device_address="0x38",field_info={'fieldname': 'cal_meas', 'length': 10, 'registers': [{'REG': '0x25', 'POS': 0, 'RegisterName': 'CAL measurement reg 1', 'RegisterLength': 8, 'Name': 'cal_meas[9:8]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 9, 'FieldLSB': 8, 'Attribute': '000000RR', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x26', 'POS': 0, 'RegisterName': 'CAL measurement reg 2', 'RegisterLength': 8, 'Name': 'cal_meas[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]},expected_value=0x0)
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'prechg_step_time', 'length': 2, 'registers': [{'REG': '0x2D', 'POS': 2, 'RegisterName': 'Sequencer settings 2', 'RegisterLength': 8, 'Name': 'prechg_step_time[1:0]', 'Mask': '0xC', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x50', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x2)


if __name__ == '__main__':
  startup()