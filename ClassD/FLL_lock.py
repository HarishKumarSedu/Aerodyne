from dfttools import *
from time import sleep 
import random
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback

def fll_lock_check():
  Test_Name = 'FFL_lock_condition_check'
  print(f'............ {Test_Name} ........')
  startup()
  global_enable()
  playback()

  '''
  FFL_lock_condition_check
  The FLL is trimmed, "IOCLK0" has 3.072MHz clock.
  Step 1. Bring out on "IODATA0" the lock control signal
  Step 2. If the FLL is locked, doublecheck its frequency output frequency by bringing out on "ADDR" the PWM clock output.
  '''

  # Step 1
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=6)  # enable "IODATA0"
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=3) # bring out {'fieldname': 'fll_lock', 'length': 1, 'registers': [{'REG': '0x24', 'POS': 6, 'RegisterName': 'Sequencer status register 1', 'RegisterLength': 8, 'Name': 'fll_lock', 'Mask': '0x40', 'Length': 1, 'FieldMSB': 6, 'FieldLSB': 6, 'Attribute': 'PR0RRRRR', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}
  sleep(0.0001) 
  expected_value = 1.8
  error_spread = expected_value*0.2 
  fll_lock_vddd=VMEASURE(signal="IODATA0", reference="GND", expected_value=expected_value, error_spread=error_spread)
  VMEASURE(signal="IODATA0", reference="GND", expected_value=float('Inf')) # remote path once measure is done 
  if fll_lock_vddd>1:
    # Step 2
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]},  write_value=0x10) #enable "ADDR"
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0) #bring out PWM frequency 
    sleep(0.0001) 
    expected_value = 289129 
    error_spread = expected_value*0.003 #1kHz precision
    PWM_freq = FREQMEASURE(signal="ADDR", reference="GND",expected_value=expected_value, error_spread=error_spread)
    print(f'FLL is locked, the PWM frequency at "ADDR" is: {PWM_freq}')
  else:
    print(f'FLL is not locked')

if __name__ == '__main__':
  fll_lock_check()


