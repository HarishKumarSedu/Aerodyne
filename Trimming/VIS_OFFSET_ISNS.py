from dfttools import *
Testname = 'VIS_OFFSET_ISNS'
print(f' {Testname}')

'''
Class D output staged are programmed to have both SPKRP and SPKRN at VCM. In this way, no current signal is applied (across R-sense) at the input of I-sense channel.
Then output code (I-sns code) it is stored.

'''
from time import sleep
from Procedures import Startup
from Procedures import Global_enable
from Procedures import CLASSD_OUT_VMID
from Procedures import VI_SNS_turn_on
sleep(0.1)
isns_offset_measured = I2C_READ("0x68", field_info={'fieldname': 'i_sense', 'length': 16, 'registers': [{'REG': '0x6B', 'POS': 0, 'RegisterName': 'I SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'i_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6C', 'POS': 0, 'RegisterName': 'I SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'i_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x00)
print(f'{Testname} value : {isns_offset_measured} ')
I2C_WRITE("0x68", field_info={'fieldname': 'otp_isense_offset', 'length': 6, 'registers': [{'REG': '0xBA', 'POS': 0, 'RegisterName': 'OTP FIELDS 10', 'RegisterLength': 8, 'Name': 'otp_isense_offset[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(round(isns_offset_measured)))