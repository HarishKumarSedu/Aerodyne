from dfttools import *
from time import sleep
import random

Test_Name = 'DAC_Common_Mode_Voltage'
from Procedures import Startup

print(f'............ {Test_Name} ........')

'''
DAC Common Mode Voltage Test
-------------------------------------------------
1. Configure the device to enable DAC common mode voltage output.
2. Bring the DAC common mode voltage to pin "IODATA1" through the analog test mux.
3. Measure the voltage at "IODATA1".
'''

# Define device address (replace with actual address)
# "0x68" = 0xXX  # Example device address, update accordingly

'''
! Important designers must correct the fields and write the procedure
# Step 1: Configure registers to enable DAC common mode voltage output
# Example register writes - replace field_info and values with actual DAC control registers
'''
# I2C_WRITE(device_address="0x68", field_info=dac_cm_enable, write_value=1)
# I2C_WRITE(device_address="0x68", field_info=dac_cm_voltage_select, write_value=1)  # Enable CM voltage mode

'''
# Step 2: Bring DAC common mode voltage to "IODATA1" through analog test mux
# Assuming 'analog_test_mux_sel' controls the analog test mux output pin selection "IODATA1"
'''
# I2C_WRITE(device_address="0x68", field_info=analog_test_mux_sel, write_value=0xXX)

# Wait a short time for signals to stabilize
sleep(0.0001)  # 100 us

# Step 3: Measure the voltage at "IODATA1"
expected_value = 1.25  # Expected voltage value from simulation/design (1.25V)
error_spread = expected_value * 0.05  # 5% error spread
measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=expected_value, error_spread=error_spread)

print(f'Measured DAC common mode voltage at "IODATA1" wrt "GND": {measured_value:.3f} V')
