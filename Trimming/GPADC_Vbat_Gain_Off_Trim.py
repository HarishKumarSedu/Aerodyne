from dfttools import *
from time import sleep

Test_Name = 'GPADC_Vbat_Gain__Off_Trim'
from Procedures import Startup
from Procedures import Global_enable
print(f'............ {Test_Name} ........')
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
I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x00,PageNo=0) # page 0
sleep(0.001)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vbat_filt', 'length': 6, 'registers': [{'REG': '0xD8', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vbat_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x10)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vtemp_filt', 'length': 6, 'registers': [{'REG': '0xD9', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vtemp_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x10)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'sar_vbat_avg_sel', 'length': 2, 'registers': [{'REG': '0xDE', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'sar_vbat_avg_sel[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x3)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'temp_duty_cycle', 'length': 4, 'registers': [{'REG': '0xDA', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'temp_duty_cycle[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x01', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_clk12m_bypass', 'length': 1, 'registers': [{'REG': '0x80', 'POS': 3, 'RegisterName': 'PLL_REG_1', 'RegisterLength': 8, 'Name': 'pll_clk12m_bypass', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x21', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_en', 'length': 1, 'registers': [{'REG': '0xDF', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NPPPNNNN', 'Default': '0x01', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
pvdd_forced_voltage = VFORCE(signal="PVDD", reference="GND", value=2.8,error_spread=0)
sleep(0.01)
VB0 = VMEASURE(signal="PVDD", reference="GND", expected_value=2.8,error_spread=0)
sleep(0.001)
mid=5.3763441E-03

HCODE0=I2C_READ(device_address="0x38",field_info={'fieldname': 'vbat_meas', 'length': 10, 'registers': [{'REG': '0x23', 'POS': 0, 'RegisterName': 'VBAT measurement reg 1', 'RegisterLength': 8, 'Name': 'vbat_meas[9:8]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 9, 'FieldLSB': 8, 'Attribute': '000000RR', 'Default': '0x00', 'User': '00YYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x24', 'POS': 0, 'RegisterName': 'VBAT measurement reg 2', 'RegisterLength': 8, 'Name': 'vbat_meas[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]},expected_value=0x1FE)
CODE0=int(HCODE0)
pvdd_forced_voltage = VFORCE(signal="PVDD", reference="GND", value=4.8,error_spread=0)
sleep(0.01)
VB1 = VMEASURE(signal="PVDD", reference="GND", expected_value=4.8,error_spread=0)
sleep(0.001)


HCODE1=I2C_READ(device_address="0x38",field_info={'fieldname': 'vbat_meas', 'length': 10, 'registers': [{'REG': '0x23', 'POS': 0, 'RegisterName': 'VBAT measurement reg 1', 'RegisterLength': 8, 'Name': 'vbat_meas[9:8]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 9, 'FieldLSB': 8, 'Attribute': '000000RR', 'Default': '0x00', 'User': '00YYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x24', 'POS': 0, 'RegisterName': 'VBAT measurement reg 2', 'RegisterLength': 8, 'Name': 'vbat_meas[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]},expected_value=0x380)
CODE1=int(HCODE1)

mreal=(VB1-VB0)/(CODE1-CODE0)
vbat_off=round((VB0/mreal))-CODE0


if vbat_off <0:  
    otp_vbat_off=256+vbat_off
else:
    otp_vbat_off=vbat_off
vbat_gain=(mreal/mid-1)*1024
if vbat_gain <0:  
    otp_vbat_gain=256+round(vbat_gain)
else:
    otp_vbat_gain=round(vbat_gain)

print(f'............ {Test_Name} Passed ........')
    # write the optimized code if the trim passed
I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1) # page 1
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_sar_gain_vbat', 'length': 8, 'registers': [{'REG': '0xC2', 'POS': 0, 'RegisterName': 'OTP FIELDS 18 - TRACEABILITY 6', 'RegisterLength': 8, 'Name': 'otp_sar_gain_vbat[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=hex(otp_vbat_gain))
I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x00,PageNo=0) # page 0

print(f"Optimal Code: {otp_vbat_off}")
print(f"Optimal Code: {otp_vbat_gain}")

I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_en', 'length': 1, 'registers': [{'REG': '0xDF', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NPPPNNNN', 'Default': '0x01', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
sleep(0.001)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
# I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_clk12m_bypass', 'length': 1, 'registers': [{'REG': '0x80', 'POS': 3, 'RegisterName': 'PLL_REG_1', 'RegisterLength': 8, 'Name': 'pll_clk12m_bypass', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x21', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vbat_filt', 'length': 6, 'registers': [{'REG': '0xD8', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vbat_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vtemp_filt', 'length': 6, 'registers': [{'REG': '0xD9', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vtemp_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'sar_vbat_avg_sel', 'length': 2, 'registers': [{'REG': '0xDE', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'sar_vbat_avg_sel[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'temp_duty_cycle', 'length': 4, 'registers': [{'REG': '0xDA', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'temp_duty_cycle[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x01', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)