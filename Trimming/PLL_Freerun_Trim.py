from dfttools import *
import time
import random

Test_Name = 'PLL_Freerun_Trim'
from Procedures import Startup
print(f'............ {Test_Name} ........')

target_value = 12.288e6          # 12.288MHz
lower_limit = 11.288e6 
higher_limit = 13.288e6 

I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_mode', 'length': 2, 'registers': [{'REG': '0x84', 'POS': 6, 'RegisterName': 'PLL_REG_5', 'RegisterLength': 8, 'Name': 'pll_mode[1:0]', 'Mask': '0xC0', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x17', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(3))      #dig_pll_freerun_en_vddd=1
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_p', 'length': 6, 'registers': [{'REG': '0x81', 'POS': 0, 'RegisterName': 'PLL reg 2', 'RegisterLength': 8, 'Name': 'pll_p[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': '00NNNNNN', 'Default': '0x06', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(6))         #dig_pll_prediv_vddd<5:0>=6d 
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_n', 'length': 6, 'registers': [{'REG': '0x82', 'POS': 0, 'RegisterName': 'PLL reg 3', 'RegisterLength': 8, 'Name': 'pll_n[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': '00NNNNNN', 'Default': '0x18', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(18))        #dig_pll_n<5:0>=24d 
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_ldet_cnt', 'length': 5, 'registers': [{'REG': '0x83', 'POS': 0, 'RegisterName': 'PLL reg 4', 'RegisterLength': 8, 'Name': 'pll_ldet_cnt[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': '000NNNNN', 'Default': '0x10', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(10)) #rfu_pll_ldet_cnt<4:0>=16d
# FREQFORCE(signal="IOCLK0",reference="GND",value=3.072e6)                             #BCLK frequency=3.072MHz
 
'''
Bring out on the digital test point the 
PLL output (divided?) and measure the clock frequency 
'''
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)  #Change page in regmap
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x08)   #enable "IODATA1" TMUX
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x23) #bring out the pll output


# Initialize minimum error and optimal code
min_error = float('inf')
optimal_code = None
optimal_measured_value = None
num_steps = 2**{'fieldname': 'pll_vco_ctrl', 'length': 2, 'registers': [{'REG': '0xCF', 'POS': 0, 'RegisterName': 'OTP FIELDS 31', 'RegisterLength': 8, 'Name': 'pll_vco_ctrl[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x02', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}.get('length')         # trimming field is 2 bit

for i in range(num_steps):
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_vco_ctrl', 'length': 2, 'registers': [{'REG': '0xCF', 'POS': 0, 'RegisterName': 'OTP FIELDS 31', 'RegisterLength': 8, 'Name': 'pll_vco_ctrl[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x02', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=i) # sweep trim code
    # time.sleep(0.0001)                                                                   # wait 100us
    measured_value = FREQMEASURE(signal="IODATA1", reference="GND",expected_value=target_value,error_spread=target_value*0.1)                     # Measure Frequency at "IODATA1"
    error = abs(measured_value - target_value)/target_value                                      # Calculate the distance from the target 12.288MHz
 
    # Check if the measured value is the nearest to the target   
    if error < min_error:
        min_error = error
        optimal_code = hex(i)
        optimal_measured_value = measured_value
    
    
# Check for limits
if lower_limit < optimal_measured_value < higher_limit:
    print(f'............ {Test_Name} Passed ........')
    # write the optimized code if the trim passed
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_vco_ctrl', 'length': 2, 'registers': [{'REG': '0xCF', 'POS': 0, 'RegisterName': 'OTP FIELDS 31', 'RegisterLength': 8, 'Name': 'pll_vco_ctrl[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x02', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=optimal_code)
else:
    print(f'............ {Test_Name} Failed ........')
    # if the trimh failed program detult zero
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_vco_ctrl', 'length': 2, 'registers': [{'REG': '0xCF', 'POS': 0, 'RegisterName': 'OTP FIELDS 31', 'RegisterLength': 8, 'Name': 'pll_vco_ctrl[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x02', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
print(f"Optimal Code: {optimal_code}")
print(f"Optimal measured value : {optimal_measured_value/1e6}MHz, Target vlaue : {target_value/1e6}MHz")
print(f"Minimum Error: {min_error}%")