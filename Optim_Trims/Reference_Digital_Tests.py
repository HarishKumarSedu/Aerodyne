from dfttools import *
def ref_digital_tests():
    Test_Name = 'REFERENCE DIGITAL TESTS '
    print(f'............ {Test_Name} ........')
    # Enabling test page
    I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1) # page 1
    #Enabling digital TMUX
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x21)

    LH= 1.8 # 1.8V
    Analdo_Trig_Status = VTRIG_LH(signal="IOCLK0", reference="GND", threshold=LH, expected_value=1.801)
    BG_READY_Trig_Status = VTRIG_LH(signal="IOCLK1", reference="GND", threshold=LH, expected_value=1.801)
    print(f'ANALDO COMPARATOR STATUS : {Analdo_Trig_Status}')
    print(f'BG_READY COMPARATOR STATUS : {BG_READY_Trig_Status}')
    VTRIG_LH(signal="IOCLK0", reference="GND", threshold=LH, expected_value=float('Inf'))# disconnect the scope
    VTRIG_LH(signal="IOCLK1", reference="GND", threshold=LH, expected_value=float('Inf'))# disconnect the scope
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x00)


if __name__ == '__main__':
  ref_digital_tests()

