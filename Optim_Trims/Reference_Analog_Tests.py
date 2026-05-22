from dfttools import *
def limit_check(target:0.0,measured:0.0,error_percentage:0.0):
    lower_limit = target - target*error_percentage
    higher_limit = target + target*error_percentage
    if measured < lower_limit or measured > higher_limit:
        raise RuntimeError(f'FAIL ! , measured : {measured}, higherlimit : {higher_limit:.7f}, lowerlimit : {lower_limit:.7f}')
    else:
        print('Limits PASS!.')
def ref_analog_tests():
    test_name = 'BGs_Trim'
    print(f'............ {test_name} ........')
    BUFFER_VOLTAGE_TESTS = {
        'PVDD_UVLO' : {'target':0.4, 'testsel_code':1,'error%':10e-3,},
        'BG_0V4' : {'target':0.6, 'testsel_code':7,'error%':4e-3},
    }
    VOLTAGE_TESTS = {
        'ANALDO_FEEDBACK' : {'target':0.461, 'testsel_code':2,'error%':5e-3,},
        'SELF_LDO_1P2V_AON' : {'target':1.2, 'testsel_code':11,'error%':5e-3},
    }
    CURRENT_TESTS = {
        'BG_CURRENT' : {'target':800E-9, 'testsel_code':8,'error%':15e-3,},
        'DIG_LDO_CURRENT' : {'target':500E-9, 'testsel_code':13,'error%':5e-3},
    }
    # BUFFERED MEASURED VOLTAGES
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_vos_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 7, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_vos_buff', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
    for testname, test_values in BUFFER_VOLTAGE_TESTS.items():
        testsel_code = test_values.get('test_values',0)
        target = test_values.get('target',0)
        erro_percentage = test_values.get('error%',0)
        I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=testsel_code) # PROGRAM THE TEST SEL CODE 
        buf_forced_voltage=VFORCE(signal="ADDR", reference="GND", value=target, error_spread=1e-3) #1mV off measurement error
        buf_measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=target, error_spread=1e-3)
        buffer_offset = abs(buf_measured_value - buf_forced_voltage)
        # REMOVE THE VOLTAGE FORCING 
        VFORCE(signal="ADDR", reference="GND", value=float('Inf'))
        targeted_measured_v = VMEASURE(signal="IODATA1", reference="GND", expected_value=target,error_spread=1e-3) - buffer_offset
        ############### LOG THE RESULTS ##################
        print(f'REFERENCE TEST {testname} RESULTS :~')
        print(f"BUFFER OFFSET : {buffer_offset} V")
        print(f"TARGET {target:.7F} V : MEASURED {targeted_measured_v:.7F} V")
        print(f'REFERENCE TEST {testname} LIMIT CHECK :~')
        limit_check(target,targeted_measured_v,erro_percentage)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_vos_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 7, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_vos_buff', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    # NON BUFFERED MEASURED VOLTAGES
    for testname, test_values in VOLTAGE_TESTS.items():
        testsel_code = test_values.get('test_values',0)
        target = test_values.get('target',0)
        erro_percentage = test_values.get('error%',0)
        I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=testsel_code) # PROGRAM THE TEST SEL CODE 
        targeted_measured_v = VMEASURE(signal="IODATA1", reference="GND", expected_value=target,error_spread=1e-3) 
        ############### LOG THE RESULTS ##################
        print(f'REFERENCE TEST {testname} RESULTS :~')
        print(f"TARGET {target:.7F} V : MEASURED {targeted_measured_v:.7F} V")
        print(f'REFERENCE TEST {testname} LIMIT CHECK :~')
        limit_check(target,targeted_measured_v,erro_percentage)
    VMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf'))
    # CURRENT MEASURE TESTS
    for testname, test_values in CURRENT_TESTS.items():
        testsel_code = test_values.get('test_values',0)
        target = test_values.get('target',0)
        erro_percentage = test_values.get('error%',0)
        I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=testsel_code) # PROGRAM THE TEST SEL CODE 
        targeted_measured_a = AMEASURE(signal="IODATA1", reference="GND", expected_value=target,error_spread=1e-9) 
        ############### LOG THE RESULTS ##################
        print(f'REFERENCE TEST {testname} RESULTS :~')
        print(f"TARGET {target:.7F} A : MEASURED {targeted_measured_a:.7F} A")
        print(f'REFERENCE TEST {testname} LIMIT CHECK :~')
        limit_check(target,targeted_measured_a,erro_percentage)
    AMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf'))
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_vos_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 7, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_vos_buff', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
if __name__ == '__main__':
    ref_analog_tests()
        
        