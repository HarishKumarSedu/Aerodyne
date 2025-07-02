from dfttools import *
from time import sleep
import random
from Procedures import Startup


Test_Name = 'UVLO_L2H_Trim_0v4'
print(f'............ {Test_Name} ........')

'''
1.Turn ON the part in active mode, temp=27°C, vddp=3.7V, vdd=1.8V, vddd=1.2V, enable ref_analdo, enable ref_pvdd_uvlo,
{'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x60', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}<4:0> = 0d;
2.Wait 50us;
3.Bring out to the analog test point (rfu_ds_ref_test_en_vddd=1d) the UVLO reference voltage;
4.Sweep vddp from 0V to 3.7V and observe the ana_ds_pvdd_uvlo signal at the digital MUX; ana_ds_pvdd_uvlo goes from "VDD" to 0V when a certain value of vddp is reached: 
target value is 2.25V; this leads to a reference voltage is 0.4V for the UVLO;
5.Change the {'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x60', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}<4:0> to get the transition of ana_ds_pvdd_uvlo as close as possible to the target value;
6.Burn the OTP with the value of {'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x60', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}<4:0> found in step 4.
'''
#Enabling test page
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'i2c_page_sel', 'length': 2, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
#Enabling "PVDD" UVLO
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'ref_force', 'length': 1, 'registers': [{'REG': '0x1C', 'POS': 4, 'RegisterName': 'FORCE_REGISTERS_5', 'RegisterLength': 8, 'Name': 'ref_force', 'Mask': '0x10', 'Length': 1, 'FieldMSB': 4, 'FieldLSB': 4, 'Attribute': '000NNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)

#Enabling digital TMUX
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x1)
I2C_WRITE(device_address="0x68", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x21)

LH_Th = 2.25  # 2.25V threshold
error_spread = LH_Th*0.1 # 10% error spread
code_width = 5  # 5 bits trimming code
min_error = float('inf')
optimal_code = None
optimal_measured_value = None
force_voltage_low_limit = 0  # minimum voltage limit
force_voltage_high_limit = 3  # maximum voltage limit

for Code in range(2^code_width):
    # TODO: Write trimming code to device via I2C
    # Example (uncomment and fill device_address and field_info):
    I2C_WRITE(device_address="0x68", field_info={'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x60', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(Code))

    force_voltage = force_voltage_low_limit
    trigger = False

    while True:
        # Add noise simulation
        pvdd_forced_voltage = VFORCE(signal="PVDD", reference="GND", value=force_voltage,error_spread=error_spread)
        # Check trigger condition
        trigger = VTRIG_LH(signal="IODATA0", reference="GND", threshold=LH_Th, expected_value=pvdd_forced_voltage)

        if trigger:
            break
        elif pvdd_forced_voltage >= force_voltage_high_limit:
            print(f'..... Voltage max limit {force_voltage_high_limit}V crossed ........')
            break

        force_voltage += 0.005  # decrease voltage by 5mV
        sleep(0.001)  # 1 ms delay

    error = abs(pvdd_forced_voltage - LH_Th)/abs(LH_Th) * 100
    if error < min_error:
        min_error = error
        optimal_code = hex(Code)
        optimal_measured_value = pvdd_forced_voltage

# Final check and reporting
if force_voltage_low_limit < optimal_measured_value < force_voltage_high_limit:
    print(f'............ UVLO_Trim Test Passed ........')
    # TODO: Burn optimal trimming code to OTP via I2C
    I2C_WRITE(device_address="0x68", field_info={'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x60', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=optimal_code)
else:
    print(f'............ UVLO_Trim Test Failed ........')
    I2C_WRITE(device_address="0x68", field_info={'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x60', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)

print(f"Optimal Code: {optimal_code}")
print(f"Optimal Measured Value: {optimal_measured_value:.4f} V (Target: {LH_Th} V)")
print(f"Minimum Error: {min_error:.6f} %")
