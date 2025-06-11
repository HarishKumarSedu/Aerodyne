from dfttools import *
from time import sleep
import random

Test_Name = 'DAC_Current'
from Procedures import Startup

print(f'............ {Test_Name} ........')

'''
DAC Current Test
-------------------------------------------------
1. Configure the device to enable DAC test current output.
2. Bring the DAC test current to pin "IODATA1" through the analog test mux.
3. Measure the current at "IODATA1".
'''

# Define device address (replace with actual address)
# "0x68" = 0xXX  # Example device address, update accordingly

'''
! Important designers must correct the fields and write the procedure
# Step 1: Configure registers to enable DAC test current output
# Example register writes - replace field_info and values with actual DAC control registers
'''
# I2C_WRITE(device_address="0x68", field_info=dac_test_enable, write_value=1)
# I2C_WRITE(device_address="0x68", field_info=dac_test_current_select, write_value=1)  # Enable DAC current test mode

'''
# Step 2: Bring DAC test current to "IODATA1" through analog test mux
# Assuming 'analog_test_mux_sel' controls the analog test mux output pin selection "IODATA1"
'''
# I2C_WRITE(device_address="0x68", field_info=analog_test_mux_sel, write_value=0xXX)

# Wait a short time for signals to stabilize
sleep(0.0001)  # 100 us

# Step 3: Measure the current at "IODATA1"
expected_value = 590e-9  # Expected current value from simulation/design 590nA
error_spread = expected_value*0.05 # 5% error spread taken for the simulation purpose designers must correct it 
measured_value = AMEASURE(signal="IODATA1", reference="GND", expected_value=expected_value, error_spread=error_spread)

print(f'Measured DAC current value at "IODATA1" wrt "GND": {measured_value}')
