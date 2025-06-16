from dfttools import *
from time import sleep 
import random
Test_Name = 'noise floor_1kHz_-60dBFS_3L'
from Procedures import Playback
from Procedures import Internal_sin_noise_floor_measurement

print(f'............ {Test_Name} ........')

'''
Reach the playback state with 3L modulation

Enable internal sinusoid generator to play -60dBFS (2mVppRMS at the classD output) at 1 kHz.

Wait 1ms.

Perform A-weighted SNR measurement (AWSNR) on the differential voltage signal measured as (voltage @"OUTP" pin) - (voltage @"OUTN" pin).

Noise floor is 2mV/AWSNR.

Expected value is 6uV. 

'''