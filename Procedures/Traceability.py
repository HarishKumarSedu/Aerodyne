from dfttools import *
from Procedures.Startup import startup 
from Procedures.Global_enable import global_enable

def traceability_burn():
  startup()
  global_enable()
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},   write_value=1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_traceability', 'length': 1, 'registers': [{'REG': '0xAE', 'POS': 2, 'RegisterName': 'OTP control reg 1', 'RegisterLength': 8, 'Name': 'otp_traceability', 'Mask': '0x4', 'Length': 1, 'FieldMSB': 2, 'FieldLSB': 2, 'Attribute': 'R0000NNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1) 
  # load otp value 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_burn', 'length': 1, 'registers': [{'REG': '0xAE', 'POS': 1, 'RegisterName': 'OTP control reg 1', 'RegisterLength': 8, 'Name': 'otp_burn', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'R0000NNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1) 
def traceability_load():
  startup()
  global_enable()
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},   write_value=1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_traceability', 'length': 1, 'registers': [{'REG': '0xAE', 'POS': 2, 'RegisterName': 'OTP control reg 1', 'RegisterLength': 8, 'Name': 'otp_traceability', 'Mask': '0x4', 'Length': 1, 'FieldMSB': 2, 'FieldLSB': 2, 'Attribute': 'R0000NNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_load', 'length': 1, 'registers': [{'REG': '0xAE', 'POS': 0, 'RegisterName': 'OTP control reg 1', 'RegisterLength': 8, 'Name': 'otp_load', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'R0000NNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1) 
  # read the burned otp values 
  


if __name__ == '__main__':
  traceability_burn()
  traceability_load()
  