from time import sleep
import os 
import sys
# example code to install python pacakage
# command = f"{sys.executable} -m pip uninstall dfttools -y"
# os.system(command)
# command = f"{sys.executable} -m pip install git+https://github.com/HarishKumarSedu/dfttools.git@main"
# os.system(command)

Test_Name = 'Startup'
print(f'............ {Test_Name} ........')
from dfttools import *

VFORCE(signal="VDD",reference="GND",value=1.8)
VFORCE(signal="RESETB",reference="GND",value=1.8)
VMEASURE(signal="PVDD",reference="GND",expected_value=3.7)

sleep(0.001)

# Switch to page 1
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
# Unlock test page 
I2C_REG_WRITE( device_address="0x68", register_address=0x2F, write_value=0xAA)
I2C_REG_WRITE( device_address="0x68", register_address=0x2F, write_value=0xBB)
# Switch to page 0
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)

