from dfttools import *
from time import sleep
import random

Test_Name = 'PLL_Freerun_Trim'
from Procedures import Startup
print(f'............ {Test_Name} ........')

'''
dig_ds_cld_pwm_en_vddd=1
rfu_ds_fll_vco_freerun_en_vddd=1
rfu_ds_cld_fll_vco_fctrl_vddd<1:0> =0
dig_dd_cld_fll_vco_dith_vddd<5:0>=32d
rfu_ds_cld_fll_vco_amp_vddd<2:0>=4d
dig_ds_cld_fll_fd_fset_vddd<8:0>=170d
'''
I2C_WRITE(device_address="0x68",field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
I2C_WRITE(device_address="0x68",field_info={'fieldname': 'cld_pwm_en_m', 'length': 1, 'registers': [{'REG': '0x19', 'POS': 6, 'RegisterName': 'Force registers 2', 'RegisterLength': 8, 'Name': 'cld_pwm_en_m', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': '0NNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# not able to find desingers must  find rfu_ds_fll_vco_freerun_en_vddd=1
# I2C_WRITE(device_address="0x68",field_info=,write_value=)
I2C_WRITE(device_address="0x68",field_info={'fieldname': 'cld_fll_vco_fctrl', 'length': 2, 'registers': [{'REG': '0x75', 'POS': 4, 'RegisterName': 'SSC reg 6', 'RegisterLength': 8, 'Name': 'cld_fll_vco_fctrl[1:0]', 'Mask': '0x30', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': '00NNNNNN', 'Default': '04', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
# not able to find desingers must  find dig_dd_cld_fll_vco_dith_vddd<5:0>=32d
# I2C_WRITE(device_address="0x68",field_info=,write_value=)
I2C_WRITE(device_address="0x68",field_info={'fieldname': 'cld_fll_vco_amp', 'length': 3, 'registers': [{'REG': '0x75', 'POS': 0, 'RegisterName': 'SSC reg 6', 'RegisterLength': 8, 'Name': 'cld_fll_vco_amp[2:0]', 'Mask': '0x7', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': '00NNNNNN', 'Default': '04', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x4)
# not able to find desingers must  finddig_ds_cld_fll_fd_fset_vddd<8:0>=170d
# I2C_WRITE(device_address="0x68",field_info=,write_value=)
'''Bring out on the digital test point the PWM clock output 
ana_dd_fllvco_classdck1_vddd and measure the clock frequency'''
# Bring out the singla through "ADDR"/ write test mux
# I2C_WRITE(device_address="0x68",field_info=,write_value=)

# desingers needs to correct the assumptions
target_value = 289.275e3 
# higher and lower limits taken about +/- 10% of the target value 
lower_limit = 275e3
higher_limit = 303e3
error_spread = target_value*0.05 # 5% of target value

# LSB is the assumption designer needs to correct
# Step size
step_size = 437.5 # assumed 437.5Hz

# Initialize minimum error and optimal code
min_error = float('inf')
optimal_code = None
optimal_measured_value = None
num_steps = 2**6 # trimming field is 6 bit
for i in range(num_steps):
    # sweep trimg code
    I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_fll_vco_trm_5l', 'length': 6, 'registers': [{'REG': '0xB7', 'POS': 0, 'RegisterName': 'OTP FIELDS 7', 'RegisterLength': 8, 'Name': 'otp_ds_fll_vco_trm_5l[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=hex(i))
    # Generate monotonic values with step size
    expected_value = lower_limit + i * step_size 
    # Add white noise to the expected value
    # Pass the noisy value as the expected measurement values
    measured_value = FREQMEASURE(signal="ADDR", reference="GND", expected_value=expected_value, error_spread=error_spread)
    error = abs(measured_value - target_value)/abs(target_value) *100
    if error < min_error:
        min_error = error
        optimal_code = hex(i)
        optimal_measured_value = measured_value
    sleep(0.05)
# Check for limits
if lower_limit < optimal_measured_value < higher_limit:
    print(f'............ {Test_Name} Passed ........')
    # write the optimized code if the trim passed
    I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_fll_vco_trm_5l', 'length': 6, 'registers': [{'REG': '0xB7', 'POS': 0, 'RegisterName': 'OTP FIELDS 7', 'RegisterLength': 8, 'Name': 'otp_ds_fll_vco_trm_5l[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=optimal_code)
else:
    print(f'............ {Test_Name} Failed ........')
    # if the trimh failed program detult zero
    I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_fll_vco_trm_5l', 'length': 6, 'registers': [{'REG': '0xB7', 'POS': 0, 'RegisterName': 'OTP FIELDS 7', 'RegisterLength': 8, 'Name': 'otp_ds_fll_vco_trm_5l[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
print(f"Optimal Code: {optimal_code}")
print(f"Optimal measured value : {optimal_measured_value}Hz, Target vlaue : {target_value}Hz")
print(f"Minimum Error: {min_error}%")




























