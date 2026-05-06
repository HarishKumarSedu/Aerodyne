from dfttools import *

def initialization():
    testname = 'Initialization'
    print('*' * ((30 - len(testname)) // 2) + testname + '*' * ((30 - len(testname) + 1) // 2)) # do not bother too much about it will just align the test in between
    VFORCE(signal="VDD",reference="GND",value=1.8)
    VFORCE(signal="RESETB",reference="GND",value=1.8)
    VFORCE(signal="PVDD",reference="GND",value=3.7)
    I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x00,PageNo=0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_mode', 'length': 2, 'registers': [{'REG': '0x84', 'POS': 6, 'RegisterName': 'PLL_REG_5', 'RegisterLength': 8, 'Name': 'pll_mode[1:0]', 'Mask': '0xC0', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x17', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x2)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_ldet_cnt', 'length': 5, 'registers': [{'REG': '0x83', 'POS': 0, 'RegisterName': 'PLL reg 4', 'RegisterLength': 8, 'Name': 'pll_ldet_cnt[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': '000NNNNN', 'Default': '0x00', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x10)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'tdm_fsyn_mnt_mode', 'length': 2, 'registers': [{'REG': '0x4E', 'POS': 4, 'RegisterName': 'TDM settings 13', 'RegisterLength': 8, 'Name': 'tdm_fsyn_mnt_mode[1:0]', 'Mask': '0x30', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x99', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'prechg_step_time', 'length': 2, 'registers': [{'REG': '0x2D', 'POS': 2, 'RegisterName': 'Sequencer settings 2', 'RegisterLength': 8, 'Name': 'prechg_step_time[1:0]', 'Mask': '0xC', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x58', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x2)
    I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1)
    # Unlock test page 
    I2C_REG_WRITE( device_address="0x38", register_address=0x2F, write_value=0xAA,PageNo=1)
    I2C_REG_WRITE( device_address="0x38", register_address=0x2F, write_value=0xBB,PageNo=1)
if __name__ == '__main__':
    initialization()