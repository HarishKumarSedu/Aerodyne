from dfttools import *
from time import sleep

Test_Name = 'IODATA1_DC_Measurement'
from Procedures import Startup

print(f'............ {Test_Name} ........')

'''
"IODATA1" DC Voltage Validation
-------------------------------------------------
1. Power up device with specified conditions
2. Configure VIS and I/O data path
3. Measure DC voltage at "IODATA1" pin
4. Validate against 2.0V ±5% specification
'''

from Procedures import Startup
from Procedures import VI_SNS_turn_on


# Step 2: "IODATA1" Signal Routing
# I2C_WRITE("0x68", io_data1_mux_sel, ANALOG_SIGNAL_SEL)  # Replace with actual mux code
# I2C_WRITE("0x68", io_data1_termination, ENABLE_50OHM)  # Set termination

# Wait for Signal Stabilization (Critical for DC Accuracy)
sleep(0.0005)  # 500 µs

# Step 3: DC Voltage Measurement
expected_value = 2.0       # Target voltage (2.0V ±5%)
tolerance_percent = 5      # ±5% tolerance
error_spread = expected_value * (tolerance_percent / 100)  # ±0.10V

measured_value = VMEASURE(
    signal='"IODATA1"', 
    reference='"GND"',
    expected_value=expected_value,
    error_spread=error_spread
)

# Step 4: Pass/Fail Criteria
lower_limit = expected_value - error_spread  # 1.90V
upper_limit = expected_value + error_spread  # 2.10V

print(f'Measured DC Voltage: {measured_value:.3f} V')
print(f'Acceptable Range: {lower_limit:.2f}V to {upper_limit:.2f}V (±{tolerance_percent}%)')

if lower_limit <= measured_value <= upper_limit:
    print("RESULT: PASS - Voltage within specification")
else:
    print("RESULT: FAIL - Voltage out of tolerance")

# Step 5: Noise Measurement (Commented Implementation)
'''
noise_bw = (20, 24000)  # 20Hz-24kHz
target_noise = 45e-6     # 45µVRMS
noise_rms = NOISEMEASURE(signal="ADDR", reference="GND",
                         bandwidth=noise_bw, 
                         expected_value=target_noise)
'''


'''
Critical Design Notes
-------------------------------------------------
1. Measurement System Validation:
   - Confirm voltmeter calibration (NIST-traceable standard)
   - Verify probe loading <10pF || >10MOhm
   - Enable 10x attenuation if measuring high-impedance nodes

2. Signal Path Verification:
   - Confirm "IODATA1" mux selection code in register map
   - Check for crosstalk from digital signals (measure adjacent pins)
   - Validate ground reference stability (measure "GND"-GNDSNS offset)

3. Thermal Considerations:
   - Allow 5-minute warm-up for thermal stabilization
   - Monitor die temperature via on-chip sensor (if available)
   - For extended testing, implement temperature compensation

4. Noise Considerations (Future Implementation):
   - Bandwidth: 20Hz-24kHz (audio band)
   - Window: Hanning with 50% overlap
   - Averaging: 1000 samples minimum
'''

# Optional: Add Measurement History Logging
'''
with open('voltage_log.csv', 'a') as f:
    f.write(f'{time.time()},{measured_value:.4f}\n')
'''

# Debugging Aids (Comment in Production)
'''
print(f'VDDA Actual: {MEASURE_SUPPLY("VDDA"):.2f}V')
print(f'Ground Offset: {VMEASURE(""GND"", "GNDSNS"):.1f}µV')
'''

# Example Output
'''
............ IODATA1_DC_Measurement ........
Measured DC Voltage: 2.03 V
Acceptable Range: 1.90V to 2.10V (±5%)
RESULT: PASS - Voltage within specification
'''
