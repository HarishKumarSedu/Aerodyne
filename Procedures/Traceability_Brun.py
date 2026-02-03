from dfttools import *
from Procedures.Startup import startup 
from Procedures.Global_enable import global_enable

def traceability_burn():
  print('traceability_burn')
  startup()
  global_enable()
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},   write_value=1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_burn', 'length': 1, 'registers': [{'REG': '0xAE', 'POS': 1, 'RegisterName': 'OTP control reg 1', 'RegisterLength': 8, 'Name': 'otp_burn', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'R0000NNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_traceability', 'length': 1, 'registers': [{'REG': '0xAE', 'POS': 2, 'RegisterName': 'OTP control reg 1', 'RegisterLength': 8, 'Name': 'otp_traceability', 'Mask': '0x4', 'Length': 1, 'FieldMSB': 2, 'FieldLSB': 2, 'Attribute': 'R0000NNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1) 
  # load otp value 
  I2C_REG_WRITE(device_address="0x38", register_address=0xBC, write_value=0x25, PageNo=1)
  I2C_REG_WRITE(device_address="0x38", register_address=0xBD, write_value=0x69, PageNo=1)
  # register 0XBE in LOT number 3 digits #1
  I2C_REG_WRITE(device_address="0x38", register_address=0xBE, write_value=0x00, PageNo=1)
  # register  0XBF in LOT number 3 digits #2
  I2C_REG_WRITE(device_address="0x38", register_address=0xBF, write_value=0x00, PageNo=1)
  # register  0XBC0 in LOT number 3 digits #3
  I2C_REG_WRITE(device_address="0x38", register_address=0xC0, write_value=0x00, PageNo=1)
  # register   0XC1 in  bits[7:5]=0x02 | bits[4:0] Wafer number
  I2C_REG_WRITE(device_address="0x38", register_address=0xC1, write_value=0x00, PageNo=1)
  # register   0XC2 in  diex
  I2C_REG_WRITE(device_address="0x38", register_address=0xC2, write_value=0x00, PageNo=1)
  # register   0XC3 in  diey
  I2C_REG_WRITE(device_address="0x38", register_address=0xC3, write_value=0x00, PageNo=1)
  I2C_REG_WRITE(device_address="0x38", register_address=0xC4, write_value=0x2A, PageNo=1)
  I2C_REG_WRITE(device_address="0x38", register_address=0xC5, write_value=0x31, PageNo=1)
  # register   0XC6 in  bits[7:5] Probe W day | bits[4:0]=0x1
  I2C_REG_WRITE(device_address="0x38", register_address=0xC6, write_value=0x01, PageNo=1)
  I2C_REG_WRITE(device_address="0x38", register_address=0xC7, write_value=0x00, PageNo=1)

  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_burn', 'length': 1, 'registers': [{'REG': '0xAE', 'POS': 1, 'RegisterName': 'OTP control reg 1', 'RegisterLength': 8, 'Name': 'otp_burn', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'R0000NNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)


if __name__ == '__main__':
  traceability_burn()
  