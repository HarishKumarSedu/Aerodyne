from dfttools import *
from time import sleep
import random

Test_Name = 'Selfreg_LDO_0v6_Trim'
from Procedures import Startup
print(f'............ {Test_Name} ........')

I2C_WRITE(device_address="0x68", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
I2C_WRITE(device_address="0x68",field_info={'fieldname': 'analdo_en_m', 'length': 1, 'registers': [{'REG': '0x1D', 'POS': 5, 'RegisterName': 'FORCE_REGISTERS_6', 'RegisterLength': 8, 'Name': 'analdo_en_m', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
I2C_WRITE(device_address="0x68",field_info=otp_ds_ref_self_ref_trim_0v6,write_value=0x0) #Default code

I2C_WRITE(device_address="0x68",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
I2C_WRITE(device_address="0x68",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0xA)
#I2C_WRITE(device_address="0x68",field_info=ref_test_en_buff,write_value=0x1)
'''
Bring 0.6V bandgap reference voltage to "IODATA1" through the analog test mux and trim it to the closest value to 0.6V
'''

# Initial value
percentage = 1e-2 # 1% difference
typical_value = 0.6
low_value = typical_value - typical_value*percentage
high_value = typical_value + typical_value*percentage
# LSB is the assumption designer needs to correct
# Step size
step_size = 7.57e-3 # 7.57mV

# Number of steps width of the field / bits
num_steps = 2^4  # 4-bit

# Standard deviation for white noise
noise_std_dev = 0.025

# Initialize minimum error and optimal code
min_error = float('inf')
optimal_code = None
optimal_measured_value = None

for i in range(num_steps):
    # sweep trimg code
    I2C_WRITE(device_address="0x68",field_info=otp_ds_ref_self_ref_trim_0v6,write_value=hex(i))
    expected_value = low_value + i * step_size 
    # Add white noise to each value
    measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=expected_value,error_spread=noise_std_dev)
    error = abs(measured_value - typical_value)/abs(typical_value) *100
    if error < min_error:
        min_error = error
        optimal_code = hex(i)
        optimal_measured_value = measured_value
    sleep(0.1)
# Check for limits
if low_value < optimal_measured_value < high_value:
    print(f'............ {Test_Name} Passed ........')
    # write the optimized code if the trim passed
    I2C_WRITE(device_address="0x68",field_info=otp_ds_ref_self_ref_trim_0v6,write_value=optimal_code)
else:
    print(f'............ {Test_Name} Failed ........')
    # if the trimh failed program detult zero
    I2C_WRITE(device_address="0x68",field_info=otp_ds_ref_self_ref_trim_0v6,write_value=0)
print(f"Optimal Code: {optimal_code}")
print(f"Optimal measured value : {optimal_measured_value}V, Target value : {typical_value}V")
print(f"Minimum Error: {min_error}%")
