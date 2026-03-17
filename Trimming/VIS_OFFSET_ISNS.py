from dfttools import *
from time import sleep
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback
from Procedures.VI_SNS_turn_on import vi_sns_turn_on
from Procedures.VI_SNS_turn_off import vi_sns_turn_off
from Procedures.utils import complement,dec_to_2complement

def vis_offset_isns():
  Testname = 'VIS_OFFSET_ISNS'
  print(f'\n{"*"*20}{Testname}{"*"*20}')
  LSB1 = 3/2**15
  LSB2 =  20/2**20
  lsb_ratio = LSB1/LSB2
  # execute the necessary procedures in order 
  startup()
  global_enable()
  # Put the it into the Playback mode then go to standlone 
  # apply 3.072MHz Clolk @ "IOCLK0"
  playback()
  # call Vi sense tunr off block
  vi_sns_turn_on()
  isns_field_length = 16
  otp_isense_offset_field_length = 7 
  # read the vsense voltage 
  I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  isns_pretrim_offset_code_raw = I2C_READ("0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x140)
  isns_pretrim_offset_code = complement(isns_pretrim_offset_code_raw,isns_field_length)
  print('=================== ISNS PRE-TRIM ====================')
  sns_pretrim_offset_value = isns_pretrim_offset_code*LSB1
  print(f'Isns Offset :~ {sns_pretrim_offset_value:.6f} A [{isns_pretrim_offset_code_raw:#04X}]')
  isns_offset_calculated = -(round(isns_pretrim_offset_code*lsb_ratio) >> 7 & 0x7F)
  isns_offset_otp_code = dec_to_2complement(value_dec=isns_offset_calculated,bit_len=otp_isense_offset_field_length,max_1=False)
  I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
  I2C_WRITE("0x38", field_info={'fieldname': 'otp_isense_offset', 'length': 7, 'registers': [{'REG': '0xBA', 'POS': 0, 'RegisterName': 'OTP FIELDS 10', 'RegisterLength': 8, 'Name': 'otp_isense_offset[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xCC', 'POS': 7, 'RegisterName': 'OTP FIELDS 28', 'RegisterLength': 8, 'Name': 'otp_isense_offset[6]', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=isns_offset_otp_code)
  print('================== ISNS POST-TRIM ===================')
  isns_posttrim_offset_code_raw = I2C_READ("0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0xFFFE)
  isns_posttrim_offset_code = complement(isns_posttrim_offset_code_raw,isns_field_length)
  sns_posttrim_offset_value = isns_posttrim_offset_code*LSB1
  print(f'Isns Offset :~ {sns_posttrim_offset_value:.6f} A [{isns_posttrim_offset_code_raw:#04X}]')
  vi_sns_turn_off()
  I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  I2C_WRITE("0x38", field_info={'fieldname': 'spk_en', 'length': 1, 'registers': [{'REG': '0x9F', 'POS': 0, 'RegisterName': 'Enables settings 5', 'RegisterLength': 8, 'Name': 'spk_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000S', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  print(f'{"*"*50}')

if __name__ == '__main__':
  vis_offset_isns()