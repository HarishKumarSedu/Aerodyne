from dfttools import *
from time import sleep

Test_Name = 'VIS_1V6_Noise_Meas'
print(f'............ {Test_Name} ........')

'''
VIS 1.6V Reference Measurement
-------------------------------------------------
1. Power up with VI-sense enabled, main bandgap trimmed
2. Configure VIS channels and route reference to "ADDR" wrt "GND"
3. Measure DC voltage at "ADDR" test point
'''


from Procedures import Startup
from Procedures import VI_SNS_turn_on

# Step 2: Settling Time
sleep(0.0005)  # 500 us

# Step 3: Route Reference to "ADDR"
# I2C_WRITE("0x68", attp_mux_sel, REF_POS_SEL_CODE)  # Symbolic reference

# Step 4: DC Voltage Measurement
expected_dc = 1.6        # Target voltage
dc_error = 0.005         # ±5mV tolerance
vref = VMEASURE(signal="ADDR", reference="GND",
                expected_value=expected_dc, 
                error_spread=dc_error)

print(f'DC Reference Voltage: {vref:.5f} V [Target: {expected_dc:.2f}V ±{dc_error*1000:.0f}mV]')


# Pass/Fail Criteria (DC Only)
dc_pass = abs(vref - expected_dc) <= dc_error
if dc_pass:
    print("PASS: DC specification met")
else:
    print(f"FAIL: DC error {abs(vref-expected_dc)*1000:.1f}mV exceeds limit")
