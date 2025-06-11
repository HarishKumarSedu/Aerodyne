from dfttools import *
Testname = 'VIS_OFFSET_ISNS'
print(f' {Testname}')

'''
Class D output staged are programmed to have both SPKRP and SPKRN at VCM. In this way, no current signal is applied (across R-sense) at the input of I-sense channel.
Then output code (I-sns code) it is stored.

'''

from Procedures import Startup
# Import classD turn on procedure
# Import classD procedure in which SPKRP and SPKRM are placed at VCM
from Procedures import VI_SNS_turn_on
# isns_offset_measured = I2C_READ("0x68", fieldname, expectedvalue)
# I2C_WRITE("0x68", OTP_fieldname, vsns_offset_measured)