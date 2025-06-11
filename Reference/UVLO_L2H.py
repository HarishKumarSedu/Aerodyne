from dfttools import *
from time import sleep
import random
from Procedures import Startup

Test_Name = 'UVLO_L2H'
print(f'............ {Test_Name} ........')

'''
Bring UVLO comparator output to pin "IODATA0" 
through digital test mux and sweep "PVDD" from 1.5V to 3V 
and record the value at which the compator toggles.
---------------------------------------------
  1.UVLO L2H
  2.Turn ON the part in active mode, temp=27°C, vddd=1.2V, UVLO trimmed ({'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}<4:0>=value );
  3.Wait 50 us;
  4.Observe the ana_ds_pvdd_uvlo signal at the digital MUX and sweep vddp from 0V to 3.7V;
  5.Store the vddp value for which the ana_ds_pvdd_uvlo goes from "VDD" to 0V; it is the L2H threshold of the UVLO.
'''
HL_Th = 2.25  # 2.25V threshold expected trigger designers must write 
error_spread = 2.5e-3 # 2.5mv error spread
force_voltage_low_limit = 1.5  # minimum voltage limit
force_voltage_high_limit = 3  # minimum voltage limit
force_voltage = force_voltage_high_limit

while True:
  # Add noise simulation
  uvlo_forced_voltage = VFORCE(signal="IODATA0", reference="GND", value=force_voltage,error_spread=error_spread)
  # Check trigger condition
  trigger = VTRIG_HL(signal="PVDD", reference="GND", threshold=HL_Th, expected_value=force_voltage)

  if trigger:
    break
  elif uvlo_forced_voltage <= force_voltage_low_limit:
    print(f'..... Voltage min limit {force_voltage_low_limit}V crossed ........')
    break

  force_voltage -= 0.05  # decrease voltage by 50mV
  sleep(0.01)  # 10 ms delay
  
error = abs(uvlo_forced_voltage - HL_Th)/abs(HL_Th) * 100
print(f"Optimal Measured(force sweeped) Value: {uvlo_forced_voltage:.4f} V (Target: {HL_Th} V)")
print(f"Minimum Error: {error:.6f} %")

