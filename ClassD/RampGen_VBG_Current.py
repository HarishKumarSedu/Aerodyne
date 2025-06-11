from dfttools import *
from time import sleep
import random

Test_Name = 'RampGen_VBG_Current'
from Procedures import Startup

print(f'............ {Test_Name} ........')

'''
Current VBG/R
-------------------------------------------------
1. Turn ON the part in active mode, T=25degC, vddio=1.8V, vddp=3.6V, main bandgap trimmed,
   turn ON the PLL in closed loop, BCLK input=3.072MHz, OTP loaded for freerun frequency.
   Set the following register fields:
     dig_ds_cld_pwm_en_vddd = 1
     rfu_ds_fll_vco_freerun_en_vddd = 0
     rfu_ds_cld_fll_vco_fctrl_vddd<1:0> = 0
     dig_dd_cld_fll_vco_dith_vddd<5:0> = 32d
     rfu_ds_cld_fll_vco_amp_vddd<2:0> = 4d
     dig_ds_cld_fll_fd_fset_vddd<8:0> = 170d
     rfu_ds_cld_pwm_test_en_vddd = 1
     rfu_ds_test_sel_vddd<4:0> = 0d
2. Wait for 100us.
3. Bring out on the analog test point the ClassD analog test output.
4. Measure the current which is a n2p type.
'''

# Define device address (replace with actual address) optional
# "0x68" =   # Example device address, update accordingly

'''
# Step 1: Write required register fields for the test 
# !!!!!!!!!1 Designers must correct the field names cross checking the regmap
# '''''' page must be changed if it is requirend in the flow 
'''
# I2C_WRITE(device_address="0x68", field_info=dig_ds_cld_pwm_en_vddd, write_value=1)
# I2C_WRITE(device_address="0x68", field_info=rfu_ds_fll_vco_freerun_en_vddd, write_value=0)
# I2C_WRITE(device_address="0x68", field_info=rfu_ds_cld_fll_vco_fctrl_vddd, write_value=0)  # Assuming full field, bits <1:0>
# I2C_WRITE(device_address="0x68", field_info=dig_dd_cld_fll_vco_dith_vddd, write_value=32)
# I2C_WRITE(device_address="0x68", field_info=rfu_ds_cld_fll_vco_amp_vddd, write_value=4)
# I2C_WRITE(device_address="0x68", field_info=dig_ds_cld_fll_fd_fset_vddd, write_value=170)
# I2C_WRITE(device_address="0x68", field_info=rfu_ds_cld_pwm_test_en_vddd, write_value=1)
# I2C_WRITE(device_address="0x68", field_info=rfu_ds_test_sel_vddd, write_value=0)

# Step 2: Wait for 100 microseconds
sleep(0.0001)  # 100 us

'''
# Step 3: Bring out on the analog test point the ClassD analog test output
# This typically involves setting a mux or test output register
# Example (replace field_info and value with actual mux control):
'''
# I2C_WRITE(device_address="0x68", field_info=analog_test_mux_sel, write_value=0xXX)

# Step 4: Measure the current which is a n2p type
# AMEASURE parameters: signal pin, reference pin, expected value, error spread
expected_value = 1  # Expected current value (designer's simulation)
measured_value = AMEASURE(signal="IODATA1", reference="GND", expected_value=expected_value, error_spread=0)

print(f'Measured value : {measured_value}  # IRAMP VBG/R current')
