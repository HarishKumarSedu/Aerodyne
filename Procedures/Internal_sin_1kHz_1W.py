# set the internal sinusoildal generator at 1kHz 1W
Test_Name = 'Internal_sin_1kHz_1W'
print(f'............ {Test_Name} ........')
from dfttools import *

I2C_WRITE(device_address="0x68", field_info={'fieldname': 'internal_sin_gain', 'length': 4, 'registers': [{'REG': '0x1F', 'POS': 4, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_gain[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(2))  # 0dB sinus amplitude
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'internal_sin_freq', 'length': 3, 'registers': [{'REG': '0x1F', 'POS': 0, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_freq[2:0]', 'Mask': '0x7', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(2))  # 1kHz sinus wave
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'internal_sin_en', 'length': 1, 'registers': [{'REG': '0x1F', 'POS': 3, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_en', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(1))  # Enable internal sin generator
# use following code if you want to foce the clock
# signal is the pin at you want to apply clock with repsct to reference
# FREQFORCE(signal=,reference=,value=)