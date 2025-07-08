from dfttools import *
from time import sleep

Test_Name = 'PAD_TEST_VO'
from Procedures import Startup
print(f'............ {Test_Name} ........')
# designers must go through the details and correct the procedure
'''
Procedure 
    1.Startup (it includes enable of test page)
    2.Global_en to turn on the island
    2.Enable of write test mode of all pads except I2C ones
    3.Check the result
'''

# Set {'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]} to 1
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)

# Switch to page 1
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)

# Enable of write test mode
I2C_REG_WRITE( device_address="0x38", register_address=0x00, write_value=0x09,PageNo=1)

# Set all pads to 1
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'io_tst_wr', 'length': 5, 'registers': [{'REG': '0x01', 'POS': 0, 'RegisterName': 'IO_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'io_tst_wr[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': '000NNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1F)

# Sink 2mA from "ADDR"/"IODATA1"/"IOCLK1"/"IODATA0"/"IOCLK0"/
AFORCE(signal="ADDR",reference="GND",value=-0.002)
AFORCE(signal="IODATA1",reference="GND",value=-0.002)
AFORCE(signal="IOCLK1",reference="GND",value=-0.002)
AFORCE(signal="IODATA0",reference="GND",value=-0.002)
AFORCE(signal="IOCLK0",reference="GND",value=-0.002)

# Measure "ADDR" voltgae
VB0 = VMEASURE(signal="ADDR", reference="GND", expected_value=1.8,error_spread=0)

# Measure "IODATA1" voltgae
VB1 = VMEASURE(signal="IODATA1", reference="GND", expected_value=1.8,error_spread=0)

# Measure "IOCLK1" voltgae
VB2 = VMEASURE(signal="IOCLK1", reference="GND", expected_value=1.8,error_spread=0)

# Measure "IODATA0" voltgae
VB3 = VMEASURE(signal="IODATA0", reference="GND", expected_value=1.8,error_spread=0)

# Measure "IOCLK0" voltgae
VB4 = VMEASURE(signal="IOCLK0", reference="GND", expected_value=1.8,error_spread=0)

Vpad_min=1.2
Vpad_max=1.8

if Vpad_min <= VB0 <= Vpad_max:
  print(f'............ {Test_Name} VB0 VOH Passed ........')

if Vpad_min <= VB1 <= Vpad_max:
  print(f'............ {Test_Name} VB1 VOH Passed ........')
    
if Vpad_min <= VB2 <= Vpad_max:
  print(f'............ {Test_Name} VB2 VOH Passed ........')
  
if Vpad_min <= VB3 <= Vpad_max:
  print(f'............ {Test_Name} VB3 VOH Passed ........')  
  
if Vpad_min <= VB4 <= Vpad_max:
  print(f'............ {Test_Name} VB4 VOH Passed ........')

#################################

# Set all pads to 0
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'io_tst_wr', 'length': 5, 'registers': [{'REG': '0x01', 'POS': 0, 'RegisterName': 'IO_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'io_tst_wr[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': '000NNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x00)

# Source 2mA from "ADDR"/"IODATA1"/"IOCLK1"/"IODATA0"/"IOCLK0"/
AFORCE(signal="ADDR",reference="GND",value=0.002)
AFORCE(signal="IODATA1",reference="GND",value=0.002)
AFORCE(signal="IOCLK1",reference="GND",value=0.002)
AFORCE(signal="IODATA0",reference="GND",value=0.002)
AFORCE(signal="IOCLK0",reference="GND",value=0.002)

# Measure "ADDR" voltgae
VB0 = VMEASURE(signal="ADDR", reference="GND", expected_value=0,error_spread=0)

# Measure "IODATA1" voltgae
VB1 = VMEASURE(signal="IODATA1", reference="GND", expected_value=0,error_spread=0)

# Measure "IOCLK1" voltgae
VB2 = VMEASURE(signal="IOCLK1", reference="GND", expected_value=0,error_spread=0)

# Measure "IODATA0" voltgae
VB3 = VMEASURE(signal="IODATA0", reference="GND", expected_value=0,error_spread=0)

# Measure "IOCLK0" voltgae
VB4 = VMEASURE(signal="IOCLK0", reference="GND", expected_value=0,error_spread=0)

Vpad_min=0
Vpad_max=0.3

if Vpad_min <= VB0 <= Vpad_max:
  print(f'............ {Test_Name} VB0 VOL Passed ........')

if Vpad_min <= VB1 <= Vpad_max:
  print(f'............ {Test_Name} VB1 VOL Passed ........')
    
if Vpad_min <= VB2 <= Vpad_max:
  print(f'............ {Test_Name} VB2 VOL Passed ........')
  
if Vpad_min <= VB3 <= Vpad_max:
  print(f'............ {Test_Name} VB3 VOL Passed ........')  
  
if Vpad_min <= VB4 <= Vpad_max:
  print(f'............ {Test_Name} VB4 VOL Passed ........')

