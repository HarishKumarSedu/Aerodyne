from dfttools import *
from time import sleep 
import random
Test_Name = 'THD_1kHz_1W_3L_max_DAC_Current'

print(f'............ {Test_Name} ........')

'''
1.Reach the playback state with 3L modulation
2.Set class D DAC at maximum current
2.Enable internal sinusoid generator to play 1W at 1 kHz.
3.Wait 1ms.
4.Perform THD measurement on the differential voltage signal measured as voltage @"OUTP" pin - voltage #"OUTN" pin.
5.Expected value is -80dB. Maximum value is -74dB.
'''
# 1.
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0) 
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1) 
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_modulation', 'length': 2, 'registers': [{'REG': '0x95', 'POS': 0, 'RegisterName': 'CLD analog setting reg 1', 'RegisterLength': 8, 'Name': 'cld_modulation[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x96', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1) # 3L modulation
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'spk_en', 'length': 1, 'registers': [{'REG': '0x9F', 'POS': 0, 'RegisterName': 'Enables settings 5', 'RegisterLength': 8, 'Name': 'spk_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000S', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1) 
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'spk_gain', 'length': 3, 'registers': [{'REG': '0x92', 'POS': 0, 'RegisterName': 'SPK setting reg 1', 'RegisterLength': 8, 'Name': 'spk_gain[2:0]', 'Mask': '0x7', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': '000NNNNN', 'Default': '0x03', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=5) # dac at max current
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tdm_sync_mode', 'length': 1, 'registers': [{'REG': '0x4E', 'POS': 7, 'RegisterName': 'TDM settings 13', 'RegisterLength': 8, 'Name': 'tdm_sync_mode', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x99', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0) 
# 2.
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=hex(1))  #Page 1 in regmap
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'internal_sin_gain', 'length': 4, 'registers': [{'REG': '0x1F', 'POS': 4, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_gain[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(1))  # -6dB sinus amplitude
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'internal_sin_freq', 'length': 3, 'registers': [{'REG': '0x1F', 'POS': 0, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_freq[2:0]', 'Mask': '0x7', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(2))  # 1kHz sinus wave
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'internal_sin_en', 'length': 1, 'registers': [{'REG': '0x1F', 'POS': 3, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_en', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(1))  # Enable internal sin generator
# 3.
sleep(0.0001) 
# 4.
maximum_thd = -74
error_percentage = 0.075 #7.5%
expeted_thd = -80
expected_vals = {'THD': expeted_thd}
error_spreads = {'THD': expeted_thd*error_percentage}
measured_Values = FFT(signal="OUTP",reference="OUTN",signal_type='Analog',expected_values=expected_vals,error_spreads=error_spreads) #sample_number=?,sample_time=?,window='Hanning' do we need to specify them?
measured_THD = measured_Values.get('THD') 
# 5.
if measured_THD < maximum_thd:
  print(f'...... {Test_Name}..Passed THD:{measured_THD}dB ')
else:
  print(f'...... {Test_Name}..Failed THD:{measured_THD}dB ')