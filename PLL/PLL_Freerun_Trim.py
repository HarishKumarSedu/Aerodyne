from dfttools import *
from time import sleep
import random

Test_Name = 'PLL_Freerun_Trim'
from Procedures import Startup
print(f'............ {Test_Name} ........')

target_value = 12.288e6 # 12.288MHz
lower_limit = 11.288e6 
higher_limit = 13.288e6 
error_spread = target_value*0.05 # 5% of target value
'''
write the following fields
dig_pll_freerun_en_vddd=1 
BCLK frequency=3.072MHz, 
dig_pll_prediv_vddd<5:0>=6d 
dig_pll_n<5:0>=24d 
rfu_pll_ldet_cnt<4:0>=16d 
'''
# I2C_WRITE(device_address="0x68",field_info=,write_value=)
# BLCK = "IOCLK0"
FREQFORCE(signal="IOCLK0",reference="GND",value=3.072e6)
# designers identify and write 
'''
Bring out on the digital test point the 
PLL output (divided?) and measure the clock frequency 
'''
# LSB is the assumption designer needs to correct
# Step size
step_size = 500e3 # assumed 500kHz

# Initialize minimum error and optimal code
min_error = float('inf')
optimal_code = None
optimal_measured_value = None
num_steps = 2**2 # trimming field is 2 bit
for i in range(num_steps):
    # sweep trimg code
    I2C_WRITE(device_address="0x68",field_info={'fieldname': 'pll_vco_ctrl', 'length': 2, 'registers': [{'REG': '0xCF', 'POS': 0, 'RegisterName': 'OTP FIELDS 31', 'RegisterLength': 8, 'Name': 'pll_vco_ctrl[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '02', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=hex(i))
    # Generate monotonic values with step size
    expected_value = lower_limit + i * step_size 
    # Add white noise to the expected value
    # Pass the noisy value as the expected measurement values
    measured_value = FREQMEASURE(signal="IODATA1", reference="GND", expected_value=expected_value, error_spread=error_spread)
    error = abs(measured_value - target_value)/abs(target_value) *100
    if error < min_error:
        min_error = error
        optimal_code = hex(i)
        optimal_measured_value = measured_value
    sleep(0.1)
# Check for limits
if lower_limit < optimal_measured_value < higher_limit:
    print(f'............ {Test_Name} Passed ........')
    # write the optimized code if the trim passed
    I2C_WRITE(device_address="0x68",field_info={'fieldname': 'pll_vco_ctrl', 'length': 2, 'registers': [{'REG': '0xCF', 'POS': 0, 'RegisterName': 'OTP FIELDS 31', 'RegisterLength': 8, 'Name': 'pll_vco_ctrl[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '02', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=optimal_code)
else:
    print(f'............ {Test_Name} Failed ........')
    # if the trimh failed program detult zero
    I2C_WRITE(device_address="0x68",field_info={'fieldname': 'pll_vco_ctrl', 'length': 2, 'registers': [{'REG': '0xCF', 'POS': 0, 'RegisterName': 'OTP FIELDS 31', 'RegisterLength': 8, 'Name': 'pll_vco_ctrl[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '02', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
print(f"Optimal Code: {optimal_code}")
print(f"Optimal measured value : {optimal_measured_value}Hz, Target vlaue : {target_value}Hz")
print(f"Minimum Error: {min_error}%")
