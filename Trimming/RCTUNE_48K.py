from dfttools import *
from time import sleep

from Procedures.Startup import startup

def rctune_48k():
  Test_Name = 'RCTUNE_48K'
  print(f'............ {Test_Name} ........')
  # designers must go through the details and correct the procedure
  '''
  Procedure 
    before to start the bandgap has to be trimmed
    1.Set 48KHz Family
    2.Run rctune procedure

  '''
  startup()
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
  sleep(0.001)

  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'vis_rctun_sel', 'length': 1, 'registers': [{'REG': '0x60', 'POS': 3, 'RegisterName': 'VIS setting reg 0', 'RegisterLength': 8, 'Name': 'vis_rctun_sel', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x0C', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_clk12m_bypass', 'length': 1, 'registers': [{'REG': '0x80', 'POS': 3, 'RegisterName': 'PLL_REG_1', 'RegisterLength': 8, 'Name': 'pll_clk12m_bypass', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x21', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)

  sleep(0.001)
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'rc_tun_start', 'length': 1, 'registers': [{'REG': '0x62', 'POS': 0, 'RegisterName': 'VIS setting reg 2', 'RegisterLength': 8, 'Name': 'rc_tun_start', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000P', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
  sleep(0.001)


  print(f"Procedure finish")

  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'vis_rctun_sel', 'length': 1, 'registers': [{'REG': '0x60', 'POS': 3, 'RegisterName': 'VIS setting reg 0', 'RegisterLength': 8, 'Name': 'vis_rctun_sel', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x0C', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
  sleep(0.001)
  I2C_WRITE(device_address="0x38",field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)

if __name__ == '__main__':
  rctune_48k()