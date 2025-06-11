from dfttools import *
from time import sleep
import random

Test_Name = 'Mid_P_Ron'
from Procedures import Startup

print(f'............ {Test_Name} ........')

'''
Mid-Side P-Channel Ron Measurement
-------------------------------------------------
1. Enable bridge p-cascode and mid devices
2. Force current into measurement node
3. Measure differential voltage across mid device
4. Calculate Ron = dV / I_forced
'''

# Define device address (replace with actual address)
# "0x68" = 0xXX  # Example device address, update accordingly

'''
! Important designers must correct the fields and write the procedure
# Step 1: Enable bridge p-cascode and mid devices
'''
# I2C_WRITE(device_address="0x68", field_info=bridge_p_cascode_en, write_value=1)
# I2C_WRITE(device_address="0x68", field_info=bridge_p_mid_en, write_value=1)

'''
# Step 2: Configure analog test mux for differential measurement
# Route Mid-P measurement points through test mux
'''
# I2C_WRITE(device_address="0x68", field_info=analog_test_mux_sel1, write_value=0xXX)  # Mid-P node 1
# I2C_WRITE(device_address="0x68", field_info=analog_test_mux_sel2, write_value=0xYY)  # Mid-P node 2

# Wait for device stabilization
sleep(0.0001)  # 100 µs

# Step 3: Force current through Mid-P channel
I_forced = 500e-3  # 500mA
AFORCE(signal="VMID", reference="GND", value=I_forced, error_spread=0.05)  # Current forcing

# Wait for current settling
sleep(0.001)  # 1 ms

# Step 4: Measure differential voltage and calculate Ron
dV = VMEASURE(signal="VMID", reference="GND", 
              expected_value=0.1, error_spread=0.05)  # Expected ~100mV for 200mOhms
MidP_ron = dV / I_forced  # R = V/I

print(f'Calculated Mid-Side P-Ron: {MidP_ron:.3f} Ohms')
print(f'[Expected ~XXXm Ohms typical, based on dV={dV:.3f}V @ {I_forced*1000:.0f}mA]')
