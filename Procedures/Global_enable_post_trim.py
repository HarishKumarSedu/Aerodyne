from dfttools import *
def global_enable_post_trim():
  Test_Name = 'Global_enable_post_trim'
  print(f'............ {Test_Name} ........')
  I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x00,PageNo=0)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)
