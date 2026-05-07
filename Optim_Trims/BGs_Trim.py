from dfttools import *

def bgs_trim():
    test_name = 'BGs_Trim'
    print(f'............ {test_name} ........')
    I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1) # page 1
    # Enabling analog TMUX
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_vos_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 7, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_vos_buff', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
    tests = {
        'BG_1V2' : {'target':1.2, 'testsel_code':4,'otp_field':{'fieldname': 'otp_ds_ref_bg_trm_1v2', 'length': 4, 'registers': [{'REG': '0xB1', 'POS': 0, 'RegisterName': 'OTP FIELDS 1', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_trm_1v2[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x80', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}},
        'BG_0V9' : {'target':0.9, 'testsel_code':5,'otp_field':{'fieldname': 'otp_ds_ref_bg_trm_0v9', 'length': 4, 'registers': [{'REG': '0xB0', 'POS': 4, 'RegisterName': 'OTP FIELDS 0', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_trm_0v9[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}},
        'BG_0V6' : {'target':0.6, 'testsel_code':6,'otp_field':{'fieldname': 'otp_ds_ref_bg_trm_0v6', 'length': 4, 'registers': [{'REG': '0xB0', 'POS': 0, 'RegisterName': 'OTP FIELDS 0', 'RegisterLength': 8, 'Name': 'otp_ds_ref_bg_trm_0v6[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}},
    }
    lsb_v = 7.57e-3 # 7.57mV
    num_bits=4
    percentage = 2.5e-2 # 2.5% deviation
    min_code    = -(2 ** (num_bits - 1))        # e.g. -8  for 4-bit
    max_code    =  (2 ** (num_bits - 1)) - 1    # e.g. +7  for 4-bit
    data={}
    for test_name, test_values in tests.items():
        target = test_values['target']
        testsel_code = test_values['testsel_code']
        otp_field = test_values['otp_field']
        min_error = float('inf')
        ######################### OFFSET MEASURMENT ##########
        I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x4) # PROGRAM THE TEST SEL CODE 
        buf_forced_voltage=VFORCE(signal="ADDR", reference="GND", value=target, error_spread=lsb_v/2)
        buf_measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=target, error_spread=lsb_v/2)
        buffer_offset = abs(buf_measured_value - buf_forced_voltage)
        print(f"{test_name} : BUFFER OFFSET : {buffer_offset} V")
        # REMOVE THE VOLTAGE FORCING 
        VFORCE(signal="ADDR", reference="GND", value=float('Inf'))
        ######################### OFFSET MEASURMENT FINISH ##
        pretrim_bg_measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=target,error_spread=3*lsb_v) - buffer_offset
        ############### Trim code esitmation ################
        delta_v     = target - pretrim_bg_measured_value          
        raw_steps   = delta_v / lsb_v               # float steps needed
        trim_code   = -round(raw_steps)              # standard rounding
        ############### Check for the Trim code range #######
        if trim_code < min_code or trim_code > max_code:
            raise RuntimeError(f"  [WARNING] Required steps ({trim_code}) out of range "
                  f"[{min_code}, {max_code}] — clamping!")
            trim_code = max(min_code, min(max_code, trim_code))
        otp_trim_code = 2**num_bits + trim_code if trim_code <0 else trim_code
        I2C_WRITE(device_address="0x38",field_info=otp_field,write_value=otp_trim_code)
        posttrim_bg_measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=target,error_spread=lsb_v/2) - buffer_offset
        min_error = (posttrim_bg_measured_value - target) /  target *100
        ############### LIMIT CHECK #######################
        lower_limit = target - target*percentage
        higher_limit = target + target*percentage
        if lower_limit < posttrim_bg_measured_value < higher_limit:
            print(f'{test_name} PASSED !!!')
        else:
            # if the trimh failed program default zero
            raise RuntimeError(f'{test_name} PASSED !!!')
            # WRITE DEFAULT
            I2C_WRITE(device_address="0x38",field_info=otp_field,write_value=0)
        ############### DATA LOGGING ########################
        print(f'TEST-NAME  : {test_name} ')
        print(f'PRE -TRIM  : {pretrim_bg_measured_value:.6f} V')
        print(f"OTP CODE   : {otp_trim_code:#02X}")
        print(f'POST -TRIM : {posttrim_bg_measured_value:.6f} V')
        print(f'TARGET     : {target:.6f} V')
        print(f"ERROR      : {min_error:.6f} %")
        data[test_name] = {
            'target':target,
            'testsel_code':testsel_code,
            'pretrim_bg_measured_value':pretrim_bg_measured_value,
            'buffer_offset':buffer_offset,
            'lower_limit':lower_limit,
            'higher_limit':higher_limit,
            'otp_trim_code':otp_trim_code,
            'posttrim_bg_measured_value':posttrim_bg_measured_value,
            'error_%':min_error
        }
    ############### SELF-REG LDO 1.2v ########################
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_vos_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 7, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_vos_buff', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    LDO_LSB = 15.14e-3
    min_error = float('inf')
    LDO_TARGET = 1.2
    LDO_ERROR_PERCENTAGE = 1e-2
    test_name='SELF_REG_LDO_1V2'
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0xC) # PROGRAM THE TEST SEL CODE 
    pretrim_ldo_measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=LDO_TARGET,error_spread=3*LDO_LSB)
    ############### Trim code esitmation ################
    delta_v     = LDO_TARGET - pretrim_ldo_measured_value          
    raw_steps   = delta_v / LDO_LSB               # float steps needed
    trim_code   = -round(raw_steps)              # standard rounding
    print(pretrim_ldo_measured_value)
    ############### Check for the Trim code range #######
    if trim_code < min_code or trim_code > max_code:
        raise RuntimeError(f"  [WARNING] Required steps ({trim_code}) out of range "
                           f"[{min_code}, {max_code}] — clamping!")
        trim_code = max(min_code, min(max_code, trim_code))
    otp_trim_code = 2**num_bits + trim_code if trim_code <0 else trim_code
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_ds_ref_self_ref_trm_0v4', 'length': 4, 'registers': [{'REG': '0xCD', 'POS': 0, 'RegisterName': 'OTP FIELDS 29', 'RegisterLength': 8, 'Name': 'otp_ds_ref_self_ref_trm_0v4[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=otp_trim_code)
    posttrim_ldo_measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=LDO_TARGET,error_spread=LDO_LSB/2)
    ############### LIMIT CHECK #######################
    lower_limit = LDO_TARGET - LDO_TARGET*LDO_ERROR_PERCENTAGE
    higher_limit = LDO_TARGET + LDO_TARGET*LDO_ERROR_PERCENTAGE
    if lower_limit < posttrim_ldo_measured_value < higher_limit:
        print(f'{test_name} PASSED !!!')
    else:
        # if the trimh failed program default zero
        raise RuntimeError(f'{test_name} PASSED !!!')
        # WRITE DEFAULT
        I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_ds_ref_self_ref_trm_0v4', 'length': 4, 'registers': [{'REG': '0xCD', 'POS': 0, 'RegisterName': 'OTP FIELDS 29', 'RegisterLength': 8, 'Name': 'otp_ds_ref_self_ref_trm_0v4[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0)
    print(f'TEST-NAME  : {test_name} ')
    print(f'PRE -TRIM  : {pretrim_ldo_measured_value:.6f} V')
    print(f"OTP CODE   : {otp_trim_code:#02X}")
    print(f'POST -TRIM : {posttrim_ldo_measured_value:.6f} V')
    print(f'TARGET     : {LDO_TARGET:.6f} V')
    print(f"ERROR      : {min_error:.6f} %")
    data[test_name] = {
            'target':LDO_TARGET,
            'testsel_code':0xC,
            'pretrim_ldo_measured_value':pretrim_ldo_measured_value,
            'lower_limit':lower_limit,
            'higher_limit':higher_limit,
            'otp_trim_code':otp_trim_code,
            'posttrim_ldo_measured_value':posttrim_ldo_measured_value,
            'error_%':min_error
        }
    ############### CLEANUP ########################
    VMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf'),comments='Remove Multimeter')
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_vos_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 7, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_vos_buff', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en_buff', 'length': 1, 'registers': [{'REG': '0x10', 'POS': 6, 'RegisterName': 'FORCING_REG_2', 'RegisterLength': 8, 'Name': 'ref_test_en_buff', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    return data
if __name__ == '__main__':
    data = bgs_trim()
    print(data)