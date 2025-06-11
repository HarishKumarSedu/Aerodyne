from dfttools import *
from time import sleep
import random
from Procedures import Startup

Test_Name = 'UVLO_H2L'
print(f'............ {Test_Name} ........')

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
LH_Th = 2.25  # assumed 2.25V threshold expected trigger @,  designers must write 
error_spread = 2.5e-3 # 2.5mv error spread
force_voltage_low_limit = 0  # minimum voltage limit
force_voltage_high_limit = 3.7  # max voltage limit
force_voltage = force_voltage_low_limit

while True:
  # Add noise simulation
  uvlo_forced_voltage = VFORCE(signal="IODATA0", reference="GND", value=force_voltage,error_spread=error_spread)
  # Check trigger condition
  trigger = VTRIG_LH(signal="PVDD", reference="GND", threshold=LH_Th, expected_value=force_voltage)

  if trigger:
    break
  elif uvlo_forced_voltage >= force_voltage_high_limit:
    print(f'..... Voltage max limit {force_voltage_low_limit}V crossed ........')
    break

  force_voltage += 0.05  # increase voltage by 50mV
  sleep(0.01)  # 10 ms delay
  
error = abs(uvlo_forced_voltage - LH_Th)/abs(LH_Th) * 100
print(f"Optimal Measured(force sweeped) Value: {uvlo_forced_voltage:.4f} V (Target: {LH_Th} V)")
print(f"Minimum Error: {error:.6f} %")

