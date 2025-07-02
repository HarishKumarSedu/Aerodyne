from dfttools import *
from time import sleep
Test_Name = 'VIS_1V6_Ref_Meas'
print(f'............ {Test_Name} ........')

'''
VIS 1.5V Reference Measurement
-------------------------------------------------
1. Power up with VI-sense enabled, main bandgap trimmed
2. Configure VIS voltage and current channels
3. Measure 1.6V reference at "ADDR" test point
4. Measure 0V reference ground at "IODATA1" test point
'''

from Procedures import Startup
from Procedures import VI_SNS_turn_on

# Step 2: Settling Time
sleep(0.0005)  # 500 µs

# Step 3: Route Reference to "ADDR" and "IODATA1"
I2C_WRITE("0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(1))  # Change page in regmap
I2C_WRITE("0x38", field_info={'fieldname': 'vis_atp_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'vis_atp_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(1))  # Enable test mux
I2C_WRITE("0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(5))  # Enable tests REF_1V6 and Reference "GND"

# Step 4: DC Voltage Measurement
expected_dc1 = 1.6       # Target voltage on "ADDR"
dc1_error = 0.005        # ±5mV tolerance
vref1V5 = VMEASURE(signal="ADDR", reference="GND", expected_value=expected_dc1, error_spread=dc1_error)
print(f'DC Reference Voltage: {vref1V5:.5f} V [Target: {expected_dc1:.2f}V ±{dc1_error*1000:.0f}mV]')
# Pass/Fail Criteria
if abs(vref1V5 - expected_dc1) <= dc1_error:
    print("PASS: Voltage within ±5mV specification")
else:
    print(f"FAIL: Voltage error {abs(vref1V5-expected_dc1)*1000:.1f}mV exceeds limit")