from dfttools import *
from time import sleep 
from math import *
import random
from time import sleep
Test_Name = 'DC_VDDP_PSRR'
from Procedures import Startup
from Procedures import Playback

print(f'............ {Test_Name} ........')

'''
DC_VDDP_PSRR test
Step 1. Configure the device registers to enable testing.
Step 2. Measure the classD DC output voltage at "PVDD"=2.5V 
Step 3. Measure the classD DC output voltage at "PVDD"=5V 
Step 4. Calculate the DC PSRR as 20*log10((|VOUT_5V - VOUT_2p5V|)/2.5)

'''
# Step 1
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1) 
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'force_dac_zero', 'length': 1, 'registers': [{'REG': '0x1E', 'POS': 1, 'RegisterName': 'Force registers 7', 'RegisterLength': 8, 'Name': 'force_dac_zero', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '000NNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1) 
error_percentage = 1e-4 # 1% use it only for the simulation purpose & same applicable to the expected value 
# Step 2
sleep(0.0001) 
#Set  VDDP=5V
VFORCE(signal="PVDD", reference="GND", value=5) # force 5v between "PVDD" wrt "GND"
Vout_V1 = VMEASURE(signal="OUTP", reference="OUTN", expected_value = 0, error_spread = error_percentage) 
VFORCE(signal="PVDD", reference="GND", value=2.5)  # force 2.5v between "PVDD" wrt "GND"
sleep(0.0001) 
#set VDDP=2.5V
Vout_V2 = VMEASURE(signal="OUTP", reference="OUTN",expected_value = 0, error_spread = error_percentage)
# print(f'Vout_V1 {Vout_V1} Vout_V2 : {Vout_V2} , {20*log10(abs(Vout_V1-Vout_V2) / 2.5)}')
measured_value_db=20*log10(abs(Vout_V1-Vout_V2)/2.5)
#expected value is -90dB
print(f'{Test_Name} ..... Measured :>  {measured_value_db} dB')
