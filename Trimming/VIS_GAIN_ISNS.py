from dfttools import *
from time import sleep
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback
from Procedures.VI_SNS_turn_on import vi_sns_turn_on
from Procedures.VI_SNS_turn_off import vi_sns_turn_off

def vis_gain_isns():
  Testname = 'VIS_GAIN_ISNS'
  print(f' {Testname}')

  '''
  The procedure is described hereafter:
  1. Force class-D output to have both SPKRP and SPKRN at VCM.
  2. Source a stated current (i.e. 500mA).
  3. Read I-sense output digital code.
  4. Sink a note current (i.e. -500mA).
  5. Read I-sense output digital code.
  6. GI=

  '''
  startup()
  global_enable()
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_ocp_en_force', 'length': 1, 'registers': [{'REG': '0x1A', 'POS': 0, 'RegisterName': 'Force registers 3', 'RegisterLength': 8, 'Name': 'cld_ocp_en_force', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1) # force ocp bit
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_ocp_en_m', 'length': 1, 'registers': [{'REG': '0x1B', 'POS': 0, 'RegisterName': 'Force registers 4', 'RegisterLength': 8, 'Name': 'cld_ocp_en_m', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0) # mode diable ocp 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'spk_gain', 'length': 3, 'registers': [{'REG': '0x92', 'POS': 0, 'RegisterName': 'SPK setting reg 1', 'RegisterLength': 8, 'Name': 'spk_gain[2:0]', 'Mask': '0x7', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': '000NNNNN', 'Default': '0x03', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x5) # adjust the speaker gain 
  playback()
  vi_sns_turn_on()
    # Force 0A between "OUTP" and "OUTN" measure the Isense offset 
  AFORCE(signal="OUTP",reference="OUTN",value=0.0, error_spread=0) # 1% error
  isns_offset_code = I2C_READ("0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x0)
  isns_offset_code = (0x10000 - isns_offset_code) if isns_offset_code & 0x8000 else isns_offset_code
  print(f' ........ 0A Current from SPKRP/SPKRM : {hex(isns_offset_code)} ........ ')
  
  source_current = 500e-3
  sleep(0.1)
  
  ############ current from outp to outn ##########################
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_data_dwa', 'length': 9, 'registers': [{'REG': '0x11', 'POS': 0, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_data_dwa[8]', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 8, 'FieldLSB': 8, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0x12', 'POS': 0, 'RegisterName': 'DAC test 2', 'RegisterLength': 8, 'Name': 'tst_data_dwa[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0xFF)  # Staturate DAC "OUTP" side 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_dac', 'length': 1, 'registers': [{'REG': '0x11', 'POS': 7, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_dac', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)  # force the switch in the selected position above
  source_current_measured = AFORCE(signal="OUTP",reference="OUTN",value=-source_current, error_spread=source_current*0.01) # 1% error sink current between outp and outn 
  sleep(0.1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0)
  isns_current_source_code = I2C_READ("0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x1555)
  # complement the 16bit isense value 
  isns_current_source_code = (0x10000 - isns_current_source_code) if isns_current_source_code & 0x8000 else isns_current_source_code
  print(f' ........ Source 500mA from SPKRP/SPKRM ........ Code {hex(isns_current_source_code)} ')
  
  ############ current from outn to outp ##########################
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_data_dwa', 'length': 9, 'registers': [{'REG': '0x11', 'POS': 0, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_data_dwa[8]', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 8, 'FieldLSB': 8, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0x12', 'POS': 0, 'RegisterName': 'DAC test 2', 'RegisterLength': 8, 'Name': 'tst_data_dwa[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x100)  # Staturate DAC "OUTN" side 
  sleep(0.1)
  sink_current_measured = AFORCE(signal="OUTN",reference="OUTP",value=-source_current, error_spread=source_current*0.01) # 1% error current from ount to outp 
  sleep(0.1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0)
  isns_current_sink_code = I2C_READ("0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0xeaab)
  isns_current_sink_code = (0x10000 - isns_current_sink_code) if isns_current_sink_code & 0x8000 else isns_current_sink_code
  print(f' ........ Sink 500mA to SPKRP/SPKRM ........ Code {hex(isns_current_sink_code)} ')
  AFORCE(signal="OUTN",reference="OUTP",value=float('Inf')) # remove current 
  
  ######## Isense Gain Calculations #####################
  LSB = (3/2**15) # lsb of the 16 bit isense value 
  Scale_Factor = (3/20) # full adapter 
  Scale_Down = (64/2**20) # weight of the isense
  delta_current = (source_current_measured - sink_current_measured )
  delta_crrent_code = (isns_current_source_code + isns_current_sink_code)
  delta = delta_crrent_code / delta_current
  correction_gain_coefficient = ( delta *LSB  -1 )
  isns_gain_calculated_and_complimented = -int((correction_gain_coefficient/Scale_Down) * Scale_Factor) 
  # Change the sign of the gain code 
  isns_gain_code = 0x4000+isns_gain_calculated_and_complimented if  isns_gain_calculated_and_complimented < 0 else isns_gain_calculated_and_complimented # gain complimented digital code conversion 
  print(f'{Testname} Gain Code  : {hex(isns_gain_code)} ')
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE("0x38", field_info={'fieldname': 'otp_isense_gain', 'length': 14, 'registers': [{'REG': '0xBB', 'POS': 0, 'RegisterName': 'OTP FIELDS 11', 'RegisterLength': 8, 'Name': 'otp_isense_gain[13:8]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 13, 'FieldLSB': 8, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xBC', 'POS': 0, 'RegisterName': 'OTP FIELDS 12- TRACEABILITY 0', 'RegisterLength': 8, 'Name': 'otp_isense_gain[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=isns_gain_code )

  # set chip in normal 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_data_dwa', 'length': 9, 'registers': [{'REG': '0x11', 'POS': 0, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_data_dwa[8]', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 8, 'FieldLSB': 8, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0x12', 'POS': 0, 'RegisterName': 'DAC test 2', 'RegisterLength': 8, 'Name': 'tst_data_dwa[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tst_dac', 'length': 1, 'registers': [{'REG': '0x11', 'POS': 7, 'RegisterName': 'DAC test 1', 'RegisterLength': 8, 'Name': 'tst_dac', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'N000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)  # Turn off DAC
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_ocp_en_force', 'length': 1, 'registers': [{'REG': '0x1A', 'POS': 0, 'RegisterName': 'Force registers 3', 'RegisterLength': 8, 'Name': 'cld_ocp_en_force', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0) # disable ocp force 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'spk_en', 'length': 1, 'registers': [{'REG': '0x9F', 'POS': 0, 'RegisterName': 'Enables settings 5', 'RegisterLength': 8, 'Name': 'spk_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000S', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0) # disable speaker 
  vi_sns_turn_off()
if __name__ == '__main__':
  vis_gain_isns()