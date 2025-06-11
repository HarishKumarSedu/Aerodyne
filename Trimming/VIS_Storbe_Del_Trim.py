from dfttools import *
from time import sleep
import random

Test_Name = 'PLL_Freerun_Trim'
from Procedures import Startup
print(f'............ {Test_Name} ........')
# designers must go through the details and correct the procedure
'''
Procedure 
-----------------
1. VI-sense IP needs to be enabled. 
2. Wait 100us. 
3. ds_vis_sar_strobedly_trim<3:0> = 1111. 
4. ds_vis_sar_strobedly_trim_en = 1. (trimming procedure enabled). 
5. Measure the frequency of the clock signal dd_vis_sar_strobedelay_clock. 
6. Decrease the bus value ds_vis_sar_strobedly_trim<3:0> until the measured frequency is close to 3.846153 MHz. In this case 130ns delay is reached, being measured freq. = 1/(2·delay). 
7. Store ds_vis_sar_strobedly_trim<3:0> - 1 in the OTP register. 
'''

I2C_WRITE(device_address="0x68",field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_vis_sar_strobedly_trim', 'length': 4, 'registers': [{'REG': '0xB2', 'POS': 0, 'RegisterName': 'OTP FIELDS 2', 'RegisterLength': 8, 'Name': 'otp_ds_vis_sar_strobedly_trim[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '84', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0xF)
I2C_WRITE(device_address="0x68",field_info={'fieldname': 'vis_sar_strobedly_trim_en', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 0, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'vis_sar_strobedly_trim_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '00NNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
# the measured frequency is close to 3.846153 MHz. In this case 130ns delay is reached, being measured freq. = 1/(2·delay).
# select the mux to bring out the dd_vis_sar_strobedelay_clock signal on "IOCLK1"
# I2C_WRITE(device_address="0x68",field_info=,write_value=)

# desingers needs to correct the assumptions
limit_percentage = 0.1 # assuming 
target_value = 3.846e6 # 3.846MHz
# higher and lower limits taken about +/- 10% of the target value 
lower_limit = target_value-target_value*limit_percentage
higher_limit = target_value+target_value*limit_percentage
error_spread = target_value*0.05 # 5% of target value

# LSB is the assumption designer needs to correct
# Step size
step_size = 150e3 # assumed 150kHz

# Initialize minimum error and optimal code
min_error = float('inf')
optimal_code = None
optimal_measured_value = None
num_steps = 2**4 # trimming field is 4 bit
for i in range(num_steps):
    # sweep trimg code
    I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_vis_sar_strobedly_trim', 'length': 4, 'registers': [{'REG': '0xB2', 'POS': 0, 'RegisterName': 'OTP FIELDS 2', 'RegisterLength': 8, 'Name': 'otp_ds_vis_sar_strobedly_trim[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '84', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=hex(i))
    # Generate monotonic values with step size
    expected_value = lower_limit + i * step_size 
    # Add white noise to the expected value
    # Pass the noisy value as the expected measurement values
    measured_value = FREQMEASURE(signal="IOCLK1", reference="GND", expected_value=expected_value, error_spread=error_spread)
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
    I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_vis_sar_strobedly_trim', 'length': 4, 'registers': [{'REG': '0xB2', 'POS': 0, 'RegisterName': 'OTP FIELDS 2', 'RegisterLength': 8, 'Name': 'otp_ds_vis_sar_strobedly_trim[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '84', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=optimal_code)
else:
    print(f'............ {Test_Name} Failed ........')
    # if the trimh failed program detult zero
    I2C_WRITE(device_address="0x68",field_info={'fieldname': 'otp_ds_vis_sar_strobedly_trim', 'length': 4, 'registers': [{'REG': '0xB2', 'POS': 0, 'RegisterName': 'OTP FIELDS 2', 'RegisterLength': 8, 'Name': 'otp_ds_vis_sar_strobedly_trim[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '84', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
print(f"Optimal Code: {optimal_code}")
print(f"Optimal measured value : {optimal_measured_value}Hz, Target vlaue : {target_value}Hz")
print(f"Minimum Error: {min_error}%")

























