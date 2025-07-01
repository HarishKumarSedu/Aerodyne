from dfttools import *
from time import sleep
import random
from Procedures import Startup

Test_Name = 'UVLO_L2H_Trim'
print(f'............ {Test_Name} ........')

'''
Set "PVDD"=2.25V (desired L2H UVLO threshold), 
bring UVLO comparator output to pin "IODATA0" 
through digital test mux and 
sweep the UVLO 0.4V reference voltage 
trimming code until the comparator toggles 
---------------------------------------------
1.UVLO Trim 0v4
2.Turn ON the part in active mode, temp=27°C, vddp=3.7V, vdd=1.8V, vddd=1.2V, enable ref_analdo, enable ref_pvdd_uvlo,
{'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}<4:0> = 0d;
3.Wait 50us;
4.Bring out to the analog test point (rfu_ds_ref_test_en_vddd=1d) the UVLO reference voltage;
5.Sweep vddp from 0V to 3.7V and observe the ana_ds_pvdd_uvlo signal at the digital MUX; ana_ds_pvdd_uvlo goes from "VDD" to 0V when a certain value of vddp is reached: 
target value is 2.25V; this leads to a reference voltage is 0.4V for the UVLO;
6.Change the {'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}<4:0> to get the transition of ana_ds_pvdd_uvlo as close as possible to the target value;
7.Burn the OTP with the value of {'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}<4:0> found in step 4.
'''
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'analdo_en_m', 'length': 1, 'registers': [{'REG': '0x1D', 'POS': 5, 'RegisterName': 'FORCE_REGISTERS_6', 'RegisterLength': 8, 'Name': 'analdo_en_m', 'Mask': '0x20', 'Length': 1, 'FieldMSB': 5, 'FieldLSB': 5, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
# not found designers find it 
# I2C_WRITE(device_address="0x68", field_info=, write_value=0x1)
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)
# bring out the necessary signal through mux
# I2C_WRITE(device_address="0x68", field_info=, write_value=)

HL_Th = 2.25  # 2.25V threshold
error_spread = 2.5e-3 # 2.5mv error spread
code_width = 4  # 4 bits trimming code
min_error = float('inf')
optimal_code = None
optimal_measured_value = None
force_voltage_low_limit = 0  # minimum voltage limit
force_voltage_high_limit = 3.7  # minimum voltage limit

for Code in range(2**code_width):
    # TODO: Write trimming code to device via I2C
    # Example (uncomment and fill device_address and field_info):
    I2C_WRITE(device_address="0x68", field_info={'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(Code))

    force_voltage = force_voltage_high_limit
    trigger = False

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
    if error < min_error:
        min_error = error
        optimal_code = hex(Code)
        optimal_measured_value = uvlo_forced_voltage

# Final check and reporting
if force_voltage_low_limit < optimal_measured_value < force_voltage_high_limit:
    print(f'............ Trim_Bg Test Passed ........')
    # TODO: Burn optimal trimming code to OTP via I2C
    I2C_WRITE(device_address="0x68", field_info={'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=optimal_code)
else:
    print(f'............ Trim_Bg Test Failed ........')
    I2C_WRITE(device_address="0x68", field_info={'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)

print(f"Optimal Code: {optimal_code}")
print(f"Optimal Measured Value: {optimal_measured_value:.4f} V (Target: {HL_Th} V)")
print(f"Minimum Error: {min_error:.6f} %")