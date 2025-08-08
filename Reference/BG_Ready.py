from dfttools import *
from time import sleep
import random
from Procedures import Startup
from Procedures import Global_enable

Test_Name = 'BG Ready'
print(f'............ {Test_Name} ........')

'''
Enable the bandgap, bring BG ready signal to pin "IOCLK1" 
through digital test mux and verify its logic value is correct
'''

# Enabling test page
I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1) # page 1
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'debug_in_en', 'length': 7, 'registers': [{'REG': '0x22', 'POS': 0, 'RegisterName': 'Debug resgister 1', 'RegisterLength': 8, 'Name': 'debug_in_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x4)
#Enabling digital TMUX
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x2)
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x21)

target_value = 1.2 # 1.2V
error_spread = target_value*0.04 # 4% of target value
measured_value = VMEASURE(signal="IOCLK1", reference="GND", expected_value=target_value,error_spread=error_spread)
error = abs(measured_value - target_value)/abs(target_value) *100
print(f"Optimal measured value : {measured_value}V, Target value : {target_value}V")
print(f"Minimum Error: {error}%")

