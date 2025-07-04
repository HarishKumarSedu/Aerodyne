from dfttools import *
from time import sleep 
import random
Test_Name = 'FLL_ramp_current'
from Procedures import Startup
from Procedures import Playback

print(f'............ {Test_Name} ........')

'''
FLL_ramp_current
The FLL is trimmed, "IOCLK0" has 3.072MHz clock.
Step 1. Bring out on "IODATA1" IRAMP VDDP/R-derived current of the FLL
Step 2. Measure it.
'''

# Step 1
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1) #enable "IODATA1"
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=3) #bring out the VDDD/R current
sleep(0.0001) 
expected_value = 0.0000015 #3.6/(3*1200000)*18/12->(vddp/2R)
error_spread = expected_value*0.2
measured_value=VMEASURE(signal="IODATA1", reference="GND", expected_value=expected_value, error_spread=error_spread)

print(f'FLL ramp VDDP/R-derived current is: {measured_value}')