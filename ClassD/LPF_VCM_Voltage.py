from dfttools import *
from time import sleep
import random

Test_Name = 'LPF_VCM_Voltage'
from Procedures import Startup

print(f'............ {Test_Name} ........')

'''
LPF Common Mode Voltage Test
-------------------------------------------------
1. Configure the device to enable LPF common mode voltage output
2. Bring the LPF VCM voltage to pin "IODATA1" through the analog test mux
3. Measure the voltage at "IODATA1"
'''

# Define device address (replace with actual address)
# "0x68" = 0xXX  # Example device address, update accordingly

'''
! Important designers must correct the fields and write the procedure
# Step 1: Configure registers to enable LPF common mode voltage
# Example register writes - replace field_info and values with actual LPF control registers
'''
# I2C_WRITE(device_address="0x68", field_info=lpf_vcm_enable, write_value=1)
# I2C_WRITE(device_address="0x68", field_info=lpf_vcm_voltage_select, write_value=1)

'''
# Step 2: Route LPF VCM voltage to "IODATA1" through analog test mux
# Assuming 'analog_test_mux_sel' controls the analog test mux output
'''
# I2C_WRITE(device_address="0x68", field_info=analog_test_mux_sel, write_value=0xXX)  # LPF_VCM selection code

# Wait for signal stabilization
sleep(0.0001)  # 100 µs

# Step 3: Measure VCM voltage
expected_value = 1.5  # Expected common mode voltage (1.5V)
error_spread = expected_value * 0.05  # 5% error margin
measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=expected_value, error_spread=error_spread)

print(f'Expected VCM voltage: {expected_value:.2f} V | Measured: {measured_value:.3f} V')
