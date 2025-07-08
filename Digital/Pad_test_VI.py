from dfttools import *
from time import sleep

Test_Name = 'PAD_TEST_VI'
from Procedures import Startup
print(f'............ {Test_Name} ........')
# designers must go through the details and correct the procedure
'''
Procedure 
    1.Startup (it includes enable of test page)
    2.Global_en to turn on the island
    2.Enable of read test mode of all pads except I2C ones
    3.Check the result
'''

# Set {'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]} to 1
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)

# Switch to page 1
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)

# Enable of read test mode
I2C_REG_WRITE( device_address="0x38", register_address=0x00, write_value=0x08,PageNo=1)

# Force all pads to 1
VFORCE(signal="ADDR",reference="GND",value=1.8)
VFORCE(signal="IODATA1",reference="GND",value=1.8)
VFORCE(signal="IOCLK1",reference="GND",value=1.8)
VFORCE(signal="IODATA0",reference="GND",value=1.8)
VFORCE(signal="IOCLK0",reference="GND",value=1.8)

HCODE0=I2C_READ(device_address="0x38",field_info={'fieldname': 'io_tst_rd', 'length': 7, 'registers': [{'REG': '0x02', 'POS': 0, 'RegisterName': 'IO_TEST_SETTINGS_3', 'RegisterLength': 8, 'Name': 'io_tst_rd[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0RRRRRRR', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},expected_value=0x1F)

if (HCODE0 == 0x1F) :
  print(f'............ {Test_Name} Passed ........')

#############################################

# Force all pads to 0
VFORCE(signal="ADDR",reference="GND",value=0)
VFORCE(signal="IODATA1",reference="GND",value=0)
VFORCE(signal="IOCLK1",reference="GND",value=0)
VFORCE(signal="IODATA0",reference="GND",value=0)
VFORCE(signal="IOCLK0",reference="GND",value=0)

HCODE0=I2C_READ(device_address="0x38",field_info={'fieldname': 'io_tst_rd', 'length': 7, 'registers': [{'REG': '0x02', 'POS': 0, 'RegisterName': 'IO_TEST_SETTINGS_3', 'RegisterLength': 8, 'Name': 'io_tst_rd[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0RRRRRRR', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},expected_value=0x00)

if (HCODE0 == 0x00) :
  print(f'............ {Test_Name} Passed ........')


