from dfttools import *
from time import sleep

Test_Name = 'V-RANDOMIZER SCAN'
from Procedures import Startup
print(f'............ {Test_Name} ........')
# designers must go through the details and correct the procedure
'''
Procedure 
    1.Startup (it includes enable of test page)
    2.Enable Vsense and go to play (to supply the Vsense ana block)
    3.Start scan for the V-randomizer
'''

# Switch to page 1
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)

# 2. Enable Vsense and go in play
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'vis_channel_v_en', 'length': 1, 'registers': [{'REG': '0xA7', 'POS': 0, 'RegisterName': 'Vis enables reg', 'RegisterLength': 8, 'Name': 'vis_channel_v_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '000000NN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'spk_en', 'length': 1, 'registers': [{'REG': '0x9F', 'POS': 0, 'RegisterName': 'Enables settings 5', 'RegisterLength': 8, 'Name': 'spk_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000S', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)

# 3. Enable scan
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'gpio0_di_en', 'length': 1, 'registers': [{'REG': '0x39', 'POS': 0, 'RegisterName': 'IODATA1 pad config', 'RegisterLength': 8, 'Name': 'gpio0_di_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NN00N0NN', 'Default': '0x00', 'User': '00YYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'scan_randomizer_v', 'length': 1, 'registers': [{'REG': '0x06', 'POS': 0, 'RegisterName': 'VIS RANDOMIZER SCAN Test', 'RegisterLength': 8, 'Name': 'scan_randomizer_v', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '000000NN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)