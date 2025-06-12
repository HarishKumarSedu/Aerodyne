from dfttools import *
from time import sleep
import random
Test_Name = 'V-sense THD'
from Procedures import Startup
print(f'............ {Test_Name} ........')
from Procedures import Playback
from Procedures import Internal_sin_1kHz_1W
from Procedures import VI_SNS_turn_on