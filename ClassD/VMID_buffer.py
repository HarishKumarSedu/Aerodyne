from dfttools import *
from time import sleep 
import random
Test_Name = '"VMID" buffer test'
from Procedures import speakerOff

print(f'............ {Test_Name} ........')

'''
"VMID" buffer test
Step 1. Configure the device registers to enable testing.
Step 2. Bring the DAC voltage reference to pin "IODATA1" through the analog test mux p and the local ground to pin "ADDR" through the analog test mux n.
Step 3. Wait for the signal to stabilize and measure the differential voltage "IODATA1" wrt "ADDR".
'''

# Select register page
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1) # page 1
# Enable forcing and disable only
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_shared_force', 'length': 1, 'registers': [{'REG': '0x18', 'POS': 0, 'RegisterName': 'Force registers 1', 'RegisterLength': 8, 'Name': 'cld_shared_force', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '00NNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)  # class D force enable
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_pwm_en_m', 'length': 1, 'registers': [{'REG': '0x19', 'POS': 6, 'RegisterName': 'Force registers 2', 'RegisterLength': 8, 'Name': 'cld_pwm_en_m', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': '0NNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0) # cld_pwm disable
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_lpf_en_m', 'length': 1, 'registers': [{'REG': '0x19', 'POS': 5, 'RegisterName': 'Force registers 2', 'RegisterLength': 8, 'Name': 'cld_lpf_en_m', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': '0NNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0) # cld_lpf disable
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dac_vddp_en_m', 'length': 1, 'registers': [{'REG': '0x19', 'POS': 4, 'RegisterName': 'Force registers 2', 'RegisterLength': 8, 'Name': 'cld_dac_vddp_en_m', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': '0NNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0) # cld_dac disable
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dac_en_m', 'length': 1, 'registers': [{'REG': '0x19', 'POS': 2, 'RegisterName': 'Force registers 2', 'RegisterLength': 8, 'Name': 'cld_dac_en_m', 'Mask': '0x4', 'Length': 1, 'FieldMSB': 2, 'FieldLSB': 2, 'Attribute': '0NNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0) # cld_dac disable
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dac_en_d_m', 'length': 1, 'registers': [{'REG': '0x19', 'POS': 3, 'RegisterName': 'Force registers 2', 'RegisterLength': 8, 'Name': 'cld_dac_en_d_m', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': '0NNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)  # cld_dac disable
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_drv_en_m', 'length': 1, 'registers': [{'REG': '0x19', 'POS': 1, 'RegisterName': 'Force registers 2', 'RegisterLength': 8, 'Name': 'cld_drv_en_m', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0NNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)  # cld_driver disable
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_bias_en_m', 'length': 1, 'registers': [{'REG': '0x19', 'POS': 0, 'RegisterName': 'Force registers 2', 'RegisterLength': 8, 'Name': 'cld_bias_en_m', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1) # cld_bias enable


I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_vmid_buf_en_force', 'length': 1, 'registers': [{'REG': '0x1A', 'POS': 6, 'RegisterName': 'Force registers 3', 'RegisterLength': 8, 'Name': 'cld_vmid_buf_en_force', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]} , write_value=0x1)  # Enable vmid_buff force

'''
Wait for the time needed for vmid to charge. 
Suppose Cmid=10uF
Buffer output resistance is 40 Ohm. Time constant is 10uFx40Ohm=400us.
Settling time is about 5tau=2ms
''' 
# Step 3
sleep(0.002) #5tau
expected_value = 1.85
error_spread = expected_value*0.0054 #10mV error
measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=expected_value, error_spread=error_spread)

print(f'Measured DAC 0p9V voltage reference value at "IODATA1" wrt "ADDR": {measured_value}')