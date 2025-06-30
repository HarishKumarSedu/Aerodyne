from dfttools import *
from time import sleep
import random

Test_Name = 'RampGen_PVDD_Current'
from Procedures import Startup
print(f'............ {Test_Name} ........')
'''
Current vddp/R
-------------------------------------------------
  1.Turn ON the part in active mode, T=25degC, vddio=1.8V, vddp=3.6V, main bandgap
    trimmed, turn ON the PLL in closed loop, BCLK input=3.072MHz, OTP loaded for
    freerun frequency. Set
      dig_ds_cld_pwm_en_vddd=1
      rfu_ds_fll_vco_freerun_en_vddd=0
      rfu_ds_cld_fll_vco_fctrl_vddd<1:0> =0
      dig_dd_cld_fll_vco_dith_vddd<5:0>=32d
      rfu_ds_cld_fll_vco_amp_vddd<2:0>=4d
      dig_ds_cld_fll_fd_fset_vddd<8:0>=170d
      rfu_ds_cld_pwm_test_en_vddd=1
      rfu_ds_test_sel_vddd<4:0>=3d
  2.Wait for 100us.
  3.Bring out on the analog test point the ClassD analog test output
  4.Measure the current which is a n2p type.
'''
# '#' is the comment remove the to write in the templated line or just copy and pate required instruction line 
# Write required register fields for the test
# I2C_WRITE(device_address="0x68",field_info=,write_value=)
# Bring out the singla through "IODATA1" write test mux
# I2C_WRITE(device_address="0x68",field_info=,write_value=)

'''
AMEASURE is the function to measure the Current from the specified 
signal pin wrt to the reference 
provide the the expected_value which designer expect from simulation 
error_spread is how much is the error expected ... this gives real feel of measuring while 
when test is executing 
in bench setup AMEASURE function measure the current from instrument/device 
'''
expected_value=1
measured_value = AMEASURE(signal="ADDR", reference="GND", expected_value=expected_value, error_spread=0)

print(f'Measured value : {measured_value}')