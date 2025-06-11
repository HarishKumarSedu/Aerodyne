from dfttools import *
from time import sleep
import random

Test_Name = 'BG_Current'
from Procedures import Startup
print(f'............ {Test_Name} ........')

'''
-----------------------------------------------
  1.BG 1uA
  2.Turn ON the part in active mode, temp=27°C, vddp=3.7V, vddd=1.2V, UVLO trimmed, enable ref_bg;
  3.Wait 400 us;
  4.Bring out to the analog test point (rfu_ds_ref_test_en_vddd=8d) the 0.4V reference output voltage. Target voltage is 0.4V.
'''
# select the page 
# I2C_WRITE(device_address="0x68",field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=)
# 1. Enable ref_bg  select the field 
# I2C_WRITE(device_address="0x68",field_info=,write_value=)
# Bring out to the analog test point (rfu_ds_ref_test_en_vddd=8d) on "IODATA1"
# I2C_WRITE(device_address="0x68",field_info=,write_value=)
target_value = 1e-6 # 1uA
error_spread = target_value*0.05 # 5% of target value
measured_value = AMEASURE(signal="IODATA1", reference="GND", expected_value=target_value,error_spread=error_spread)
error = abs(measured_value - target_value)/abs(target_value) *100
print(f"Optimal measured value : {measured_value/ 1e-6}uA, Target vlaue : {target_value/ 1e-6}uA")
print(f"Minimum Error: {error}%")