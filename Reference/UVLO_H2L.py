from dfttools import *
from time import sleep
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable

def uvlo_h2l_test():
  Test_Name = 'UVLO_H2L'
  print(f'............ {Test_Name} ........')
  startup()
  global_enable()
  '''
Enable the bandgap, bring UVLO comparator output to pin "IODATA0" 
through digital test mux and 
sweep "PVDD" from 3V to 1.5V and record the value 
at which the compator toggles
---------------------------------------------
  1.UVLO H2L
  2.Turn ON the part in active mode, temp=27°C, vddd=1.2V, ref_bg enabled;
  3.Wait 50 us;
  4.Observe the ana_ds_pvdd_uvlo signal at the digital MUX and sweep vddp from 3.7V to 0V;
  5.Store the vddp value for which the ana_ds_pvdd_uvlo goes from 0V to "VDD"; it is the H2L threshold of the UVLO.
'''
  # Enabling test page
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel_1', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel_1', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'bg_en_m', 'length': 1, 'registers': [{'REG': '0x1D', 'POS': 7, 'RegisterName': 'FORCE_REGISTERS_6', 'RegisterLength': 8, 'Name': 'bg_en_m', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'N0NNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'analdo_en_m', 'length': 1, 'registers': [{'REG': '0x1D', 'POS': 5, 'RegisterName': 'FORCE_REGISTERS_6', 'RegisterLength': 8, 'Name': 'analdo_en_m', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': 'N0NNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pvdd_uvlo_en_m', 'length': 1, 'registers': [{'REG': '0x1D', 'POS': 4, 'RegisterName': 'FORCE_REGISTERS_6', 'RegisterLength': 8, 'Name': 'pvdd_uvlo_en_m', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'N0NNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'ref_force', 'length': 1, 'registers': [{'REG': '0x1C', 'POS': 4, 'RegisterName': 'FORCE_REGISTERS_5', 'RegisterLength': 8, 'Name': 'ref_force', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': '000NNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'debug_in_en', 'length': 7, 'registers': [{'REG': '0x22', 'POS': 0, 'RegisterName': 'Debug resgister 1', 'RegisterLength': 8, 'Name': 'debug_in_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x4)
  #Enabling digital TMUX
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x2)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x21)

  HL_Th = 1.96  # assumed 1.96V threshold expected trigger
  error_spread = HL_Th*0.05 # 5% error spread
  force_voltage_low_limit = 0  # minimum voltage limit
  force_voltage_high_limit = 3.7  # max voltage limit
  force_voltage = force_voltage_low_limit

  while True:
      # Add noise simulation
      pvdd_forced_voltage = VFORCE(signal="PVDD", reference="GND", value=force_voltage,error_spread=error_spread)
      # Check trigger condition
      trigger = VTRIG_HL(signal="IODATA0", reference="GND", threshold=HL_Th, expected_value=force_voltage)

      if trigger:
        break
      elif pvdd_forced_voltage <= force_voltage_high_limit:
        print(f'..... Voltage high limit {force_voltage_high_limit}V crossed ........')
        break

      force_voltage += 0.05  # increase voltage by 50mV
      sleep(0.001)  # 1 ms delay
  
  error = abs(pvdd_forced_voltage - HL_Th)/abs(HL_Th) * 100
  print(f"Optimal Measured(force sweeped) Value: {pvdd_forced_voltage:.4f} V (Target: {HL_Th} V)")
  print(f"Minimum Error: {error:.6f} %")
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'bg_en_m', 'length': 1, 'registers': [{'REG': '0x1D', 'POS': 7, 'RegisterName': 'FORCE_REGISTERS_6', 'RegisterLength': 8, 'Name': 'bg_en_m', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'N0NNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'analdo_en_m', 'length': 1, 'registers': [{'REG': '0x1D', 'POS': 5, 'RegisterName': 'FORCE_REGISTERS_6', 'RegisterLength': 8, 'Name': 'analdo_en_m', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': 'N0NNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pvdd_uvlo_en_m', 'length': 1, 'registers': [{'REG': '0x1D', 'POS': 4, 'RegisterName': 'FORCE_REGISTERS_6', 'RegisterLength': 8, 'Name': 'pvdd_uvlo_en_m', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': 'N0NNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'ref_force', 'length': 1, 'registers': [{'REG': '0x1C', 'POS': 4, 'RegisterName': 'FORCE_REGISTERS_5', 'RegisterLength': 8, 'Name': 'ref_force', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': '000NNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)
if __name__ == '__main__':
  uvlo_h2l_test()