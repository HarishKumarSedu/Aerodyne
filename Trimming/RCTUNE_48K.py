from dfttools import *
from time import sleep

Test_Name = 'RCTUNE_48K'
from Procedures import Startup
print(f'............ {Test_Name} ........')
# designers must go through the details and correct the procedure
'''
Procedure 
    before to start the bandgap has to be trimmed
    1.Set 48KHz Family
    2.Run rctune procedure

'''
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
sleep(0.001)

I2C_WRITE(device_address="0x38",field_info={'fieldname': 'spk_en', 'length': 1, 'registers': [{'REG': '0x9F', 'POS': 0, 'RegisterName': 'Enables settings 5', 'RegisterLength': 8, 'Name': 'spk_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000S', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0) # {'fieldname': 'spk_en', 'length': 1, 'registers': [{'REG': '0x9F', 'POS': 0, 'RegisterName': 'Enables settings 5', 'RegisterLength': 8, 'Name': 'spk_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000S', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]} off
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'vis_rctun_sel', 'length': 1, 'registers': [{'REG': '0x60', 'POS': 3, 'RegisterName': 'VIS setting reg 0', 'RegisterLength': 8, 'Name': 'vis_rctun_sel', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x0C', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_clk12m_bypass', 'length': 1, 'registers': [{'REG': '0x80', 'POS': 3, 'RegisterName': 'PLL_REG_1', 'RegisterLength': 8, 'Name': 'pll_clk12m_bypass', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x21', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0) #use internal trimmed PLL signal

sleep(0.001)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'rc_tun_start', 'length': 1, 'registers': [{'REG': '0x62', 'POS': 0, 'RegisterName': 'VIS setting reg 2', 'RegisterLength': 8, 'Name': 'rc_tun_start', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000P', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
sleep(0.1) # wait at least 100us
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
rctune_48k = I2C_READ(device_address="0x38",field_info={'fieldname': 'otp_vis_rc_tun_48', 'length': 4, 'registers': [{'REG': '0xB2', 'POS': 4, 'RegisterName': 'OTP FIELDS 2', 'RegisterLength': 8, 'Name': 'otp_vis_rc_tun_48[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x84', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},expected_value=0x8)
print(f"Procedure finish")
print(f"{Test_Name} :> Code {hex(rctune_48k)}")

I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'vis_rctun_sel', 'length': 1, 'registers': [{'REG': '0x60', 'POS': 3, 'RegisterName': 'VIS setting reg 0', 'RegisterLength': 8, 'Name': 'vis_rctun_sel', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x0C', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
sleep(0.001)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)