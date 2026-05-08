from dfttools import *

def initialization():
    testname = 'Initialization'
    print('*' * ((30 - len(testname)) // 2) + testname + '*' * ((30 - len(testname) + 1) // 2)) # do not bother too much about it will just align the test in between
    VFORCE(signal="VDD",reference="GND",value=1.8)
    VFORCE(signal="RESETB",reference="GND",value=1.8)
    VFORCE(signal="PVDD",reference="GND",value=3.7)
    I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x00,PageNo=0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_ldet_cnt', 'length': 5, 'registers': [{'REG': '0x83', 'POS': 0, 'RegisterName': 'PLL reg 4', 'RegisterLength': 8, 'Name': 'pll_ldet_cnt[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': '000NNNNN', 'Default': '0x00', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x10)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'tdm_fsyn_mnt_mode', 'length': 2, 'registers': [{'REG': '0x4E', 'POS': 4, 'RegisterName': 'TDM settings 13', 'RegisterLength': 8, 'Name': 'tdm_fsyn_mnt_mode[1:0]', 'Mask': '0x30', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x99', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x1)
    I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1)
    # Unlock test page 
    I2C_REG_WRITE( device_address="0x38", register_address=0x2F, write_value=0xAA,PageNo=1)
    I2C_REG_WRITE( device_address="0x38", register_address=0x2F, write_value=0xBB,PageNo=1)
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'force_otp_clk_on', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 1, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'force_otp_clk_on', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'otp_burnt', 'length': 1, 'registers': [{'REG': '0xCF', 'POS': 7, 'RegisterName': 'OTP FIELDS 31', 'RegisterLength': 8, 'Name': 'otp_burnt', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x02', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
    
if __name__ == '__main__':
    initialization()