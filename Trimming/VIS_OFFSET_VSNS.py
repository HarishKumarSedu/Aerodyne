from dfttools import *
Testname = 'VIS_OFFSET_VSNS'
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
vsns_offset_measured = I2C_READ("0x38", field_info={'fieldname': 'v_sense', 'length': 16, 'registers': [{'REG': '0x69', 'POS': 0, 'RegisterName': 'V SENSE readback reg 1', 'RegisterLength': 8, 'Name': 'v_sense[15:8]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 15, 'FieldLSB': 8, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x6A', 'POS': 0, 'RegisterName': 'V SENSE readback reg 2', 'RegisterLength': 8, 'Name': 'v_sense[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]}, expected_value=0x00)
print(f'{Testname} value : {vsns_offset_measured} ')
I2C_WRITE("0x38", field_info={'fieldname': 'otp_vsense_offset', 'length': 6, 'registers': [{'REG': '0xB8', 'POS': 0, 'RegisterName': 'OTP FIELDS 8', 'RegisterLength': 8, 'Name': 'otp_vsense_offset[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(round(vsns_offset_measured)))