from dfttools import *
def limit_check(target:0.0,measured:0.0,error_percentage:0.0):
    lower_limit = target - target*error_percentage
    higher_limit = target + target*error_percentage
    if measured < lower_limit or measured > higher_limit:
        raise RuntimeError(f'FAIL ! , measured : {measured}, higherlimit : {higher_limit:.7f}, lowerlimit : {lower_limit:.7f}')
    else:
        print('Limits PASS!.')
def vis_analog_tests():
    test_name = 'VIs ANALOG TESTS'
    print(f'............ {test_name} ........')
    VOLTAGE_TESTS = {
        'VIS_1V5_REF' : {'target':1.5, 'testsel_code':1,'error%':0.33E-2,},
        'VIS_1V6_REF' : {'target':1.6, 'testsel_code':5,'error%':0.33E-2,},
    }
    CURRENT_TESTS = {
        'VIS_CURR1_1uA' : {'target':1E-6, 'testsel_code':8,'error%':15e-3,},
        'DIG_LDO_CURRENT' : {'target':0.5-6, 'testsel_code':13,'error%':5e-3},
    }
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0)  
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'spk_en', 'length': 1, 'registers': [{'REG': '0x9F', 'POS': 0, 'RegisterName': 'Enables settings 5', 'RegisterLength': 8, 'Name': 'spk_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000S', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)  # turn on the device after dac put down
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)  # Change page in regmap
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'vis_atp_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'vis_atp_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)  # Enable test mux
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)  
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)  

    for testname, test_values in VOLTAGE_TESTS.items():
        testsel_code = test_values.get('testsel_code',0)
        target = test_values.get('target',0)
        erro_percentage = test_values.get('error%',0)
        I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=testsel_code) # PROGRAM THE TEST SEL CODE 
        targeted_measured_v = VMEASURE(signal="IODATA1", reference="ADDR", expected_value=target,error_spread=1e-3) 
        ############### LOG THE RESULTS ##################
        print(f'VIS TEST {testname} RESULTS :~')
        print(f"TARGET {target:.7F} V : MEASURED {targeted_measured_v:.7F} V")
        print(f'VIS TEST {testname} LIMIT CHECK :~')
        limit_check(target,targeted_measured_v,erro_percentage)
    VMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf'))
    # CURRENT MEASURE TESTS
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=4)
    vis_curr1_1ua = AMEASURE(signal="IODATA1", reference="GND", expected_value=1E-6,error_spread=1e-9) 
    ############### LOG THE RESULTS ##################
    print(f'VIS TEST CURRENT1 1uA RESULTS :~')
    print(f"TARGET 1uA : MEASURED {vis_curr1_1ua/1e-6:.7F} A")
    print(f'VIS TEST  CURRENT1 1uA LIMIT CHECK :~')
    limit_check(1e-6,vis_curr1_1ua,10e-2)
    vis_curr1_0p5ua = AMEASURE(signal="ADDR", reference="GND", expected_value=0.5E-6,error_spread=1e-9) 
    ############### LOG THE RESULTS ##################
    print(f'VIS TEST CURRENT2 0.5uA RESULTS :~')
    print(f"TARGET 0.5uA : MEASURED {vis_curr1_0p5ua/1e-6:.7F} A")
    print(f'VIS TEST  CURRENT1 1uA LIMIT CHECK :~')
    limit_check(0.5e-6,vis_curr1_0p5ua,10e-2)
    AMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf'))
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'vis_atp_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'vis_atp_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)  # Enable test mux
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)  
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)  
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
if __name__ == '__main__':
    vis_analog_tests()
        
        