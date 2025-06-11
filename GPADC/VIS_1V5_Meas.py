from dfttools import *
from time import sleep

Test_Name = 'VIS_1V5_Meas'
from Procedures import Startup

print(f'............ {Test_Name} ........')

'''
VIS 1.5V Reference Measurement
-------------------------------------------------
1. Power up with VI-sense enabled, main bandgap trimmed
2. Configure VIS voltage and current channels
3. Measure 1.5V reference at "ADDR" test point
'''

# Device Configuration
TEMP = 25       # 25°C ambient
VDDA = 3.0      # Analog supply
VDDD = 1.2      # Digital supply
VDDP = 3.7      # Power supply

# Define device address (replace with actual)
# "0x68" = 0xXX

# Step 1: Power Up and VIS Configuration

# Voltage Channel Configuration (Symbolic References)
# I2C_WRITE("0x68", dig_ds_vis_channel_v_en, 1)
# I2C_WRITE("0x68", dig_ds_vis_dac_v_en, 1)
# I2C_WRITE("0x68", dig_ds_vis_sarmute_v, 0)
# I2C_WRITE("0x68", dig_ds_vis_int_res_v, 1)
# I2C_WRITE("0x68", dig_ds_vis_digres_v, 0)

# Current Channel Configuration (Symbolic References)
# I2C_WRITE("0x68", dig_ds_vis_channel_i_en, 1)
# I2C_WRITE("0x68", dig_ds_vis_dac_i_en, 1)
# I2C_WRITE("0x68", dig_ds_vis_sarmute_i, 0)
# I2C_WRITE("0x68", dig_ds_vis_int_res_i, 1)
# I2C_WRITE("0x68", dig_ds_vis_digres_i, 0)

'''
DESIGNER NOTES:
-------------------------------------------------
1. Symbolic Register Implementation:
   - All register fields should be defined as symbolic constants
   - Actual implementation requires proper symbol definition
   - Example: dig_ds_vis_channel_v_en = (register_addr, bit_mask)

2. Signal Routing Verification:
   - Confirm "ADDR" pin is configured as analog output
   - Verify mux selection code in register map
   - Check for conflicts with digital address functionality
'''

# Step 2: Settling Time
sleep(0.0005)  # 500 µs

# Step 3: Route Reference to "ADDR"
# I2C_WRITE("0x68", addr_mux_sel, REF_OUT_SEL_CODE)  # Symbolic reference

# Step 4: DC Voltage Measurement
expected_dc = 1.5       # Target voltage
dc_error = 0.005        # ±5mV tolerance
vref = VMEASURE(signal='"ADDR"', reference='"GND"', 
                expected_value=expected_dc, error_spread=dc_error)

print(f'DC Reference Voltage: {vref:.5f} V [Target: {expected_dc:.2f}V ±{dc_error*1000:.0f}mV]')

# Pass/Fail Criteria
if abs(vref - expected_dc) <= dc_error:
    print("PASS: Voltage within ±5mV specification")
else:
    print(f"FAIL: Voltage error {abs(vref-expected_dc)*1000:.1f}mV exceeds limit")

# Example Output
'''
............ VIS_1V5_Meas ........
DC Reference Voltage: 1.50234 V [Target: 1.50V ±5mV]
PASS: Voltage within ±5mV specification
'''

'''
Modification History:
-------------------------------------------------
1. Signal Routing Changed: ATTP -> "ADDR"
2. Removed explicit symbol class
3. Maintained symbolic references in I2C_WRITE
4. Added symbol definition requirements
'''
# Symbolic I2C_WRITE Template
'''
# Format: I2C_WRITE(device, register_symbol, value)
# Requires symbol-to-register mapping implementation
# Example: I2C_WRITE("0x68", dig_ds_vis_channel_v_en, 1)
'''
