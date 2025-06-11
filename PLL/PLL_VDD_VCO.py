from dfttools import *
from time import sleep

Test_Name = 'PLL_VDD_VCO'
from Procedures import Startup
print(f'............ {Test_Name} ........')

pll_target_value = 680e-6 # 680mV
BLCK_Set = 3.072e6 # 3.072MHz
pll_error_spread = pll_target_value*0.01 # 1% of target value


'''
  1.Turn ON the part in active mode (PLL ON), T=25degC, vddd=1.2V, Main bandgap trimmed,
    dig_pll_freerun_en_vddd=1
    BCLK frequency=3.072MHz,
    dig_pll_prediv_vddd<5:0>=6d
    dig_pll_n<5:0>=24d
    rfu_pll_ldet_cnt<4:0>=16d
  2.Wait for 300us
  3.Bring out on the analog test point the PLL VDDCO voltage. Measure it with a high input impedance voltmeter
  4.Target value is around 680mV (typ)
'''
# I2C_WRITE(device_address="0x68",field_info=,write_value=)
# BLCK = "IOCLK0"
# BCLK frequency=3.072MHz
FREQFORCE(signal="IOCLK0",reference="GND",value=BLCK_Set)#
'''
Bring out all the necessary signals 
'''
# I2C_WRITE(device_address="0x68",field_info=,write_value=)
pll_measured_vco_vdd = AMEASURE(signal="IODATA1", reference="GND", expected_value=pll_target_value,error_spread=pll_error_spread)
error = abs(pll_measured_vco_vdd - pll_target_value)/abs(pll_target_value) *100
print(f"Optimal measured value : {pll_measured_vco_vdd}V, Target vlaue : {pll_target_value}V")
