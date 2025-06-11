from dfttools import *
from time import sleep
import random

Test_Name = 'CLD DRIVER INTERNAL RAIL_1'
from Procedures import Startup
# from Procedures import Playback suppose this procedure will be available

print(f'............ {Test_Name} ........')



# Define device address (replace with actual address)
# "0x68" = 0xXX  # Example device address, update accordingly


I2C_WRITE(device_address="0x68", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x03)
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'cld_driver_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 2, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'cld_driver_test_en', 'Mask': '0x4', 'Length': 1, 'FieldMSB': 2, 'FieldLSB': 2, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1) 
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '00000NNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '00000NNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)



# Wait a short time for signals to stabilize
sleep(0.001)  # 1 ms

# Step 3: Measure the voltage at "IODATA1" and "ADDR"
expected_value = 450e-3  # expected value is 450mV
error_spread = expected_value * 0.05  # 5% error spread
measured_value = VMEASURE(signal="IODATA1", reference="ADDR", expected_value=expected_value, error_spread=error_spread)

print(f'Expected  voltage at "IODATA1" wrt "ADDR": {expected_value /  1e-3} mV')
print(f'Expected  voltage at "IODATA1" wrt "ADDR": {measured_value /  1e-3} mV')