from dfttools import *
from time import sleep
import random
# Newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
def Self_Reg_LDO_1V2_Trim():


    Test_Name = 'Self_Reg_LDO_1V2_Trim'
    from Procedures.Startup import startup
    from Procedures.Global_enable import global_enable
    print(f'............ {Test_Name} ........')
    startup()
    global_enable()
    typical_value = 1.2
    # Enabling test page
    I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1) # page 1

    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0xC)      
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
    '''
    Bring 1.2v self-regLDO voltage to "IODATA1" through the analog test mux and trim it to the closest value to 1.2V
    '''

    # Initial value
    percentage = 1e-2 # 1% difference
    
    low_value = typical_value - typical_value*percentage
    high_value = typical_value + typical_value*percentage

    
    # Step size
    step_size = 15.14e-3       # 15.14mV

    # Number of steps width of the field / bits
    num_bits = 4  # 4-bit

    # Standard deviation for white noise
    noise_std_dev = 0.025

    # Initialize minimum error and optimal code
    min_error = float('inf')
    optimal_code = None
    optimal_measured_value = None
    # 4bit :> sweep 8 to 15, 0 t0 7
    for i in list(list(range(2**num_bits//2, 2**num_bits))+list(range(0,2**num_bits//2))):
        # sweep trimg code
        I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_ds_ref_self_ref_trm_0v4', 'length': 4, 'registers': [{'REG': '0xCD', 'POS': 0, 'RegisterName': 'OTP FIELDS 29', 'RegisterLength': 8, 'Name': 'otp_ds_ref_self_ref_trm_0v4[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=hex(i))
        expected_value = low_value + i * step_size 
        # Add white noise to each value 
        measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=expected_value,error_spread=noise_std_dev)      
        error = abs(measured_value - typical_value)/abs(typical_value) *100
        if error < min_error:
            min_error = error
            optimal_code = hex(i)
            optimal_measured_value = measured_value
        sleep(0.01) # 1ms
    # Check for limits
    if low_value < optimal_measured_value < high_value:
        print(f'............ {Test_Name} Passed ........')
        # write the optimized code if the trim passed
        I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_ds_ref_self_ref_trm_0v4', 'length': 4, 'registers': [{'REG': '0xCD', 'POS': 0, 'RegisterName': 'OTP FIELDS 29', 'RegisterLength': 8, 'Name': 'otp_ds_ref_self_ref_trm_0v4[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=optimal_code)
    else:
        print(f'............ {Test_Name} Failed ........')
        raise RuntimeWarning(f'............ {Test_Name} Failed ........')
        # if the trimh failed program detult zero
        I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_ds_ref_self_ref_trm_0v4', 'length': 4, 'registers': [{'REG': '0xCD', 'POS': 0, 'RegisterName': 'OTP FIELDS 29', 'RegisterLength': 8, 'Name': 'otp_ds_ref_self_ref_trm_0v4[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'ref_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 7, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'ref_test_en', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    print(f"Optimal Code: {optimal_code}")
    print(f"Optimal measured value : {optimal_measured_value}V, Target value : {typical_value}V")
    print(f"Minimum Error: {min_error}%")


    return optimal_code,optimal_measured_value,min_error

if __name__ == '__main__':
    Self_Reg_LDO_1V2_Trim()