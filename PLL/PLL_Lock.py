from dfttools import *
from time import sleep

Test_Name = 'PLL_Lock'
from Procedures import Startup
print(f'............ {Test_Name} ........')

pll_target_value_1 = 12.288e6 # 12.288MHz
BLCK_Set_1 = 3.072e6 # 3.072MHz
pll_target_value_2 = 13.68e6 # 13.6MHz
BLCK_Set_2 = 3.4e6 # 3.4MHz
pll_error_spread_1 = pll_target_value_1*0.01 # 1% of target value
pll_error_spread_2 = pll_target_value_2*0.01 # 1% of target value

'''
  1.Turn ON the part in active mode (PLL ON), T=25degC, vddd=1.2V, Main bandgap trimmed,
    dig_pll_freerun_en_vddd=0
    BCLK frequency=3.072MHz,
    dig_pll_prediv_vddd<5:0>=6d
    dig_pll_n<5:0>=24d
    rfu_pll_ldet_cnt<4:0>=16d
  2.Wait for 300us, check lock signal is high
  3. Bring out on the digital test point the PLL output (divided?) and measure the frequency. It must be 12.288MHz
  4.Change the BCLK frequency higher by 10%, to 3.4MHz and check lock signal returns to high level (expectation is that it glitches to low level)
  5.Measure the Output Frequency. It must be13.6MHz 
 
'''
# I2C_WRITE(device_address="0x68",field_info=,write_value=)
# BLCK = "IOCLK0"
#  BCLK frequency=3.072MHz
FREQFORCE(signal="IOCLK0",reference="GND",value=BLCK_Set_1)
pll_measured_value_1 = FREQMEASURE(signal="IODATA1", reference="GND", expected_value=pll_target_value_1, error_spread=pll_error_spread_1)
# check the measured value within the error spread limit 
# error pread makes accounts measurement error also 
if (pll_target_value_1 - pll_error_spread_1) < pll_measured_value_1 < (pll_target_value_1 + pll_error_spread_1):
  # check for the intial lock frequency pass 12.288MHz
  #  BCLK frequency=3.072MHz
  FREQFORCE(signal="IOCLK0",reference="GND",value=BLCK_Set_1)
  pll_measured_value_2 = FREQMEASURE(signal="IODATA1", reference="GND", expected_value=pll_target_value_2, error_spread=pll_error_spread_2)
  
  if (pll_target_value_2 - pll_error_spread_1) < pll_measured_value_2 < (pll_target_value_2 + pll_error_spread_2):
    # check for the intial lock frequency pass 13.6MHz
    #  BCLK frequency=3.4MHz
    print(f'.... {Test_Name}.., Passed....')
    print(f'BCLK = {BLCK_Set_1 / 1e6}MHz , pll Freq Measured : {pll_measured_value_1 / 1e6}MHz')
    print(f'BCLK = {BLCK_Set_2 / 1e6}MHz , pll Freq Measured : {pll_measured_value_2 / 1e6}MHz')
  else:
    print(f'.... {Test_Name}.., Frequency Locking Failed ....')
    print(f'BCLK = {BLCK_Set_2 / 1e6}MHz , pll Freq Measured : {pll_measured_value_2 / 1e6}MHz')
  
else:
  print(f'.... {Test_Name}.., Failed Trim PLL ....')
  print(f'BCLK = {BLCK_Set_1 / 1e6}MHz , pll Freq Measured : {pll_measured_value_1 / 1e6}MHz')