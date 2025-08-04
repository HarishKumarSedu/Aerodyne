from dfttools import *
from time import sleep

Test_Name = 'OTP Burning'
from Procedures import Startup
print(f'............ {Test_Name} ........')
# designers must go through the details and correct the procedure
'''
Procedure 
    1. Startup (it includes enable of test page)
    2. Global_en to turn on the island
    3. Set VDDIO to 1.6V
    4. I2C writings of OTP shadow registers
    5. {'fieldname': 'otp_burn', 'length': 1, 'registers': [{'REG': '0xAE', 'POS': 1, 'RegisterName': 'OTP control reg 1', 'RegisterLength': 8, 'Name': 'otp_burn', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'R0000NNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]} setting
'''

# Set {'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]} to 1
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)

# Switch to page 1
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)

# Enable clock for otp fsm
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'force_otp_clk_on', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 1, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'force_otp_clk_on', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)

#################### I2C writings of OTP shadow registers #####################

#################### I2C writings of OTP shadow registers #####################

# Start of burn
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_burn', 'length': 1, 'registers': [{'REG': '0xAE', 'POS': 1, 'RegisterName': 'OTP control reg 1', 'RegisterLength': 8, 'Name': 'otp_burn', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'R0000NNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)