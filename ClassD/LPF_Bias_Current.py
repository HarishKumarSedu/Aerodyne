from dfttools import *
from time import sleep
import random

Test_Name = 'LPF_BIAS_Current'
from Procedures import Startup
# from Procedures import Playback suppose this procedure will be available

print(f'............ {Test_Name} ........')

'''
LPF Bias Current Test
-------------------------------------------------
1. Configure the device to enable LPF bias current output.
2. Bring the LPF test current (p2n type) to pin "IODATA1" through the analog test mux.
3. Measure the current at "IODATA1".
'''

# Define device address (replace with actual address)
# "0x38" = 0xXX  # Example device address, update accordingly

'''
! Important designers must correct the fields and write the procedure
# Step 1: Configure registers to enable LPF bias current output
# Example register writes - replace field_info and values with actual LPF control registers
# Step 1) Turn ON the part in active mode, T=25degC, vddio=1.8V, vddp=3.7V, main bandgap trimmed. Set:
# dig_ds_cld_bias_en = 1
# Step 2) wait 200us
# Step 3) set 
# rfu_ds_cld_dac_lpf_test_en = 1
# rfu_ds_test_sel[3:0] = 0

# Step 4) Measure the out current from the positive analog test point (500nA) 

'''
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x00)
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dac_lpf_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 4, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'cld_dac_lpf_test_en', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)  # Enable current test mode
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
'''
# Step 2: Bring LPF test current to "IODATA1" through analog test mux
# Assuming 'analog_test_mux_sel' controls the analog test mux output pin selection "IODATA1"
'''
# I2C_WRITE(device_address="0x38", field_info=analog_test_mux_sel, write_value=0xXX)  # p2n current path

# Wait a short time for signals to stabilize
sleep(0.001)  # 1 ms

# Step 3: Measure the current at "IODATA1" (p2n type)
expected_value = 500e-9  # 500nA expected current
error_spread = expected_value * 0.05  # 5% error spread
measured_value = AMEASURE(signal="IODATA1", reference="GND", expected_value=expected_value, error_spread=error_spread)

print(f'Expected  LPF bias current (p2n) at "IODATA1" wrt "GND": {expected_value /  1e-9} nA')
print(f'Measured LPF bias current (p2n) at "IODATA1" wrt "GND": {measured_value /  1e-9} nA')
