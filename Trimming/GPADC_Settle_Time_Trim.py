from dfttools import *
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from time import sleep
def gpadc_settle_time_trim():
    Test_Name = 'GPADC_Settle_Time_Trim'
    print(f'............ {Test_Name} ........')
    # designers must go through the details and correct the procedure
    startup()
    global_enable()
    '''
    Procedure 
        before to start the bandgap has to be trimmed
        1.Enable the SAR ADC 
        2.Wait 100us
        3.Set ds_gpadc_del_comp_vddd<3:0>  to 1111 
        4.ds_gpadc_del_comp_en_vddd  at 1 
        5.measure the frequency of the signal dd_gpadc_tb_delay_clock_dvdd 
        6.Decrease the bus value ds_gpadc_del_comp_vddd<3:0> till the frequency measured is > of 9.09MHz.  
        7.Store the ds_gpadc_del_comp_vddd<3:0> -1  in the OTP register 
    '''
    # Enabling test page
    I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x00,PageNo=0) # page 0
    sleep(0.001)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vbat_filt', 'length': 6, 'registers': [{'REG': '0xD8', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vbat_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x10)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vtemp_filt', 'length': 6, 'registers': [{'REG': '0xD9', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vtemp_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x10)
    I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1) # page 1
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_ds_gpadc_del_comp', 'length': 4, 'registers': [{'REG': '0xB4', 'POS': 0, 'RegisterName': 'OTP FIELDS 4', 'RegisterLength': 8, 'Name': 'otp_ds_gpadc_del_comp[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x04', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0xF)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x4)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x11)
    I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x00,PageNo=0) # page 0
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_en', 'length': 1, 'registers': [{'REG': '0xDF', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NPPPNNNN', 'Default': '0x01', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
    sleep(0.001)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_del_comp_en', 'length': 1, 'registers': [{'REG': '0xD6', 'POS': 2, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_del_comp_en', 'Mask': '0x4', 'Length': 1, 'FieldMSB': 2, 'FieldLSB': 2, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
    I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1) # page 1

    # select the mux to bring out the ana_dd_gpadc_tb_delay_clock_dvdd signal on "IOCLK1"
    # the frequency measured is > of 9.09MHz.  
    # desingers needs to correct the assumptions
    limit_percentage = 0.1 # assuming 
    target_value = 4.761e6 # 4.761MHz
    # higher and lower limits taken about +/- 10% of the target value 
    lower_limit = target_value-target_value*limit_percentage
    higher_limit = target_value+target_value*limit_percentage
    error_spread = target_value*0.05 # 5% of target value

    # LSB is the assumption designer needs to correct
    # Step size
    step_size = 580e3 # assumed 580kHz

    # Initialize minimum error and optimal code
    min_error = float('inf')
    optimal_code = None
    optimal_measured_value = None
    num_steps = 2**4-1 # trimming field is 4 bit
    for i in range(num_steps,-1,-1):
        # sweep trimg code
        I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_ds_gpadc_del_comp', 'length': 4, 'registers': [{'REG': '0xB4', 'POS': 0, 'RegisterName': 'OTP FIELDS 4', 'RegisterLength': 8, 'Name': 'otp_ds_gpadc_del_comp[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x04', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=hex(i))
        # Generate monotonic values with step size
        expected_value = higher_limit - i * step_size 
        # Add white noise to the expected value
        # Pass the noisy value as the expected measurement values
        measured_value = FREQMEASURE(signal="IOCLK1", reference="GND", expected_value=expected_value, error_spread=error_spread)
        error = abs(measured_value - target_value)/abs(target_value) *100
        if error < min_error:
            min_error = error
            optimal_code = hex(i)
            optimal_measured_value = measured_value
        sleep(0.1)
    # Check for limits
    if lower_limit < optimal_measured_value < higher_limit:
        print(f'............ {Test_Name} Passed ........')
        # write the optimized code if the trim passed
        I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_ds_gpadc_del_comp', 'length': 4, 'registers': [{'REG': '0xB4', 'POS': 0, 'RegisterName': 'OTP FIELDS 4', 'RegisterLength': 8, 'Name': 'otp_ds_gpadc_del_comp[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x04', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=optimal_code)
    else:
        print(f'............ {Test_Name} Failed ........')
        # if the trimh failed program detult zero
        I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_ds_gpadc_del_comp', 'length': 4, 'registers': [{'REG': '0xB4', 'POS': 0, 'RegisterName': 'OTP FIELDS 4', 'RegisterLength': 8, 'Name': 'otp_ds_gpadc_del_comp[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x04', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    print(f"Optimal Code: {optimal_code}")
    print(f"Optimal measured value : {optimal_measured_value}Hz, Target vlaue : {target_value}Hz")
    print(f"Minimum Error: {min_error}")
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vbat_filt', 'length': 6, 'registers': [{'REG': '0xD8', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vbat_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x10)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vtemp_filt', 'length': 6, 'registers': [{'REG': '0xD9', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vtemp_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x10)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_del_comp_en', 'length': 1, 'registers': [{'REG': '0xD6', 'POS': 2, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_del_comp_en', 'Mask': '0x4', 'Length': 1, 'FieldMSB': 2, 'FieldLSB': 2, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_en', 'length': 1, 'registers': [{'REG': '0xDF', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NPPPNNNN', 'Default': '0x01', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)


if __name__ == '__main__':
    gpadc_settle_time_trim()