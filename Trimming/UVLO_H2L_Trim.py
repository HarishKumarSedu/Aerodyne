from dfttools import *
from time import sleep
import random
from Procedures import Startup

Test_Name = 'UVLO_H2L_Trim'
print(f'............ {Test_Name} ........')

'''
Set "PVDD"=2.25V (desired L2H UVLO threshold), 
bring UVLO comparator output to pin "IODATA0" 
through digital test mux and 
sweep the UVLO 0.4V reference voltage 
trimming code until the comparator toggles 
'''

HL_Th = 2.25  # 2.25V threshold
error_spread = 2.5e-3 # 2.5mv error spread
code_width = 4  # 4 bits trimming code
min_error = float('inf')
optimal_code = None
optimal_measured_value = None
force_voltage_low_limit = 0  # minimum voltage limit
force_voltage_high_limit = 3.7  # minimum voltage limit

for Code in range(2**code_width):
    # TODO: Write trimming code to device via I2C
    # Example (uncomment and fill device_address and field_info):
    # I2C_WRITE(device_address=0xXX, field_info=field_info, write_value=hex(Code))

    force_voltage = force_voltage_high_limit
    trigger = False

    while True:
        # Add noise simulation
        uvlo_forced_voltage = VFORCE(signal="IODATA0", reference="GND", value=force_voltage,error_spread=error_spread)
        # Check trigger condition
        trigger = VTRIG_HL(signal="PVDD", reference="GND", threshold=HL_Th, expected_value=force_voltage)

        if trigger:
            break
        elif uvlo_forced_voltage <= force_voltage_low_limit:
            print(f'..... Voltage min limit {force_voltage_low_limit}V crossed ........')
            break

        force_voltage -= 0.05  # decrease voltage by 50mV
        sleep(0.01)  # 10 ms delay

    error = abs(uvlo_forced_voltage - HL_Th)/abs(HL_Th) * 100
    if error < min_error:
        min_error = error
        optimal_code = hex(Code)
        optimal_measured_value = uvlo_forced_voltage

# Final check and reporting
if force_voltage_low_limit < optimal_measured_value < force_voltage_high_limit:
    print(f'............ Trim_Bg Test Passed ........')
    # TODO: Burn optimal trimming code to OTP via I2C
    # I2C_WRITE(device_address=0xXX, field_info=field_info, write_value=optimal_code)
else:
    print(f'............ Trim_Bg Test Failed ........')

print(f"Optimal Code: {optimal_code}")
print(f"Optimal Measured Value: {optimal_measured_value:.4f} V (Target: {HL_Th} V)")
print(f"Minimum Error: {min_error:.6f} %")







