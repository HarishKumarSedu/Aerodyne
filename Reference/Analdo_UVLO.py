from dfttools import *
from time import sleep
import random
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable

def analdo_uvlo():
  Test_Name = 'Analdo UVLO'
  print(f'............ {Test_Name} ........')
  startup()
  global_enable()

  '''
  Bring analogLDO UVLO comparator output to pin "IOCLK0" 
  through digital test mux and verify it is at the correct level
'''

  # Enabling test page
  I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1) # page 1
  #Enabling digital TMUX
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x21)

  target_value = 1.8 # 1.8V
  error_spread = target_value*0.04 # 4% of target value
  measured_value = VMEASURE(signal="IOCLK0", reference="GND", expected_value=target_value,error_spread=error_spread)
  error = abs(measured_value - target_value)/abs(target_value) *100
  print(f"Optimal measured value : {measured_value}V, Target value : {target_value}V")
  print(f"Minimum Error: {error}%")

if __name__ == '__main__':
  analdo_uvlo()

