from dfttools import *
from time import sleep
import random
Test_Name = 'I-sense THD'
from Procedures import Startup
print(f'............ {Test_Name} ........')
from Procedures import Playback
# from Procedures import Internal_sin_1kHz_1W # set the internal sinusoidal generator at 1kHz 1W
I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1) # page 1  #Page 1 in regmap
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'internal_sin_gain', 'length': 4, 'registers': [{'REG': '0x1F', 'POS': 4, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_gain[3:0]', 'Mask': '0xF0', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(0x00))  # 0dB sine amplitude
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'internal_sin_freq', 'length': 3, 'registers': [{'REG': '0x1F', 'POS': 0, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_freq[2:0]', 'Mask': '0x7', 'Length': 3, 'FieldMSB': 2, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(0x02))  # 1kHz sine frequncy
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'internal_sin_en', 'length': 1, 'registers': [{'REG': '0x1F', 'POS': 3, 'RegisterName': 'Internal sin register 1', 'RegisterLength': 8, 'Name': 'internal_sin_en', 'Mask': '0x8', 'Length': 1, 'FieldMSB': 3, 'FieldLSB': 3, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(0x01))  # internal sine enable
I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x00,PageNo=0)   #Page 0 in regmap
from Procedures import VI_SNS_turn_on
sleep (0.01)
# Acquire via TDM V-sns stream, (fsyn 48KHz, BCLK 3 MHz, delay_mode=1)
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pcm_vmon_en', 'length': 1, 'registers': [{'REG': '0x5D', 'POS': 0, 'RegisterName': 'TDM settings 15', 'RegisterLength': 8, 'Name': 'pcm_vmon_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '00000NNN', 'Default': '0x00', 'User': '00000YYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=hex(0x02))  # Setting I-sns output
I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tdm_tx_en', 'length': 1, 'registers': [{'REG': '0x5F', 'POS': 0, 'RegisterName': 'TDM settings 17', 'RegisterLength': 8, 'Name': 'tdm_tx_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=hex(0x01))  # Enable tdm in transmission
sleep (0.01)
'''
  Wait for 1ms, waiting for settling
  Measure from TDM V-sns digital output
  Desired value is 65dB
 '''
sleep(0.001)  # 1 ms
# Measure TDM Dgital from "IODATA1" for FFT Computations 
# realize FFT expexted value = 65dB, error: +/- 3dB
expected_vals = {'THD': 65}
measured_THD = FFT(signal="IODATA1",reference="GND",signal_type='Digital',sample_number=9202,sample_time=0.003,window='Hanning',expected_values=expected_vals).get('THD') 
if measured_THD < 62.0:
  print(f' ....... {Test_Name} ... Failed  :>  {measured_THD}dB')
else:
  print(f' ....... {Test_Name} ... Passed  :>  {measured_THD}dB')