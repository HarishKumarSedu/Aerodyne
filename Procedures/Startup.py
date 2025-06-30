Test_Name = 'Startup'
print(f'............ {Test_Name} ........')
from dfttools import *
from time import sleep

VFORCE(signal="VDD",reference="GND",value=1.8)
VFORCE(signal="RESETB",reference="GND",value=1.8)
VFORCE(signal="PVDD",reference="GND",value=3.7)

sleep(0.001)

I2C_WRITE(device_address="0x38",field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)




