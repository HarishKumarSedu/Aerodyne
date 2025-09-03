from dfttools import *
from time import sleep
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback
from Procedures.VI_SNS_turn_on import vi_sns_turn_on

def vis_gain_isns():
  Testname = 'VIS_GAIN_ISNS'
  print(f' {Testname}')

  '''
  The procedure is described hereafter:
  1. Force class-D output to have both SPKRP and SPKRN at VCM.
  2. Source a stated current (i.e. 100mA).
  3. Read I-sense output digital code.
  4. Sink a note current (i.e. -100mA).
  5. Read I-sense output digital code.
  6. GI=DELTA_I=(200mA)/DELTA_code.

  '''
  startup()
  global_enable()
  playback()
  vi_sns_turn_on()

  
  source_current = 500e-3
  sleep(0.1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x66)  # select all switch off
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_drv_force', 'length': 1, 'registers': [{'REG': '0x9B', 'POS': 4, 'RegisterName': 'CLD analog setting reg 5', 'RegisterLength': 8, 'Name': 'cld_drv_force', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '0x81', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)  # force the switch in the selected position above
  # Force 0A between "OUTP" and "OUTN" measure the Isense offset 
  AFORCE(signal="OUTP",reference="OUTN",value=0.0, error_spread=0) # 1% error
  isns_offset = I2C_READ("0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x0)
  isns_offset = (0x10000 - isns_offset) if isns_offset & 0x8000 else isns_offset
  print(f' ........ 0A Current from SPKRP/SPKRM : {hex(isns_offset)} ........ ')
  surce_current_measured = AFORCE(signal="OUTP",reference="OUTN",value=source_current, error_spread=source_current*0.01) # 1% error
  sleep(0.1)
  isns_current_source_measured = I2C_READ("0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0xFE)
  # complement the 16bit isense value 
  isns_current_source_measured = (0x10000 - isns_current_source_measured) if isns_current_source_measured & 0x8000 else isns_current_source_measured
  print(f' ........ Source 500mA from SPKRP/SPKRM ........ Code {hex(isns_current_source_measured)} ')
  surce_sink_measured = AFORCE(signal="OUTP",reference="OUTN",value=-source_current, error_spread=source_current*0.01) # 1% error
  sleep(0.1)
  isns_current_sink_measured = I2C_READ("0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x01)
  isns_current_sink_measured = (0x10000 - isns_current_sink_measured) if isns_current_sink_measured & 0x8000 else isns_current_sink_measured
  print(f' ........ Sink 500mA to SPKRP/SPKRM ........ Code {hex(isns_current_sink_measured)} ')
  ######## Isense Gain Calculations #####################
  LSB = (20/2**15) # lsb of the 16 bit isense value 
  Scale_Factor = (3/20) # full adapter 
  Scale_Down = (64/2**20) # weight of the isense
  isns_gain_calculated = int((((isns_current_source_measured + isns_current_sink_measured)/(surce_current_measured - surce_sink_measured ) *LSB  -1 )*Scale_Factor) /Scale_Down) & 0xFFF # convert it to 12bit 
  # Change the sign of the gain code 
  isns_gain_calculated = 0x4000+isns_gain_calculated if  isns_gain_calculated & 0x2000 else 0x4000 -  isns_gain_calculated
  print(f'{Testname} value : {isns_gain_calculated} ')
  I2C_WRITE("0x38", field_info={'fieldname': 'otp_isense_gain', 'length': 14, 'registers': [{'REG': '0xBB', 'POS': 0, 'RegisterName': 'OTP FIELDS 11', 'RegisterLength': 8, 'Name': 'otp_isense_gain[13:8]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 13, 'FieldLSB': 8, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xBC', 'POS': 0, 'RegisterName': 'OTP FIELDS 12- TRACEABILITY 0', 'RegisterLength': 8, 'Name': 'otp_isense_gain[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(round(isns_gain_calculated)) )
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x66)  # set bridge switch (LSp off, MIDp off, CASp off, HSp off, LSn off, MIDn off, CASn off, HSn off)
  # disconnect the current sources applying infinity current 
if __name__ == '__main__':
  vis_gain_isns()