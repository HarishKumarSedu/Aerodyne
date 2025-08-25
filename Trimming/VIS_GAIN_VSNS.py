from dfttools import *


'''
The procedure is described hereafter:
1. Force class-D output to have SPKRP high and SPKRN low.
2. Read V-sense output digital code.
3. Force class-D output to have SPKRP low and SPKRN high.
4. Read V-sense output digital code.
5. GV=DELTA_V(=2*VDDP)/DELTA_code.

'''
from time import sleep
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback
from Procedures.VI_SNS_turn_on import vi_sns_turn_on
from Procedures.VI_SNS_turn_off import vi_sns_turn_off

def vis_gain_vsns():
  Testname = 'VIS_GAIN_VSNS'
  print(f' {Testname}')
  # import general procedures and & classd_out_pos
  startup()
  global_enable()
  playback()
  I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  I2C_WRITE("0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0) # bridge HiZ
  I2C_WRITE("0x38", field_info={'fieldname': 'cld_drv_force', 'length': 1, 'registers': [{'REG': '0x9B', 'POS': 4, 'RegisterName': 'CLD analog setting reg 5', 'RegisterLength': 8, 'Name': 'cld_drv_force', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '0x81', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)
  vi_sns_turn_on()
  pvdd_value = VFORCE ("PVDD","GND",3.7,3.7)
  sleep(0.1)
  VFORCE("OUTP","OUTN",2.5,0)
  sleep(1)
  vsns_gain_high_measured = I2C_READ("0x38", field_info={'fieldname': 'v_sense', 'length': 16, 'registers': [{'REG': '0x69', 'POS': 0, 'RegisterName': 'V SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'v_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6A', 'POS': 0, 'RegisterName': 'V SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'v_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x7F)
  vsns_gain_high_measured =  0x10000 - vsns_gain_high_measured if vsns_gain_high_measured > 0x1000 else vsns_gain_high_measured
  print(f'vsns_gain_high_measured : {hex(vsns_gain_high_measured)}')
  VFORCE ("OUTP","OUTN",-2.5,0)
  sleep(1)
  vsns_gain_low_measured = I2C_READ("0x38", field_info={'fieldname': 'v_sense', 'length': 16, 'registers': [{'REG': '0x69', 'POS': 0, 'RegisterName': 'V SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'v_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6A', 'POS': 0, 'RegisterName': 'V SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'v_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x7E)
  vsns_gain_low_measured = 0x10000 - vsns_gain_low_measured   if vsns_gain_low_measured > 0x1000 else vsns_gain_low_measured
  print(f'vsns_gain_low_measured : {hex(vsns_gain_low_measured)}')
  
  vi_sns_turn_off()
  
  '''
    1. (vsns_gain_high_measured + vsns_gain_low_measured)/5 => delta (code) / delta (outp,outn) {@outp,outn =>2.5V}
      a. vsns_gain_high_measured,vsns_gain_low_measured are twos complemented if the the code is negative 
      
    2. LSB = (5.5/2**15) {@ 16bit signed vsens value so the total steps => 2**15@referece 5.5V}
    3. delta (code) / delta (outp,outn) x LSB -1 => Residual of the gain 
    4. Residual of the gain * Scale Factor {Sclae Factor = 5/5.5}
    6. Scale down the value with => Residual of the gain * Scale Factor / (64/2**20) {@ 20bits}
    7. Change the sign of the residual gain value for the 16bit otp_gain value => vsns_gain_calculated if  vsns_gain_calculated & 0x2000 else 0x4000 -  vsns_gain_calculated
  '''
  LSB = (5.5/2**15)
  Scale_Factor = (5/5.5)
  Scale_Down = (64/2**20)
  vsns_gain_calculated = int((((vsns_gain_high_measured + vsns_gain_low_measured)/5 *LSB  -1 )*Scale_Factor) /Scale_Down) #assuming VDDP=3.7V, otherwise value has to be updated 
  # vsns_gain_calculated = 0x3e67  #assuming VDDP=3.7V, otherwise value has to be updated 
  vsns_gain_calculated = vsns_gain_calculated if  vsns_gain_calculated & 0x2000 else 0x4000 -  vsns_gain_calculated
  print(f'{Testname} value : {hex(vsns_gain_calculated)} ')
  I2C_WRITE("0x38", field_info={'fieldname': 'otp_vsense_gain', 'length': 14, 'registers': [{'REG': '0xB9', 'POS': 0, 'RegisterName': 'OTP FIELDS 9', 'RegisterLength': 8, 'Name': 'otp_vsense_gain[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xCC', 'POS': 0, 'RegisterName': 'OTP FIELDS 28', 'RegisterLength': 8, 'Name': 'otp_vsense_gain[13:8]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 13, 'FieldLSB': 8, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(vsns_gain_calculated) )
  I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  I2C_WRITE("0x38", field_info={'fieldname': 'cld_drv_force', 'length': 1, 'registers': [{'REG': '0x9B', 'POS': 4, 'RegisterName': 'CLD analog setting reg 5', 'RegisterLength': 8, 'Name': 'cld_drv_force', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '0x81', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  VFORCE("OUTP","OUTN",float('Inf'),0)

if __name__ == '__main__':
  vis_gain_vsns()