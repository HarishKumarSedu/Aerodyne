from dfttools import *
from time import sleep 
import random
Test_Name = 'noise floor_1kHz_-60dBFS_5L'

print(f'............ {Test_Name} ........')

'''
1.Reach the playback state with 5L modulation
2.Enable internal sinusoid generator to play -60dBFS at 1 kHz.
3.Wait 1ms.
4.Perform A-weighted SNR measurement, AWSNR, on the differential output voltage signal. 
  ASWNR(dB)=20*log10(V_signal_RMS/V_noise_RMS) with A-weighting applied.
  A 1kHz -60dBFS tone has a V_signal_RMS=(6V*0.001/1.414)=4.24mVRMS amplitude.
5.Noise floor RMS value is expected to be 6uVRMS, so AWSNR is expected to be larger than 20*log10(4.24mV/6uV)=57dB.
'''
# 1.
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0) 
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1) 
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_modulation', 'length': 2, 'registers': [{'REG': '0x95', 'POS': 0, 'RegisterName': 'CLD analog setting reg 1', 'RegisterLength': 8, 'Name': 'cld_modulation[1:0]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x96', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=2) # 5L modulation
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'spk_en', 'length': 1, 'registers': [{'REG': '0x9F', 'POS': 0, 'RegisterName': 'Enables settings 5', 'RegisterLength': 8, 'Name': 'spk_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000S', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1) 
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tdm_sync_mode', 'length': 1, 'registers': [{'REG': '0x4E', 'POS': 7, 'RegisterName': 'TDM settings 13', 'RegisterLength': 8, 'Name': 'tdm_sync_mode', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x89', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0) 
# 2.
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(1))  #Page 1 in regmap
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'internal_sin_gain', 'length': 4, 'registers': [{'REG': '0x1F', 'POS': 4, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_gain[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(10))  # -60dB sinus amplitude
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'internal_sin_freq', 'length': 3, 'registers': [{'REG': '0x1F', 'POS': 0, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_freq[2:0]', 'Mask': '0x7', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(2))  # 1kHz sinus wave
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'internal_sin_en', 'length': 1, 'registers': [{'REG': '0x1F', 'POS': 3, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_en', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(1))  # Enable internal sin generator
# 3.
sleep(0.0001) 
# 4.
minimum_AWSNR = 55
error_percentage = 0.03
expected_AWSNR = 57
expected_vals = {'SNR': expected_AWSNR}
error_spreads = {'SNR': expected_AWSNR*error_percentage}
measured_Values = FFT(signal="OUTP",reference="OUTN",signal_type='Analog',expected_values=expected_vals,error_spreads=error_spreads) #,sample_number=?,sample_time=?,window='Hanning' do we need to specify them?
measured_AWSNR = measured_Values.get('SNR') 
# 5.
if measured_AWSNR > minimum_AWSNR:
  print(f'...... {Test_Name}..Passed SNR:{measured_AWSNR}dB ')
else:
  print(f'...... {Test_Name}..Failed SNR:{measured_AWSNR}dB ')