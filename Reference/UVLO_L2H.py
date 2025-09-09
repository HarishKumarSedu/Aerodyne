from dfttools import *
from time import sleep
import random
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
def uvlo_l2h_test():
  Test_Name = 'UVLO_L2H'
  print(f'............ {Test_Name} ........')

  '''
Bring UVLO comparator output to pin "IODATA0" 
through digital test mux and sweep "PVDD" from 1.5V to 3V 
and record the value at which the compator toggles.
---------------------------------------------
  1.UVLO L2H
  2.Turn ON the part in active mode, temp=27°C, vddd=1.2V, UVLO trimmed ({'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x60', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}<4:0>=value);
  3.Wait 50 us;
  4.Observe the ana_ds_pvdd_uvlo signal at the digital MUX and sweep vddp from 0V to 3.7V;
  5.Store the vddp value for which the ana_ds_pvdd_uvlo goes from "VDD" to 0V; it is the L2H threshold of the UVLO.
  '''
  # Enabling test page
  I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1) # page 1
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'debug_in_en', 'length': 7, 'registers': [{'REG': '0x22', 'POS': 0, 'RegisterName': 'Debug resgister 1', 'RegisterLength': 8, 'Name': 'debug_in_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x4)
  #Enabling digital TMUX
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x2)
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x21)

  LH_Th = 2.25  # 2.25V threshold expected trigger  
  error_spread = LH_Th*0.1 # 10% error spread
  force_voltage_low_limit = 1.5  # minimum voltage limit
  force_voltage_high_limit = 3.7  # minimum voltage limit
  force_voltage = force_voltage_high_limit

  while True:
    # Add noise simulation
    pvdd_forced_voltage = VFORCE(signal="PVDD", reference="GND", value=force_voltage,error_spread=error_spread)
    # Check trigger condition
    trigger = VTRIG_LH(signal="IODATA0", reference="GND", threshold=LH_Th, expected_value=force_voltage)

    if trigger:
      break
    elif pvdd_forced_voltage < force_voltage_low_limit:
      print(f'..... Voltage max limit {force_voltage_high_limit}V crossed ........')
      break

    force_voltage -= 0.005  #  voltage by 5mV step
    sleep(0.001)  # 1 ms delay
  
  error = abs(pvdd_forced_voltage - LH_Th)/abs(LH_Th) * 100
  print(f"Optimal Measured(force sweeped) Value: {pvdd_forced_voltage:.4f} V (Target: {LH_Th} V)")
  print(f"Minimum Error: {error:.6f} %")

if __name__ == '__main__':
  uvlo_l2h_test()

