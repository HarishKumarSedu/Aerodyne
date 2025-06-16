Test_Name = 'Startup'
print(f'............ {Test_Name} ........')
from dfttools import *

VFORCE(signal="VDD",reference="GND",value=1.8)
VFORCE(signal="RESETB",reference="GND",value=1.8)
VFORCE(signal="PVDD",reference="GND",value=3.7)







