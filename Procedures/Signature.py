from dfttools import *
from Procedures.Startup import startup 
from Procedures.Global_enable import global_enable

def Signature_burn():
  startup()
  global_enable()
  I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},   write_value=1)
  
  REG_B0=I2C_REG_READ("0x38", xB0, x00, PageNo=1)
  REG_B1=I2C_REG_READ("0x38", xB1, x00, PageNo=1)
  REG_B2=I2C_REG_READ("0x38", xB2, x00, PageNo=1)
  REG_B3=I2C_REG_READ("0x38", xB3, x00, PageNo=1)
  REG_B4=I2C_REG_READ("0x38", xB4, x00, PageNo=1)
  REG_B5=I2C_REG_READ("0x38", xB5, x00, PageNo=1)
  REG_B6=I2C_REG_READ("0x38", xB6, x00, PageNo=1)
  REG_B7=I2C_REG_READ("0x38", xB7, x00, PageNo=1)
  REG_B8=I2C_REG_READ("0x38", xB8, x00, PageNo=1)
  REG_B9=I2C_REG_READ("0x38", xB9, x00, PageNo=1)
  REG_BA=I2C_REG_READ("0x38", xBA, x00, PageNo=1)
  REG_BB=I2C_REG_READ("0x38", xBB, x00, PageNo=1)
  REG_BC=I2C_REG_READ("0x38", xBC, x00, PageNo=1)
  REG_BD=I2C_REG_READ("0x38", xBD, x00, PageNo=1)
  REG_BE=I2C_REG_READ("0x38", xBE, x00, PageNo=1)
  REG_BF=I2C_REG_READ("0x38", xBF, x00, PageNo=1)
  
  REG_D0=REG_B0^REG_B1^REG_B2^REG_B3^REG_B4^REG_B5^_REG_B6^_REG_B7^REG_B8^REG_B9^REG_BA^REG_BB^REG_BC^REG_BD^REG_BE^REG_BF

  REG_C0=I2C_REG_READ("0x38", xC0, x00, PageNo=1)
  REG_C1=I2C_REG_READ("0x38", xC1, x00, PageNo=1)
  REG_C2=I2C_REG_READ("0x38", xC2, x00, PageNo=1)
  REG_C3=I2C_REG_READ("0x38", xC3, x00, PageNo=1)
  REG_C4=I2C_REG_READ("0x38", xC4, x00, PageNo=1)
  REG_C5=I2C_REG_READ("0x38", xC5, x00, PageNo=1)
  REG_C6=I2C_REG_READ("0x38", xC6, x00, PageNo=1)
  REG_C7=I2C_REG_READ("0x38", xC7, x00, PageNo=1)
  REG_C8=I2C_REG_READ("0x38", xC8, x00, PageNo=1)
  REG_C9=I2C_REG_READ("0x38", xC9, x00, PageNo=1)
  REG_CA=I2C_REG_READ("0x38", xCA, x00, PageNo=1)
  REG_CB=I2C_REG_READ("0x38", xCB, x00, PageNo=1)
  REG_CC=I2C_REG_READ("0x38", xCC, x00, PageNo=1)
  REG_CD=I2C_REG_READ("0x38", xCD, x00, PageNo=1)
  REG_CE=I2C_REG_READ("0x38", xCE, x00, PageNo=1)
  REG_CF=I2C_REG_READ("0x38", xCF, x00, PageNo=1)
  
  REG_D1=REG_C0^REG_C1^REG_C2^REG_C3^REG_C4^REG_C5^_REG_C6^_REG_C7^REG_C8^REG_C9^REG_CA^REG_CB^REG_CC^REG_CD^REG_CE^REG_CF

  I2C_REG_WRITE(device_address="0x38", register_address=xD0, write_value=REG_D0, PageNo=1)
  I2C_REG_WRITE(device_address="0x38", register_address=xD1, write_value=REG_D1, PageNo=1)
 