from dfttools import *
from Procedures.Startup import startup 
from Procedures.Global_enable import global_enable

def Signature_burn():
  print('Signature_burn')
  startup()
  global_enable()
  I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},   write_value=1)
# this is an example, in the real case you need to combine the OTP values you have found to create the values of the registers from B0 to BF
  
  REG_B0=I2C_REG_READ("0x38", 0xB0, 0x00, PageNo=1)
  REG_B1=I2C_REG_READ("0x38", 0xB1, 0x00, PageNo=1)
  REG_B2=I2C_REG_READ("0x38", 0xB2, 0x00, PageNo=1)
  REG_B3=I2C_REG_READ("0x38", 0xB3, 0x00, PageNo=1)
  REG_B4=I2C_REG_READ("0x38", 0xB4, 0x00, PageNo=1)
  REG_B5=I2C_REG_READ("0x38", 0xB5, 0x00, PageNo=1)
  REG_B6=I2C_REG_READ("0x38", 0xB6, 0x00, PageNo=1)
  REG_B7=I2C_REG_READ("0x38", 0xB7, 0x00, PageNo=1)
  REG_B8=I2C_REG_READ("0x38", 0xB8, 0x00, PageNo=1)
  REG_B9=I2C_REG_READ("0x38", 0xB9, 0x00, PageNo=1)
  REG_BA=I2C_REG_READ("0x38", 0xBA, 0x00, PageNo=1)
  REG_BB=I2C_REG_READ("0x38", 0xBB, 0x00, PageNo=1)
  REG_BC=I2C_REG_READ("0x38", 0xBC, 0x00, PageNo=1)
  REG_BD=I2C_REG_READ("0x38", 0xBD, 0x00, PageNo=1)
  REG_BE=I2C_REG_READ("0x38", 0xBE, 0x00, PageNo=1)
  REG_BF=I2C_REG_READ("0x38", 0xBF, 0x00, PageNo=1)
  
  REG_D0=REG_B0^REG_B1^REG_B2^REG_B3^REG_B4^REG_B5^REG_B6^REG_B7^REG_B8^REG_B9^REG_BA^REG_BB^REG_BC^REG_BD^REG_BE^REG_BF

  # this is an example, in the real case you need to combine the OTP values you have found to create the values of the registers from C0 to CF
  REG_C0=I2C_REG_READ("0x38", 0xC0, 0x00, PageNo=1)
  REG_C1=I2C_REG_READ("0x38", 0xC1, 0x00, PageNo=1)
  REG_C2=I2C_REG_READ("0x38", 0xC2, 0x00, PageNo=1)
  REG_C3=I2C_REG_READ("0x38", 0xC3, 0x00, PageNo=1)
  REG_C4=I2C_REG_READ("0x38", 0xC4, 0x00, PageNo=1)
  REG_C5=I2C_REG_READ("0x38", 0xC5, 0x00, PageNo=1)
  REG_C6=I2C_REG_READ("0x38", 0xC6, 0x00, PageNo=1)
  REG_C7=I2C_REG_READ("0x38", 0xC7, 0x00, PageNo=1)
  REG_C8=I2C_REG_READ("0x38", 0xC8, 0x00, PageNo=1)
  REG_C9=I2C_REG_READ("0x38", 0xC9, 0x00, PageNo=1)
  REG_CA=I2C_REG_READ("0x38", 0xCA, 0x00, PageNo=1)
  REG_CB=I2C_REG_READ("0x38", 0xCB, 0x00, PageNo=1)
  REG_CC=I2C_REG_READ("0x38", 0xCC, 0x00, PageNo=1)
  REG_CD=I2C_REG_READ("0x38", 0xCD, 0x00, PageNo=1)
  REG_CE=I2C_REG_READ("0x38", 0xCE, 0x00, PageNo=1)
  REG_CF=I2C_REG_READ("0x38", 0xCF, 0x00, PageNo=1)
  REG_D1=REG_C0^REG_C1^REG_C2^REG_C3^REG_C4^REG_C5^REG_C6^REG_C7^REG_C8^REG_C9^REG_CA^REG_CB^REG_CC^REG_CD^REG_CE^REG_CF

  I2C_REG_WRITE(device_address="0x38", register_address=0xD0, write_value=REG_D0, PageNo=1)
  I2C_REG_WRITE(device_address="0x38", register_address=0xD1, write_value=REG_D1, PageNo=1)

if __name__ == '__main__':
  Signature_burn()
  
 