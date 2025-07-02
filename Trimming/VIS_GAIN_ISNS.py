from dfttools import *
Testname = 'VIS_GAIN_VSNS'
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

from time import sleep
from Procedures import Startup
from Procedures import Global_enable
from Procedures import VI_SNS_turn_on
print(f' ........ Source 500mA from SPKRP/SPKRM ........ ')
source_current = 500e-3
from Procedures import CLASSD_OUT_CURR_TRIM
sleep(0.001)
AFORCE(signal="OUTP",reference="GND",value=source_current, error_spread=source_current*0.01) # 1% error
AFORCE(signal="OUTN",reference="GND",value=-source_current, error_spread=source_current*0.01) # 1% error
sleep(0.001)
isns_gain_source_measured = I2C_READ("0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0xFE)
print(f' ........ Sink 500mA to SPKRP/SPKRM ........ ')
AFORCE(signal="OUTP",reference="GND",value=-source_current, error_spread=source_current*0.01) # 1% error
AFORCE(signal="OUTN",reference="GND",value=source_current, error_spread=source_current*0.01) # 1% error
sleep(0.001)
isns_gain_sink_measured = I2C_READ("0x38", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x01)
isns_gain_calculated = 2*0.5/(int(isns_gain_source_measured)-int(isns_gain_sink_measured))
print(f'{Testname} value : {isns_gain_calculated} ')
I2C_WRITE("0x38", field_info={'fieldname': 'otp_isense_gain', 'length': 14, 'registers': [{'REG': '0xBB', 'POS': 0, 'RegisterName': 'OTP FIELDS 11', 'RegisterLength': 8, 'Name': 'otp_isense_gain[13:8]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 13, 'FieldLSB': 8, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xBC', 'POS': 0, 'RegisterName': 'OTP FIELDS 12- TRACEABILITY 0', 'RegisterLength': 8, 'Name': 'otp_isense_gain[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(round(isns_gain_calculated)) )
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x66)  # set bridge switch (LSp off, MIDp off, CASp off, HSp off, LSn off, MIDn off, CASn off, HSn off)


