from dfttools import *
from time import sleep

from Procedures.Startup import startup
from Procedures.Global_enable import global_enable

from Procedures.utils import complement,dec_to_2complement
def samples_average(fields=None, samples=8, sleep_time=5e-3):
    if fields is None:
        fields = []
    no_fields = len(fields)
    if no_fields == 0:
        return []
    # Initialize data with zeros for each field
    data = [0] * no_fields
    for i in range(samples):
        for field_no in range(no_fields):
            field = fields[field_no].get('field', {})
            expected_value = fields[field_no].get('expected_value', 0xffff)
            raw_data = I2C_READ("0x38", field_info=field, expected_value=expected_value)
            data[field_no] += raw_data
        sleep(sleep_time)
    # Correct averaging: divide by samples (right-shift by log2(samples))
    shift_amount = samples.bit_length() - 1  # For samples=8, shift=3
    for field_no in range(no_fields):
        data[field_no] = data[field_no] >> shift_amount
    return data
def vbat_gpadc_gain_offset_cal(data:{}):
    VBAT_LSB=5.5/(2**10 -1)
    vbat_gain_otp_length = {'fieldname': 'otp_sar_gain_vbat', 'length': 8, 'registers': [{'REG': '0xC2', 'POS': 0, 'RegisterName': 'OTP FIELDS 18 - TRACEABILITY 6', 'RegisterLength': 8, 'Name': 'otp_sar_gain_vbat[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}.get( 'length',8)
    vbat_offset_otp_length = {'fieldname': 'otp_sar_offs', 'length': 10, 'registers': [{'REG': '0xBF', 'POS': 4, 'RegisterName': 'OTP FIELDS 15 - TRACEABILITY 3', 'RegisterLength': 8, 'Name': 'otp_sar_offs[9:8]', 'Mask': '0x30', 'Length': 2, 'FieldMSB': 9, 'FieldLSB': 8, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xC1', 'POS': 0, 'RegisterName': 'OTP FIELDS 17 - TRACEABILITY 5', 'RegisterLength': 8, 'Name': 'otp_sar_offs[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}.get( 'length',8)
    VB1 = data.get('VB1')
    VB0 = data.get('VB0')
    CODE1 = data.get('CODE1')
    CODE0 = data.get('CODE0')
    vbat_gain=(VB1-VB0)/(CODE1-CODE0)
    vbat_off=round((VB0/vbat_gain)-CODE0)
    vbat_gain_correction_scaled=round((vbat_gain/VBAT_LSB-1)*1024)
    # complement the value 
    vbat_gain_otp_code = dec_to_2complement(vbat_gain_correction_scaled,vbat_gain_otp_length,False)
    vbat_offset_otp_code = dec_to_2complement(vbat_off,vbat_offset_otp_length,False)
    return {'vbat_gain':vbat_gain,'vbat_off':vbat_off,'vbat_gain_otp_code':vbat_gain_otp_code,'vbat_offset_otp_code':vbat_offset_otp_code}



def gpadc_vbat_gain_off_trim():
    Test_Name = 'GPADC_Vbat_Gain__Off_Trim'
    print(f'............ {Test_Name} ........')
    startup()
    global_enable()
    # designers must go through the details and correct the procedure
    '''
    Procedure 
        before to start the bandgap has to be trimmed
        1.Enable the SAR ADC with extenal clock
        2.Force VBAT at 2.8 V
        3.Measure VBAT and save the result in Variable VB0
        4.Measure the Vbat register after 8 average save in the Variable CODE0
        5.Force Vbat at 4.8 V
        6.Measure VBAT and save the result in Variable VB1
        7.Measure the Vbat register after 8 average save in the Variable CODE1
        8.Define m=(VB1-VB0)/(CODE1-CODE0)
        9.Dedine mid=5.3763441E-03
        10.Define vbat_off=VB0/m-CODE0
        11.Define Gaincorr=m/mid
        12.Define Vbat_gain_corr= (m/mid-1)*1024


    '''
    FREQFORCE(signal="IOCLK0",reference="GND",value=3.072e6)   # force clock 
    I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x00,PageNo=0) # page 0
    sleep(0.001)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vbat_filt', 'length': 6, 'registers': [{'REG': '0xD8', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vbat_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x00)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vtemp_filt', 'length': 6, 'registers': [{'REG': '0xD9', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vtemp_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x20', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x20)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'sar_vbat_avg_sel', 'length': 2, 'registers': [{'REG': '0xDE', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'sar_vbat_avg_sel[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x0F', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x3)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_en', 'length': 1, 'registers': [{'REG': '0xDF', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NPPPNNNN', 'Default': '0x03', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_refcomp_sel', 'length': 1, 'registers': [{'REG': '0xD6', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_refcomp_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x01', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
    VB0 = VFORCE(signal="PVDD", reference="GND", value=2.8,error_spread=0)
    sleep(0.1)
    mid=5.3763441E-03

    CODE0=I2C_READ(device_address="0x38",field_info={'fieldname': 'vbat_meas', 'length': 10, 'registers': [{'REG': '0x23', 'POS': 0, 'RegisterName': 'VBAT measurement reg 1', 'RegisterLength': 8, 'Name': 'vbat_meas[9:8]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 9, 'FieldLSB': 8, 'Attribute': '000000RR', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x24', 'POS': 0, 'RegisterName': 'VBAT measurement reg 2', 'RegisterLength': 8, 'Name': 'vbat_meas[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]},expected_value=0x1FE)
    VB1 = VFORCE(signal="PVDD", reference="GND", value=4.8,error_spread=0)
    sleep(0.1)


    CODE1=I2C_READ(device_address="0x38",field_info={'fieldname': 'vbat_meas', 'length': 10, 'registers': [{'REG': '0x23', 'POS': 0, 'RegisterName': 'VBAT measurement reg 1', 'RegisterLength': 8, 'Name': 'vbat_meas[9:8]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 9, 'FieldLSB': 8, 'Attribute': '000000RR', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x24', 'POS': 0, 'RegisterName': 'VBAT measurement reg 2', 'RegisterLength': 8, 'Name': 'vbat_meas[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]},expected_value=0x380)

    mreal=(VB1-VB0)/(CODE1-CODE0)
    vbat_off=int((VB0/mreal)-CODE0)

    vbat_gain=int((mreal/mid-1)*1024)
    # complement the value 
    otp_vbat_gain = 0x100 + vbat_gain if vbat_gain < 0 else vbat_gain
    otp_vbat_off = 0x400+vbat_off if vbat_off <0 else vbat_off
    print(f'............ {Test_Name} Passed ........')
        # write the optimized code if the trim passed
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=1)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_sar_offs', 'length': 10, 'registers': [{'REG': '0xBF', 'POS': 4, 'RegisterName': 'OTP FIELDS 15 - TRACEABILITY 3', 'RegisterLength': 8, 'Name': 'otp_sar_offs[9:8]', 'Mask': '0x30', 'Length': 2, 'FieldMSB': 9, 'FieldLSB': 8, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xC1', 'POS': 0, 'RegisterName': 'OTP FIELDS 17 - TRACEABILITY 5', 'RegisterLength': 8, 'Name': 'otp_sar_offs[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=vbat_off)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_sar_gain_vbat', 'length': 8, 'registers': [{'REG': '0xC2', 'POS': 0, 'RegisterName': 'OTP FIELDS 18 - TRACEABILITY 6', 'RegisterLength': 8, 'Name': 'otp_sar_gain_vbat[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=hex(otp_vbat_gain))

   
    print(f"Optimal gain Code: {hex(otp_vbat_gain)}")
    print(f"Optimal offset Code: {hex(vbat_off)}")

    sleep(0.001)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vbat_filt', 'length': 6, 'registers': [{'REG': '0xD8', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vbat_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vtemp_filt', 'length': 6, 'registers': [{'REG': '0xD9', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vtemp_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x20', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'sar_vbat_avg_sel', 'length': 2, 'registers': [{'REG': '0xDE', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'sar_vbat_avg_sel[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x0F', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'temp_duty_cycle', 'length': 4, 'registers': [{'REG': '0xDA', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'temp_duty_cycle[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x01', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
    FREQFORCE(signal="IOCLK0",reference="GND",value=float('Inf')) # disable the clock at the end of the test 

if __name__ == '__main__':
    gpadc_vbat_gain_off_trim()