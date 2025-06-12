from dfttools import *
from time import sleep
import random
Test_Name = 'V-sense THD'
from Procedures import Startup
print(f'............ {Test_Name} ........')
from Procedures import Playback
from Procedures import Internal_sin_1kHz_1W # set the internal sinusoidal generator at 1kHz 1W
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(0x01))  #Page 1 in regmap
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'internal_sin_gain', 'length': 4, 'registers': [{'REG': '0x1F', 'POS': 4, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_gain[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(0x00))  # 0dB sinus amplitude
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(0x01))  #Page 0 in regmap
from Procedures import VI_SNS_turn_on
'''
  Wait for 1ms, waiting for settling
  Measure from TDM V-sns digital output
  Desired value is 83dB
 '''
sleep(0.001)  # 1 ms
# realize FFT expexted value = 83dB, error: +/- 3dB
expected_vals = {'THD': 83}
measured_THD = FFT(signal='TDM_OUTPUT',reference="GND",signal_type='Digital',sample_number=9202,sample_time=0.003,window='Hanning',expected_values=expected_vals) 
if measured_THD < 80.0:
  print(f' ....... {Test_Name} ... Failed  :>  {measured_THD}dB')
else:
  print(f' ....... {Test_Name} ... Passed  :>  {measured_THD}dB')
