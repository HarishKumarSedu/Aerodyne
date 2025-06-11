from dfttools import *
from time import sleep 
import random
Test_Name = 'THD_1kHz_1W_3L'
from Procedures import Playback
from Procedures import Internal_sin_1kHz_1W

print(f'............ {Test_Name} ........')

'''
Reach the playback state with 3L modulation

Enable internal sinusoid generator to play 1W at 1 kHz.

Wait 1ms.

Perform THD measurement on the differential voltage signal measured as  voltage @"OUTP" pin - voltage #"OUTN" pin.

Expected value is -80dB.
Maximum value is -77dB.
'''


