from dfttools import *
from time import sleep
import random

Test_Name = 'Cascode_P_Ron'
from Procedures.Ron_CLD import ron_cld_setup,ron_cld_unset
def cascode_p_ron():
  print(f'............ {Test_Name} ........')
  
  #I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0) # page 0
  ron_cld_setup()
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0) # page 0
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0xE)  # set bridge switch (LSp on, MIDp on, CASp on, HSp off, LSn off, MIDn off, CASn off, HSn off)
  
  # Wait for device stabilization
  sleep(0.0001)  # 100 µs
  
  I_forced= 0.5 # APPLY WITH RAMP
  
  # Step 3: Force 500mA current into "OUTP" pin
  AFORCE(signal="OUTP", reference="OUTN", value=I_forced, error_spread=I_forced*1e-2)  # 500mA ±5%
  
  dV = VMEASURE(signal="OUTP", reference="VMID", expected_value=0.028, error_spread=0.01)
  CASCODEP_ron = (dV / I_forced ) - 25e-3 # R = V/I
  
  print(f'Calculated cascode P-Ron: {CASCODEP_ron:.3f} Ohms')
  print(f'[Expected ~67m Ohms typical, based on dV={dV:.3f}V @ {I_forced*1000:.0f}mA]')
  
  AFORCE(signal="OUTP", reference="OUTN", value=float('inf'), error_spread=0.05)  # stop forcing
  ron_cld_unset()
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'cld_dvr_force_sel', 'length': 8, 'registers': [{'REG': '0x9C', 'POS': 0, 'RegisterName': 'CLD analog setting reg 6', 'RegisterLength': 8, 'Name': 'cld_dvr_force_sel[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0x0) 
if __name__ == '__main__':
  cascode_p_ron()