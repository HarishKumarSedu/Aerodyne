from dfttools import *
from time import sleep
import random

Test_Name = 'AnaLDO_Feedback_Votlage'
from Procedures import Startup
print(f'............ {Test_Name} ........')

'''
-----------------------------------------------
  1.Analdo feedback
  2.Turn ON the part in active mode, temp=27°C, vddp=3.7V, vddd=1.2V, UVLO trimmed, Bandgap ON, bandgap ready signal HIGH;
  3.Wait 400 us;
  4.Bring out to the analog test point (rfu_ds_ref_test_en_vddd=2d) on "IODATA1"
'''
# select the page 
# I2C_WRITE(device_address="0x68",field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=)
# 1. Enable ref_bg  select the field 
# I2C_WRITE(device_address="0x68",field_info=,write_value=)
# Bring out to the analog test point (rfu_ds_ref_test_en_vddd=) on "IODATA1"
# I2C_WRITE(device_address="0x68",field_info=,write_value=)

target_value = 0.4 # 0.4V
error_spread = target_value*0.05 # 5% of target value
measured_value = VMEASURE(signal="IODATA0", reference="GND", expected_value=target_value,error_spread=error_spread)
error = abs(measured_value - target_value)/abs(target_value) *100
print(f"Optimal measured value : {measured_value}V, Target vlaue : {target_value}V")
print(f"Minimum Error: {error}%")