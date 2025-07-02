from dfttools import *
from time import sleep
import random

Test_Name = 'LPF_VCM_Voltage'
from Procedures import Startup
# from Procedures import Playback suppose this procedure will be available
print(f'............ {Test_Name} ........')

'''
LPF Common Mode Voltage Test
-------------------------------------------------
1. Configure the device to enable LPF common mode voltage output
2. Bring the LPF VCM voltage to pin "IODATA1" through the analog test mux
3. Measure the voltage at "IODATA1"
'''
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x01)
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dac_lpf_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 4, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'cld_dac_lpf_test_en', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)  # Enable current test mode
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
# Define device address (replace with actual address)
# "0x38" = 0xXX  # Example device address, update accordingly

'''
! Important designers must correct the fields and write the procedure
# Step 1: Configure registers to enable LPF common mode voltage
# Example register writes - replace field_info and values with actual LPF control registers
'''
# I2C_WRITE(device_address="0x38", field_info=lpf_vcm_enable, write_value=1)
# I2C_WRITE(device_address="0x38", field_info=lpf_vcm_voltage_select, write_value=1)

'''
# Step 2: Route LPF VCM voltage to "IODATA1" through analog test mux
# Assuming 'analog_test_mux_sel' controls the analog test mux output
'''
# I2C_WRITE(device_address="0x38", field_info=analog_test_mux_sel, write_value=0xXX)  # LPF_VCM selection code

# Wait for signal stabilization
sleep(0.001)  # 1 ms

# Step 3: Measure VCM voltage
expected_value = 1.5  # Expected common mode voltage (1.5V)
error_spread = expected_value * 0.05  # 5% error margin
measured_value = VMEASURE(signal="IODATA1", reference="ADDR", expected_value=expected_value, error_spread=error_spread)

print(f'Expected VCM voltage: {expected_value:.2f} V | Measured: {measured_value:.3f} V')
