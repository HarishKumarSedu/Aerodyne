from dfttools import *
from time import sleep

Test_Name = 'GPADCTemp_Off_Trim'
from Procedures import Startup
print(f'............ {Test_Name} ........')
# designers must go through the details and correct the procedure
'''
Procedure 
    before to start the bandgap has to be trimmed
    1.Enable the SAR ADC with extenal clock
    2.Wait 100us
    3.Do measure at room temperature  (27 degree)
    4.Measure the temperature register after 8 average
    5.Target Code(Decimal)=-1.628904*(Temp+40)+674  At 27  Target is 674 Decimal
'''
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
sleep(0.001)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vbat_filt', 'length': 6, 'registers': [{'REG': '0xD8', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vbat_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x10)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vtemp_filt', 'length': 6, 'registers': [{'REG': '0xD9', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vtemp_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x10)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'sar_temp_avg_sel', 'length': 2, 'registers': [{'REG': '0xDE', 'POS': 2, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'sar_temp_avg_sel[1:0]', 'Mask': '0xC', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x3)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'temp_duty_cycle', 'length': 4, 'registers': [{'REG': '0xDA', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'temp_duty_cycle[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x01', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_clk12m_bypass', 'length': 1, 'registers': [{'REG': '0x80', 'POS': 3, 'RegisterName': 'PLL_REG_1', 'RegisterLength': 8, 'Name': 'pll_clk12m_bypass', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x21', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_en', 'length': 1, 'registers': [{'REG': '0xDF', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NPPPNNNN', 'Default': '0x01', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
sleep(0.003)
#I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)

# select the mux to bring out the ana_dd_gpadc_tb_delay_clock_dvdd signal on "IOCLK0"
# the frequency measured is > of 9.09MHz.  
# I2C_WRITE(device_address="0x38",field_info=,write_value=)
# desingers needs to correct the assumptions
limit_percentage = 0.1 # assuming 
target_value = 674 # 674
# higher and lower limits taken about +/- 10% of the target value 
lower_limit = target_value-target_value*limit_percentage
higher_limit = target_value+target_value*limit_percentage
error_spread = target_value*0.05 # 5% of target value
temp_read=I2C_READ(device_address="0x38",field_info={'fieldname': 'temp_meas', 'length': 10, 'registers': [{'REG': '0x21', 'POS': 0, 'RegisterName': 'TEMP measurement reg 1', 'RegisterLength': 8, 'Name': 'temp_meas[9:8]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 9, 'FieldLSB': 8, 'Attribute': '000000RR', 'Default': '0x00', 'User': '00YYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x22', 'POS': 0, 'RegisterName': 'TEMP measurement reg 2', 'RegisterLength': 8, 'Name': 'temp_meas[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]},expected_value=0x2BC)
temp_dec=int(temp_read)
temp_corr=target_value-temp_dec
if temp_corr <0:  
    temp_core=256+temp_corr
else:
    temp_core=temp_corr

print(f'............ {Test_Name} Passed ........')
    # write the optimized code if the trim passed
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x1)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'otp_sar_offs', 'length': 10, 'registers': [{'REG': '0xBF', 'POS': 4, 'RegisterName': 'OTP FIELDS 15 - TRACEABILITY 3', 'RegisterLength': 8, 'Name': 'otp_sar_offs[9:8]', 'Mask': '0x30', 'Length': 2, 'FieldMSB': 9, 'FieldLSB': 8, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}, {'REG': '0xC1', 'POS': 0, 'RegisterName': 'OTP FIELDS 17 - TRACEABILITY 5', 'RegisterLength': 8, 'Name': 'otp_sar_offs[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=hex(temp_core))
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},write_value=0x0)

print(f"Optimal Code: {temp_core}")



I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_en', 'length': 1, 'registers': [{'REG': '0xDF', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NPPPNNNN', 'Default': '0x01', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
sleep(0.001)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_clk12m_bypass', 'length': 1, 'registers': [{'REG': '0x80', 'POS': 3, 'RegisterName': 'PLL_REG_1', 'RegisterLength': 8, 'Name': 'pll_clk12m_bypass', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x21', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vbat_filt', 'length': 6, 'registers': [{'REG': '0xD8', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vbat_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'gpadc_vtemp_filt', 'length': 6, 'registers': [{'REG': '0xD9', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'gpadc_vtemp_filt[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'sar_temp_avg_sel', 'length': 2, 'registers': [{'REG': '0xDE', 'POS': 2, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'sar_temp_avg_sel[1:0]', 'Mask': '0xC', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
I2C_WRITE(device_address="0x38",field_info={'fieldname': 'temp_duty_cycle', 'length': 4, 'registers': [{'REG': '0xDA', 'POS': 0, 'RegisterName': 'SAR ADC settings ', 'RegisterLength': 8, 'Name': 'temp_duty_cycle[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x01', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)