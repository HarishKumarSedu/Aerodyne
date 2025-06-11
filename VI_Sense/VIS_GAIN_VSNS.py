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

from Procedures import Startup
# Import classD turn on procedure
from Procedures import VI_SNS_turn_on
# Import classD procedure in which SPKRP and SPKRM are LOW
# vsns_gain_low_measured = I2C_READ("0x68", fieldname, expectedvalue)
# Import classD procedure in which SPKRP and SPKRM are HIGH
# vsns_gain_high_measured = I2C_READ("0x68", fieldname, expectedvalue)
# vsns_gain_calculated = 2*VDDP/(vsns_gain_high_measured-vsns_gain_low_measured)
# print(f'{Testname} value : {vsns_gain_calculated} ')
# I2C_WRITE("0x68", opt_fieldname, int(vsns_gain_calculated) )