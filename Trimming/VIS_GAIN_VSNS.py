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
  I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
  I2C_WRITE("0x38", field_info={'fieldname': 'cld_vmid_buf_en_m', 'length': 1, 'registers': [{'REG': '0x1B', 'POS': 6, 'RegisterName': 'Force registers 4', 'RegisterLength': 8, 'Name': 'cld_vmid_buf_en_m', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
  I2C_WRITE("0x38", field_info={'fieldname': 'cld_vmid_buf_en_force', 'length': 1, 'registers': [{'REG': '0x1A', 'POS': 6, 'RegisterName': 'Force registers 3', 'RegisterLength': 8, 'Name': 'cld_vmid_buf_en_force', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
  I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)
  I2C_WRITE("0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x5A) # tun on P_ouup, MID_outp, N_outn, CAS_outn
  vi_sns_turn_on()
  pvdd_value = VFORCE ("PVDD","GND",2.5,2.5)
  sleep(0.001)
  vsns_gain_high_measured = I2C_READ("0x38", field_info={'fieldname': 'v_sense', 'length': 16, 'registers': [{'REG': '0x69', 'POS': 0, 'RegisterName': 'V SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'v_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6A', 'POS': 0, 'RegisterName': 'V SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'v_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x7F)
  sleep(0.001)
  I2C_WRITE("0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0) # bridge HiZ
  sleep(0.001)
  I2C_WRITE("0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0xA5) # tun on P_ouup, MID_outp, N_outn, CAS_outn
  sleep(0.001)
  vsns_gain_low_measured = I2C_READ("0x38", field_info={'fieldname': 'v_sense', 'length': 16, 'registers': [{'REG': '0x69', 'POS': 0, 'RegisterName': 'V SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'v_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6A', 'POS': 0, 'RegisterName': 'V SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'v_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0xFE)
  
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x00)  # set bridge switch (LSp off, MIDp off, CASp off, HSp off, LSn off, MIDn off, CASn off, HSn off)
  sleep(0.001)
  vi_sns_turn_off()
  
  # VDDP_3P7 = VMEASURE(signal="PVDD", reference="GND", expected_value=3.7,error_spread=0)
  vsns_gain_calculated = 2*pvdd_value/(int(vsns_gain_high_measured)-int(vsns_gain_low_measured)) #assuming VDDP=3.7V, otherwise value has to be updated 
  print(f'{Testname} value : {vsns_gain_calculated} ')
  I2C_WRITE("0x38", field_info={'fieldname': 'otp_vsense_gain', 'length': 14, 'registers': [{'REG': '0xB9', 'POS': 0, 'RegisterName': 'OTP FIELDS 9', 'RegisterLength': 8, 'Name': 'otp_vsense_gain[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xCC', 'POS': 0, 'RegisterName': 'OTP FIELDS 28', 'RegisterLength': 8, 'Name': 'otp_vsense_gain[13:8]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 13, 'FieldLSB': 8, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(round(vsns_gain_calculated)) )
  VFORCE ("PVDD","GND",3.7,3.7)
if __name__ == '__main__':
  vis_gain_vsns()