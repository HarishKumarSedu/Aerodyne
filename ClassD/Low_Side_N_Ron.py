from dfttools import *
from time import sleep
import random

Test_Name = 'Low_Side_N_Ron'
from Procedures import Startup

print(f'............ {Test_Name} ........')

'''
Low-Side N-Channel Ron Measurement
-------------------------------------------------
1. Enable bridge n-cascode, mid, and ls devices
2. Force 500mA current into "OUTP" pin
3. Measure differential voltage between "VMID" and PGND_sns
4. Calculate Ron = dV / 500mA
'''

# Define device address (replace with actual address)
# "0x68" = 0xXX  # Example device address, update accordingly

'''
! Important designers must correct the fields and write the procedure
# Step 1: Enable bridge n-cascode, mid, and ls devices
'''
# I2C_WRITE(device_address="0x68", field_info=bridge_n_cascode_en, write_value=1)
# I2C_WRITE(device_address="0x68", field_info=bridge_n_mid_en, write_value=1)
# I2C_WRITE(device_address="0x68", field_info=bridge_n_ls_en, write_value=1)

'''
# Step 2: Configure analog test mux for differential measurement
# Route "VMID" and PGND_sns to measurement channels through test mux
'''
# I2C_WRITE(device_address="0x68", field_info=analog_test_mux_sel1, write_value=0xXX)  # "VMID"
# I2C_WRITE(device_address="0x68", field_info=analog_test_mux_sel2, write_value=0xYY)  # PGND_sns

# Wait for device stabilization (critical for N-channel measurements[^8^])
sleep(0.0001)  # 100 µs

# Step 3: Force 500mA current into "OUTP" pin
I_forced = 500e-3  # 500mA
AFORCE(signal="OUTP", reference="GND", value=I_forced, error_spread=0.05)  # Current forcing

# Wait for current settling (consider thermal effects[^6^])
sleep(0.001)  # 1 ms

# Step 4: Measure differential voltage and calculate Ron
dV = VMEASURE(signal="VMID", reference="PGND", expected_value=0.1, error_spread=0.05)
LSN_ron = dV / I_forced  # R = V/I

print(f'Calculated Low-Side N-Ron: {LSN_ron:.3f} Ohms')
print(f'[Expected ~XXXm Ohms typical, based on dV={dV:.3f}V @ {I_forced*1000:.0f}mA]')
