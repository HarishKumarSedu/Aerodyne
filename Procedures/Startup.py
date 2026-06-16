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
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
  # Switch to page 1
  I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1)
  # Unlock test page 
  I2C_REG_WRITE( device_address="0x38", register_address=0x2F, write_value=0xAA,PageNo=1)
  I2C_REG_WRITE( device_address="0x38", register_address=0x2F, write_value=0xBB,PageNo=1)
  # Switch to page 0
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'tdm_fsyn_mnt_mode', 'length': 2, 'registers': [{'REG': '0x4E', 'POS': 4, 'RegisterName': 'TDM settings 13', 'RegisterLength': 8, 'Name': 'tdm_fsyn_mnt_mode[1:0]', 'Mask': '0x30', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x99', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)

if __name__ == '__main__':
  startup()