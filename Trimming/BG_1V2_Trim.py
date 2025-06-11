from dfttools import *
from time import sleep
import random

Test_Name = 'BG_1V2_Trim'
from Procedures import Startup
print(f'............ {Test_Name} ........')
'''
enable ref_bg, # designer needs identify
{'fieldname': 'otp_ds_ref_bg_ptat_trm', 'length': 3, 'registers': [{'REG': '0xB3', 'POS': 5, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_ptat_trm[2:0]', 'Mask': '0xE0', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}<2:0>=0d, 
{'fieldname': 'otp_ds_ref_bg_trm_0v6', 'length': 4, 'registers': [{'REG': '0xB0', 'POS': 0, 'RegisterName': 'OTP FIELDS 0', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_trm_0v6[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}<3:0>=0d, 
{'fieldname': 'otp_ds_ref_bg_trm_0v9', 'length': 4, 'registers': [{'REG': '0xB0', 'POS': 4, 'RegisterName': 'OTP FIELDS 0', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_trm_0v9[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}<3:0>=0d, 
{'fieldname': 'otp_ds_ref_bg_trm_1v2', 'length': 4, 'registers': [{'REG': '0xB1', 'POS': 0, 'RegisterName': 'OTP FIELDS 1', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_trm_1v2[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '80', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}<3:0>=0d; 
'''
I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_ref_bg_ptat_trm', 'length': 3, 'registers': [{'REG': '0xB3', 'POS': 5, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_ptat_trm[2:0]', 'Mask': '0xE0', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_ref_bg_trm_0v6', 'length': 4, 'registers': [{'REG': '0xB0', 'POS': 0, 'RegisterName': 'OTP FIELDS 0', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_trm_0v6[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_ref_bg_trm_0v9', 'length': 4, 'registers': [{'REG': '0xB0', 'POS': 4, 'RegisterName': 'OTP FIELDS 0', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_trm_0v9[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_ref_bg_trm_1v2', 'length': 4, 'registers': [{'REG': '0xB1', 'POS': 0, 'RegisterName': 'OTP FIELDS 1', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_trm_1v2[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '80', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
# Bring out to the analog test point (rfu_ds_ref_test_en_vddd=4d) the 1.2V reference output voltage. Target voltage is 1.2V; 
# I2C_WRITE(device_address="0x68",field_info=,write_value=)

'''
Bring 1.2V bandgap reference voltage to "IODATA1" through the analog test mux and trim it to the closest value to 1.2V
'''

# Initial value 
percentage = 0.1 # 10% deviation

typical_value = 1.2
low_value = typical_value - typical_value*percentage
high_value = typical_value + typical_value*percentage

# Step size, designers needs to enter by lsb size
step_size = 0.01 # 10mV

# Number of steps width of the field / bits
num_steps = 2**4  # 4-bit

# Standard deviation for white noise
noise_std_dev = 0.025

# Initialize minimum error and optimal code
min_error = float('inf')
optimal_code = None
optimal_measured_value = None

for i in range(num_steps):
    # sweep trimg code
    I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_ref_bg_trm_1v2', 'length': 4, 'registers': [{'REG': '0xB1', 'POS': 0, 'RegisterName': 'OTP FIELDS 1', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_trm_1v2[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '80', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=hex(i))
    # Generate monotonic values with step size
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
    I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_ref_bg_trm_1v2', 'length': 4, 'registers': [{'REG': '0xB1', 'POS': 0, 'RegisterName': 'OTP FIELDS 1', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_trm_1v2[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '80', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=optimal_code)
else:
    print(f'............ {Test_Name} Failed ........')
    # if the trimh failed program detult zero
    I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_ref_bg_trm_1v2', 'length': 4, 'registers': [{'REG': '0xB1', 'POS': 0, 'RegisterName': 'OTP FIELDS 1', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_trm_1v2[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '80', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0)
print(f"Optimal Code: {optimal_code}")
print(f"Optimal measured value : {optimal_measured_value}V, Target vlaue : {typical_value}V")

print(f"Minimum Error: {min_error}%")
