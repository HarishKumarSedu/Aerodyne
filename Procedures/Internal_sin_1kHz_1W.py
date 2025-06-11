# set the internal sinusoildal generator at 1kHz 1W
Test_Name = 'Internal_sin_1kHz_1W'
print(f'............ {Test_Name} ........')
from dfttools import *

# use following code if you want to foce the clock
# signal is the pin at you want to apply clock with repsct to reference
# FREQFORCE(signal=,reference=,value=)