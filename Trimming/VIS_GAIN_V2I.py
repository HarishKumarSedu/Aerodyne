from dfttools import *
Testname = 'VIS_GAIN_V2I'
print(f' {Testname}')

'''
Due to technological mismatch of input and DAC resistors, when a voltage at the input is applied, a current is flowing to those resistors. This effect produces a current modifying the signal current that must be measured. To compensate for this effect, the procedure is the following:
1. Remove output load from class-D output
2. Force class-D output to have SPKRP high and SPKRN low.
3. Read I-sense output digital code.
4. Force class-D output to have SPKRP low and SPKRN high.
5. Read I-sense output digital code
GVI = DELTA_V=(2*VDDP)/DELTA_code

'''
from time import sleep
print(f' ........ Remove load from classD ........')
from Procedures import Startup
from Procedures import Global_enable
from Procedures import VI_SNS_turn_on
from Procedures import CLASSD_OUT_POS
sleep(0.001)
isns_gain_low_measured = I2C_READ("0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x01)
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x66)  # set bridge switch (LSp off, MIDp off, CASp off, HSp off, LSn off, MIDn off, CASn off, HSn off)
from Procedures import CLASSD_OUT_NEG
sleep(0.001)
isns_gain_high_measured = I2C_READ("0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0xFE)
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x66)  # set bridge switch (LSp off, MIDp off, CASp off, HSp off, LSn off, MIDn off, CASn off, HSn off)
VDDP_3P7 = VMEASURE(signal="PVDD", reference="GND", expected_value=3.7,error_spread=0) # VDDP reading
v2i_gain_calculated = VDDP_3P7/(int(isns_gain_high_measured)-int(isns_gain_low_measured)) #assuming VDDP=3.7V, otherwise value has to be updated
print(f'{Testname} value : {v2i_gain_calculated} ')
I2C_WRITE("0x38", field_info={'fieldname': 'otp_isense_from_vsense_gain', 'length': 12, 'registers': [{'REG': '0xBF', 'POS': 0, 'RegisterName': 'OTP FIELDS 15 - TRACEABILITY 3', 'RegisterLength': 8, 'Name': 'otp_isense_from_vsense_gain[11:8]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 11, 'FieldLSB': 8, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xC0', 'POS': 0, 'RegisterName': 'OTP FIELDS 16 - TRACEABILITY 4', 'RegisterLength': 8, 'Name': 'otp_isense_from_vsense_gain[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(round(v2i_gain_calculated)) )
I2C_WRITE("0x38", field_info={'fieldname': 'otp_isense_gain', 'length': 14, 'registers': [{'REG': '0xBB', 'POS': 0, 'RegisterName': 'OTP FIELDS 11', 'RegisterLength': 8, 'Name': 'otp_isense_gain[13:8]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 13, 'FieldLSB': 8, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xBC', 'POS': 0, 'RegisterName': 'OTP FIELDS 12- TRACEABILITY 0', 'RegisterLength': 8, 'Name': 'otp_isense_gain[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(round(v2i_gain_calculated)) )
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x66)  # set bridge switch (LSp off, MIDp off, CASp off, HSp off, LSn off, MIDn off, CASn off, HSn off)