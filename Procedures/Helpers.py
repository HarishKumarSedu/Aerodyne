from dfttools import *
from time import sleep
import random 
from dfttools import *
from time import sleep

def SWEEP_CODE_TRIGHL_VFORCE(field_info={},force_signal='',force_reference='',trig_signal='',trig_reference='',target=0,force_low_limit=0,force_high_limit=0,error_percentage=0):
    HL_Th = target
    error_spread = target*error_percentage
    min_error = float('inf')
    optimal_code = None
    optimal_measured_value = None
    if field_info:
        code_width = field_info.get('length')
        for Code in range(2**code_width):
            # TODO: Write trimming code to device via I2C
            # Example (uncomment and fill device_address and field_info):
            I2C_WRITE(device_address="0x68", field_info=field_info, write_value=hex(Code))
            force_voltage = force_high_limit
            trigger = False
            while True:
                # Add noise simulation
                forced_voltage = VFORCE(signal=force_signal, reference=force_reference, value=force_voltage,error_spread=error_spread)
                # Check trigger condition
                trigger = VTRIG_HL(signal=trig_signal, reference=trig_reference, threshold=HL_Th, expected_value=force_voltage)
                if trigger:
                    break
                elif forced_voltage <= force_low_limit:
                    print(f'..... Voltage min limit {force_low_limit}V crossed ........')
                    break
                force_voltage -= 0.05  # decrease voltage by 50mV
                sleep(0.01)  # 10 ms delay
            error = abs(forced_voltage - HL_Th)/abs(HL_Th) * 100
            if error < min_error:
                min_error = error
                optimal_code = hex(Code)
                optimal_measured_value = forced_voltage
        # Final check and reporting
        if force_low_limit < optimal_measured_value < force_high_limit:
          print(f'............ Test Passed ........')
          # TODO: Burn optimal trimming code to OTP via I2C
          I2C_WRITE(device_address="0x68", field_info={'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=optimal_code)
        else:
          print(f'............ Test Failed ........')
          I2C_WRITE(device_address="0x68", field_info={'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x0)
        return optimal_code,optimal_measured_value,min_error
    else:
        print('!!!!!!!!!!!!!!! error provide valid field !!!!!!!!!!!!!!!!!!!!!!')
# optimal_code,optimal_measured_value,min_error = SWEEP_CODE_TRIGHL_VFORCE(field_info={'fieldname': 'otp_ds_ref_pvdd_uvlo_trm', 'length': 5, 'registers': [{'REG': '0xB3', 'POS': 0, 'RegisterName': 'OTP FIELDS 3', 'RegisterLength': 8, 'Name': 'otp_ds_ref_pvdd_uvlo_trm[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG1'}]},force_signal='"IODATA0"',force_reference='"GND"',trig_signal='"PVDD"',trig_reference='"GND"',target=2.25,force_low_limit=0,force_high_limit=3.7,error_percentage=0.05)
# print(optimal_code,optimal_measured_value,min_error)