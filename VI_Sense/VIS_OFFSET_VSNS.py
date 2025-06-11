from dfttools import *
Testname = 'VIS_OFFSET_VSNS'
print(f' {Testname}')

'''
Class D output staged are programmed to have both SPKRP and SPKRN at VCM.
In this way, no voltage signal is applied at the input of V-sense channel.
Then output code (V-sns code) is stored.

'''

from Procedures import Startup
# Import classD turn on procedure
# Import classD procedure in which SPKRP and SPKRM are placed at VCM
from Procedures import VI_SNS_turn_on
# vsns_offset_measured = I2C_READ("0x68", fieldname, expectedvalue)
# I2C_WRITE("0x68", OTP_fieldname, vsns_offset_measured)