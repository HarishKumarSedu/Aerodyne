from dfttools import *
from time import sleep
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback
from Procedures.VI_SNS_turn_on import vi_sns_turn_on
from Procedures.VI_SNS_turn_off import vi_sns_turn_off

from time import sleep
def vis_gain_v2i():
    Testname = 'VIS_GAIN_V2I'
    print(f' {Testname}')
    startup()
    VFORCE ("PVDD","GND",2.5,0)
    global_enable()
    playback()
    vi_sns_turn_on()
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_data_dwa', 'length': 9, 'registers': [{'REG': '0x11', 'POS': 0, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_data_dwa[8]', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 8, 'FieldLSB': 8, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0x12', 'POS': 0, 'RegisterName': 'DAC test 2', 'RegisterLength': 8, 'Name': 'tst_data_dwa[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0xFF) # Turn on DAC positive side 
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_dac', 'length': 1, 'registers': [{'REG': '0x11', 'POS': 7, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_dac', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1) # Turn on DAC 
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0)
    sleep(0.1)
    current_lsb = 3/2**15
    voltage_lsb =  (5.5/2**15)
    
    vsns_gain_high_measured = I2C_READ(device_address="0x38", field_info={'fieldname': 'v_sense', 'length': 16, 'registers': [{'REG': '0x69', 'POS': 0, 'RegisterName': 'V SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'v_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6A', 'POS': 0, 'RegisterName': 'V SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'v_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=-14886)
    isns_gain_high_measured = I2C_READ(device_address="0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=-1006)
    isns_gain_high_measured =  -(0x10000 - isns_gain_high_measured)    if isns_gain_high_measured & 0x8000 else isns_gain_high_measured
    vsns_gain_high_measured =  -(0x10000 - vsns_gain_high_measured)    if vsns_gain_high_measured & 0x8000 else vsns_gain_high_measured
    print(f'vsns_gain_high_measured : {vsns_gain_high_measured}, voltage : {vsns_gain_high_measured*voltage_lsb}')
    print(f'isns_gain_high_measured : {isns_gain_high_measured}, current : {current_lsb*isns_gain_high_measured}')

    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_data_dwa', 'length': 9, 'registers': [{'REG': '0x11', 'POS': 0, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_data_dwa[8]', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 8, 'FieldLSB': 8, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0x12', 'POS': 0, 'RegisterName': 'DAC test 2', 'RegisterLength': 8, 'Name': 'tst_data_dwa[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x100) # Turn on DAC negative side 
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0)

    sleep(0.1)
    vsns_gain_low_measured = I2C_READ(device_address="0x38", field_info={'fieldname': 'v_sense', 'length': 16, 'registers': [{'REG': '0x69', 'POS': 0, 'RegisterName': 'V SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'v_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6A', 'POS': 0, 'RegisterName': 'V SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'v_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=14893)
    isns_gain_low_measured = I2C_READ(device_address="0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=-129)
 
    isns_gain_low_measured =  -(0x10000 - isns_gain_low_measured )    if isns_gain_low_measured & 0x8000 else isns_gain_low_measured
    vsns_gain_low_measured = -( 0x10000 - vsns_gain_low_measured)    if vsns_gain_low_measured & 0x8000 else vsns_gain_low_measured
    print(f'vsns_gain_low_measured : {vsns_gain_low_measured}, voltage : {vsns_gain_low_measured*voltage_lsb}')
    print(f'isns_gain_low_measured : {isns_gain_low_measured}, current : {current_lsb*isns_gain_low_measured}')
    scale_down = (2**20/64)
    v2i_gain = -int((((isns_gain_high_measured  - isns_gain_low_measured) /(vsns_gain_high_measured - vsns_gain_low_measured)) * (((3*5.5)/(20*5))*scale_down)))  # convert it to the 12bit value
    v2i_gain_code = 0x1000 + v2i_gain  if v2i_gain < 0  else  v2i_gain 
 
    print(f'v2i_gain_code {hex(v2i_gain_code)}')
    VFORCE ("PVDD","GND",3.7,0)
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_isense_from_vsense_gain', 'length': 12, 'registers': [{'REG': '0xBF', 'POS': 0, 'RegisterName': 'OTP FIELDS 15 - TRACEABILITY 3', 'RegisterLength': 8, 'Name': 'otp_isense_from_vsense_gain[11:8]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 11, 'FieldLSB': 8, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xC0', 'POS': 0, 'RegisterName': 'OTP FIELDS 16 - TRACEABILITY 4', 'RegisterLength': 8, 'Name': 'otp_isense_from_vsense_gain[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=v2i_gain_code) # Turn on DAC positive side 0xFa9 could be typical gain code 
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_data_dwa', 'length': 9, 'registers': [{'REG': '0x11', 'POS': 0, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_data_dwa[8]', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 8, 'FieldLSB': 8, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0x12', 'POS': 0, 'RegisterName': 'DAC test 2', 'RegisterLength': 8, 'Name': 'tst_data_dwa[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x00) # Turn on DAC positive side 
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_dac', 'length': 1, 'registers': [{'REG': '0x11', 'POS': 7, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_dac', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0) # Turn off DAC 
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0)
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'spk_en', 'length': 1, 'registers': [{'REG': '0x9F', 'POS': 0, 'RegisterName': 'Enables settings 5', 'RegisterLength': 8, 'Name': 'spk_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000S', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0)
    vi_sns_turn_off()
  
if  __name__ == '__main__':
  vis_gain_v2i()