from dfttools import *
from time import sleep 
import random
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
from Procedures.Playback import playback

def fll_vddp_r_current():
  Test_Name = 'FLL_VDDP_R_current'
  print(f'............ {Test_Name} ........')
  startup()
  global_enable()
  playback()

  '''
  FLL_VDDP_R_current
  The FLL is trimmed, "IOCLK0" has 3.072MHz clock.
  this is a n2p current measure from 
  Step 1. Bring out on "IODATA1" VDDP/R current of the FLL
  Step 2. Measure it.
  '''

  # Step 1
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1) #enable "IODATA1" 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_pwm_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 5, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'cld_pwm_test_en', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0) #bring out the VDDD/R current
  sleep(0.0001) 
  expected_value = 1e-6 #3.6/(3*1200000)->(vddp/3R)
  '''
  FLL Bias Current is the n2p current measurement
  1. Measure current between the "VDD" and "IODATA1"
  2. Current Measured at bench ~ 1.136uA
  '''
  error_spread = expected_value*0.2
  measured_value=AMEASURE(signal="VDD", reference="IODATA1", expected_value=expected_value, error_spread=error_spread)

  print(f'FLL VDDP/R current expected_value {expected_value} is: {measured_value}')
  VMEASURE(signal="VDD", reference="IODATA1", expected_value=float('Inf'))
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_pwm_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 5, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'cld_pwm_test_en', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0) #enable "IODATA1"
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0) #bring out the VDDD/R current

if __name__ == '__main__':
  fll_vddp_r_current()