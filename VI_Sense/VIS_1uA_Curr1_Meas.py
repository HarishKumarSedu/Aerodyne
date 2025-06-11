from dfttools import *
from time import sleep

Test_Name = 'VIS_1uA_Curr1_Meas'
from Procedures import Startup

print(f'............ {Test_Name} ........')

'''
VIS 1uA Current Source Measurement
-------------------------------------------------
1. Power up with VI-sense enabled, main bandgap trimmed
2. Configure VIS channels and route current to "ADDR"
3. Measure 1uA current at "ADDR" pin
'''

from Procedures import Startup
from Procedures import VI_SNS_turn_on

'''
DESIGNER NOTES:
-------------------------------------------------
1. Current Routing:
   - Confirm "ADDR" pin is configured as current output
   - Verify mux selection for CURR_1U path
   - Check current mirror ratio settings

2. Measurement Setup:
   - Use picoammeter with guarded triaxial connection
   - Enable 10s integration time for stable readings
   - Maintain <1pF stray capacitance at "ADDR" pin
'''

# Step 2: Settling Time
sleep(0.0005)  # 500 us

# Step 3: Route Current to "ADDR"
# I2C_WRITE("0x68", addr_mux_sel, CURR1_OUT_SEL_CODE)  # Symbolic reference

# Step 4: Current Measurement
expected_curr = 1.0e-6    # 1.0 uA target
curr_error = 0.1e-6       # ±0.1 uA tolerance
imeas = AMEASURE(signal='"ADDR"', reference='"GND"',
                 expected_value=expected_curr,
                 error_spread=curr_error)

print(f'Measured Current: {imeas*1e6:.3f} uA [Target: {expected_curr*1e6:.1f}uA ±{curr_error*1e6:.1f}uA]')
