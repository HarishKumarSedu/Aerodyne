from dfttools import *
Testname = 'VIS_GAIN_VSNS'
print(f' {Testname}')

'''
The procedure is described hereafter:
1. Force class-D output to have SPKRP high and SPKRN low.
2. Read V-sense output digital code.
3. Force class-D output to have SPKRP low and SPKRN high.
4. Read V-sense output digital code.
5. GV=DELTA_V(=2*VDDP)/DELTA_code.

'''
from time import sleep
from Procedures import Startup
from Procedures import Global_enable
from Procedures import VI_SNS_turn_on
from Procedures import CLASSD_OUT_POS
sleep(0.001)
vsns_gain_low_measured = I2C_READ("0x68", field_info={'fieldname': 'v_sense', 'length': 16, 'registers': [{'REG': '0x69', 'POS': 0, 'RegisterName': 'V SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'v_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6A', 'POS': 0, 'RegisterName': 'V SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'v_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x01)
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x66)  # set bridge switch (LSp off, MIDp off, CASp off, HSp off, LSn off, MIDn off, CASn off, HSn off)
sleep(0.001)
from Procedures import CLASSD_OUT_NEG
sleep(0.001)
vsns_gain_high_measured = I2C_READ("0x68", field_info={'fieldname': 'v_sense', 'length': 16, 'registers': [{'REG': '0x69', 'POS': 0, 'RegisterName': 'V SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'v_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6A', 'POS': 0, 'RegisterName': 'V SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'v_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0xFE)
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x66)  # set bridge switch (LSp off, MIDp off, CASp off, HSp off, LSn off, MIDn off, CASn off, HSn off)
sleep(0.001)
VDDP_3P7 = VMEASURE(signal="PVDD", reference="GND", expected_value=3.7,error_spread=0)
vsns_gain_calculated = 2*VDDP_3P7/(int(vsns_gain_high_measured)-int(vsns_gain_low_measured)) #assuming VDDP=3.7V, otherwise value has to be updated 
print(f'{Testname} value : {vsns_gain_calculated} ')
I2C_WRITE("0x68", field_info={'fieldname': 'otp_vsense_gain', 'length': 14, 'registers': [{'REG': '0xB9', 'POS': 0, 'RegisterName': 'OTP FIELDS 9', 'RegisterLength': 8, 'Name': 'otp_vsense_gain[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xCC', 'POS': 0, 'RegisterName': 'OTP FIELDS 28', 'RegisterLength': 8, 'Name': 'otp_vsense_gain[13:8]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 13, 'FieldLSB': 8, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(round(vsns_gain_calculated)) )