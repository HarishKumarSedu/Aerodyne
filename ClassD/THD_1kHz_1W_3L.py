from dfttools import *
from time import sleep 
import random
Test_Name = 'THD_1kHz_1W_3L'
from Procedures import Playback
from Procedures import Internal_sin_1kHz_1W

print(f'............ {Test_Name} ........')

'''
1.Reach the playback state with 3L modulation
2.Enable internal sinusoid generator to play 1W at 1 kHz.
3.Wait 1ms.
4.Perform THD measurement on the differential voltage signal measured as  voltage @"OUTP" pin - voltage #"OUTN" pin.
5.Expected value is -80dB.
6.Maximum value is -77dB.
'''
maximum_thd = -77
error_percentage = 0.075 # 7.5%
expeted_thd = -80
expected_vals = {'THD': expeted_thd}
error_spreads = {'THD': expeted_thd*error_percentage}

measured_Values = FFT(signal="IODATA1",reference="GND",signal_type='Digital',sample_number=9202,sample_time=0.003,window='Hanning',expected_values=expected_vals,error_spreads=error_spreads)
measured_THD = measured_Values.get('THD') 

if measured_THD < maximum_thd:
  print(f'...... {Test_Name}..Passed THD:{measured_THD}dB ')
else:
  print(f'...... {Test_Name}..Failed THD:{measured_THD}dB ')
  