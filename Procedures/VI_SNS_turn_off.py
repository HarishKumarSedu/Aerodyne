Test_Name = 'VI_SNS_turn_off'
from dfttools import *
def vi_sns_turn_off():
  print(f'............ {Test_Name} ........')
  FREQFORCE(signal="IOCLK0",reference="GND",value=float('Inf')) # trun off the clock  
  I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  I2C_WRITE("0x38", field_info={'fieldname': 'vis_channel_v_en', 'length': 1, 'registers': [{'REG': '0xA7', 'POS': 0, 'RegisterName': 'Vis enables reg', 'RegisterLength': 8, 'Name': 'vis_channel_v_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '000000NN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  I2C_WRITE("0x38", field_info={'fieldname': 'vis_channel_i_en', 'length': 1, 'registers': [{'REG': '0xA7', 'POS': 1, 'RegisterName': 'Vis enables reg', 'RegisterLength': 8, 'Name': 'vis_channel_i_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '000000NN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  I2C_WRITE("0x38", field_info={'fieldname': 'otp_ds_ref_bg_ptat_trm', 'length': 3, 'registers': [{'REG': '0xB3', 'POS': 5, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_ptat_trm[2:0]', 'Mask': '0xE0', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x60', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)
if __name__ == '__main__':
  vi_sns_turn_off()