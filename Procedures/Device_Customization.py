from dfttools import *
from Procedures.Startup import startup 
from Procedures.Global_enable import global_enable
# from Digital.OTP_Burning import otp_burning
def device_customization():
  startup()
  global_enable()
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_power_island_en', 'length': 1, 'registers': [{'REG': '0xCB', 'POS': 1, 'RegisterName': 'OTP FIELDS 27', 'RegisterLength': 8, 'Name': 'otp_power_island_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_platform_en', 'length': 1, 'registers': [{'REG': '0xB4', 'POS': 7, 'RegisterName': 'OTP FIELDS 4', 'RegisterLength': 8, 'Name': 'otp_platform_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x04', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)