Test_Name = 'VI_SNS_turn_on'
from dfttools import *
def vi_sns_turn_on():
  print(f'............ {Test_Name} ........')
  I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  I2C_REG_WRITE( device_address="0x38", register_address=0xA7, write_value=0x3,PageNo=0) # enable the v and i channel

if __name__ == '__main__':
  vi_sns_turn_on()