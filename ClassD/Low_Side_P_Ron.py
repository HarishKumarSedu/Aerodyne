from dfttools import *
from time import sleep
import random

Test_Name = 'Low_Side_P_Ron'
from Procedures import Startup

print(f'............ {Test_Name} ........')

'''
Low-Side P-Channel Ron Measurement
-------------------------------------------------
1. Enable bridge p-cascode, mid, and ls devices
2. Force 500mA current into "OUTP" pin
3. Measure differential voltage between "VMID" and PGND_sns
4. Calculate Ron = dV / 500mA
'''

# Define device address (replace with actual address)
# "0x68" = 0xXX  # Example device address, update accordingly

'''
! Important designers must correct the fields and write the procedure
# Step 1: Enable bridge p-cascode, mid, and ls devices
'''
# I2C_WRITE(device_address="0x68", field_info=bridge_p_cascode_en, write_value=1)
# I2C_WRITE(device_address="0x68", field_info=bridge_p_mid_en, write_value=1)
# I2C_WRITE(device_address="0x68", field_info=bridge_p_ls_en, write_value=1)

'''
# Step 2: Configure analog test mux for differential measurement
# Route "VMID" and PGND_sns to measurement channels through test mux
'''
# I2C_WRITE(device_address="0x68", field_info=analog_test_mux_sel1, write_value=0xXX)  # "VMID"
# I2C_WRITE(device_address="0x68", field_info=analog_test_mux_sel2, write_value=0xYY)  # PGND_sns

# Wait for device stabilization
sleep(0.0001)  # 100 µs

# Step 3: Force 500mA current into "OUTP" pin
AFORCE(signal="OUTP", reference="GND", value=500e-3, error_spread=0.05)  # 500mA ±5%

# Wait for current settling
sleep(0.001)  # 1 ms

# Step 4: Measure differential voltage and calculate Ron
dV = VMEASURE(signal="VMID", reference="PGND", expected_value=0.1, error_spread=0.05)  # Expected ~100mV for 200mOhms
LSp_ron = dV / 500e-3  # R = V/I

print(f'Calculated Low-Side P-Ron: {LSp_ron:.3f} Ohms')  # "Ohms" 
print(f'[Expected ~200m Ohms typical, based on dV={dV:.3f}V @ 500mA]')
