Test_Name = 'VI_SNS_turn_on'
from dfttools import *
from time import sleep
from Procedures.Global_enable import global_enable
def vi_sns_turn_on():
  print(f'............ {Test_Name} ........')
  global_enable()
  I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
  I2C_WRITE("0x38", field_info={'fieldname': 'vis_adc_clk_pol_v', 'length': 1, 'registers': [{'REG': '0xA6', 'POS': 2, 'RegisterName': 'Vis modulator reg', 'RegisterLength': 8, 'Name': 'vis_adc_clk_pol_v', 'Mask': '0x4', 'Length': 1, 'FieldMSB': 2, 'FieldLSB': 2, 'Attribute': '0000NNNN', 'Default': '0x0C', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  I2C_WRITE("0x38", field_info={'fieldname': 'vis_adc_clk_pol_i', 'length': 1, 'registers': [{'REG': '0xA6', 'POS': 3, 'RegisterName': 'Vis modulator reg', 'RegisterLength': 8, 'Name': 'vis_adc_clk_pol_i', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': '0000NNNN', 'Default': '0x0C', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  I2C_WRITE("0x38", field_info={'fieldname': 'vis_channel_v_en', 'length': 1, 'registers': [{'REG': '0xA7', 'POS': 0, 'RegisterName': 'Vis enables reg', 'RegisterLength': 8, 'Name': 'vis_channel_v_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '000000NN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)
  I2C_WRITE("0x38", field_info={'fieldname': 'vis_channel_i_en', 'length': 1, 'registers': [{'REG': '0xA7', 'POS': 1, 'RegisterName': 'Vis enables reg', 'RegisterLength': 8, 'Name': 'vis_channel_i_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '000000NN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)
if __name__ == '__main__':
  vi_sns_turn_on()