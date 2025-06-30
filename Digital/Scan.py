from dfttools import *
from time import sleep

Test_Name = 'COMPRESSED_SCAN_DIG_TOP'
from Procedures import Startup
print(f'............ {Test_Name} ........')
# designers must go through the details and correct the procedure
'''
Procedure 
    1.Startup (it includes enable of test page)
    2.Enable scan compression
    3.Start scan for stuck at/transition/iddq patterns
'''

# Switch to page 1
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)

# Enable scan compression
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'scanx_enh', 'length': 1, 'registers': [{'REG': '0x05', 'POS': 0, 'RegisterName': 'SCAN Test', 'RegisterLength': 8, 'Name': 'scanx_enh', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '000000NN', 'Default': '18', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'A', 'PageName': 'PAG1'}]}, write_value=0x1)

# Start scan
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'scan_enh', 'length': 1, 'registers': [{'REG': '0x05', 'POS': 1, 'RegisterName': 'SCAN Test', 'RegisterLength': 8, 'Name': 'scan_enh', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '000000NN', 'Default': '18', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'A', 'PageName': 'PAG1'}]}, write_value=0x1)
