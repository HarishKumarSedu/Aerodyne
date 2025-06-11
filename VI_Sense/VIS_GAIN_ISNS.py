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


from Procedures import Startup
# Import classD turn on procedure
from Procedures import VI_SNS_turn_on
print(f' ........ Source 100mA from SPKRP/SPKRM ........ ')
source_current = 100e-3
AFORCE(signal="OUTP",reference="GND",value=source_current, error_spread=source_current*0.01) # 5% error 
# isns_gain_source_measured = I2C_READ("0x68", fieldname, expectedvalue)
print(f' ........ Sink 100mA to SPKRP/SPKRM ........ ')
AFORCE(signal="OUTP",reference="GND",value=-source_current, error_spread=-source_current*0.01) # 5% error 
# isns_gain_sink_measured = I2C_READ("0x68", fieldname, expectedvalue)
# isns_gain_calculated = 200m/(isns_gain_source_measured-isns_gain_sink_measured)
# print(f'{Testname} value : {isns_gain_calculated} ')
# I2C_WRITE("0x68", opt_fieldname, int(isns_gain_calculated) )

