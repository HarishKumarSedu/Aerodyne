from dfttools import *
from time import sleep

Test_Name = 'VIS_0V5_Curr2_Meas'
print(f'............ {Test_Name} ........')

'''
Aerodyne VI Sense ADC - 0.5uA Current Measurement
-------------------------------------------------
1. Power up with VI-sense enabled, main bandgap trimmed
2. Configure VIS channels and route current to ATTP
3. Measure 0.5uA current at ATTP test point
'''

# Device Configuration
TEMP = 25       # 25C ambient
VDDA = 3.0      # Analog supply
VDDD = 1.2      # Digital supply
VDDP = 3.7      # Power supply

# Step 1: Channel Configuration (Symbolic References)
# I2C_WRITE("0x68", dig_ds_vis_channel_v_en, 1)
# I2C_WRITE("0x68", dig_ds_vis_dac_v_en, 1)
# I2C_WRITE("0x68", dig_ds_vis_sarmute_v, 0)
# I2C_WRITE("0x68", dig_ds_vis_int_res_v, 1)
# I2C_WRITE("0x68", dig_ds_vis_digres_v, 0)

# I2C_WRITE("0x68", dig_ds_vis_channel_i_en, 1)
# I2C_WRITE("0x68", dig_ds_vis_dac_i_en, 1)
# I2C_WRITE("0x68", dig_ds_vis_sarmute_i, 0)
# I2C_WRITE("0x68", dig_ds_vis_int_res_i, 1)
# I2C_WRITE("0x68", dig_ds_vis_digres_i, 0)

'''
DESIGNER NOTES:
-------------------------------------------------
1. Current Source Configuration:
   - Verify current mirror ratio = 1:1
   - Check DAC LSB weight calibration
   - Confirm reference current stability

2. Measurement Protocol:
   - Use guarded triaxial connection
   - Enable picoammeter zero-check
   - Maintain <10pA bias current
'''

# Step 2: Settling Time
sleep(0.0005)  # 500 us

# Step 3: Route Current to ATTP -> "ADDR"
# I2C_WRITE("0x68", attp_mux_sel, CURR1U_OUT_SEL_CODE)  # Symbolic reference

# Step 4: Current Measurement
expected_curr = 0.5e-6    # 0.5 uA target
curr_error = 0.05e-6      # ±0.05 uA tolerance
imeas = AMEASURE(signal="ADDR", reference="GND",
                 expected_value=expected_curr,
                 error_spread=curr_error)

print(f'Measured Current: {imeas*1e6:.3f} uA [Target: {expected_curr*1e6:.1f}uA ±{curr_error*1e6:.1f}uA]')

# Pass/Fail Criteria
if abs(imeas - expected_curr) <= curr_error:
    print("PASS: Current within ±0.05uA specification")
else:
    print(f"FAIL: Current error {(imeas-expected_curr)*1e6:.2f}uA exceeds limit")