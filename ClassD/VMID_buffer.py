from dfttools import *
from time import sleep 
import random
'''
"VMID" buffer test
Step 1. Configure the device registers to enable testing.
Step 2. Bring the DAC voltage reference to pin "IODATA1" through the analog test mux p and the local ground to pin "ADDR" through the analog test mux n.
Step 3. Wait for the signal to stabilize and measure the differential voltage "IODATA1" wrt "ADDR".
'''
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback

def vmid_buffer():
  Test_Name = '"VMID" buffer test'
  print(f'............ {Test_Name} ........')
  startup()
  global_enable()
  playback()

  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1) # page 1
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1) # enable atp
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x6)  # {'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_driver_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 2, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'cld_driver_test_en', 'Mask': '0x4', 'Length': 1, 'FieldMSB': 2, 'FieldLSB': 2, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]} , write_value=0x1)  # test enable for driver

  '''
  Wait for the time needed for vmid to charge. 
  Suppose Cmid=10uF
  Buffer output resistance is 40 Ohm. Time constant is 10uFx40Ohm=400us.
  Settling time is about 5tau=2ms
  ''' 
  # Step 3
  sleep(0.002) #5tau
  expected_value = 1.85
  error_spread = expected_value*0.0054 #10mV error
  measured_value = VMEASURE(signal="IODATA1", reference="GND", expected_value=expected_value, error_spread=error_spread)

  print(f'Measured DAC 0p9V voltage reference value at "IODATA1" wrt "ADDR": {measured_value}')

  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1) # page 1
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0) # disable atp
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_n_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_n_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_driver_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 2, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'cld_driver_test_en', 'Mask': '0x4', 'Length': 1, 'FieldMSB': 2, 'FieldLSB': 2, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]} , write_value=0x0)  # test disable for driver
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)  # {'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}

if __name__ == '__main__':
  vmid_buffer()