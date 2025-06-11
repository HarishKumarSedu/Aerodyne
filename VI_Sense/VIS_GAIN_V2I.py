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

print(f' ........ Remove load from classD ........')
from Procedures import Startup
# Import classD turn on procedure
from Procedures import VI_SNS_turn_on
# Import classD procedure in which SPKRP and SPKRM are LOW
# isns_gain_low_measured = I2C_READ("0x68", fieldname, expectedvalue)
# Import classD procedure in which SPKRP and SPKRM are HIGH
# isns_gain_high_measured = I2C_READ("0x68", fieldname, expectedvalue)
# vsns_gain_calculated = VDDP/(isns_gain_high_measured-isns_gain_low_measured)
# print(f'{Testname} value : {vsns_gain_calculated} ')
# I2C_WRITE("0x68", opt_fieldname, int(vsns_gain_calculated) )