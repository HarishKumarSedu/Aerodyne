from dfttools import *
from time import sleep
from Procedures.Startup import startup
from Procedures.VI_SNS_turn_on import vi_sns_turn_on

def vis_2ua_curr1_meas():
    Test_Name = 'VIS_2uA_Curr1_Meas'
    print(f'............ {Test_Name} ........')
    startup()
    vi_sns_turn_on()
    '''
    VIS 2uA Current Source Measurement
    -------------------------------------------------
    1. Power up with VI-sense enabled, main bandgap trimmed
    2. Configure VIS channels and route current to "ADDR"
    3. Measure 0.5uA current at "IODATA1" pin
    '''
    # Step 2: Settling Time
    sleep(0.0005)  # 500 us
    # Step 3: Route Current to "IODATA1"
    I2C_REG_WRITE(device_address="0x38", register_address=0xFE, write_value=0x01, PageNo=1)  # Change page in regmap
    I2C_WRITE("0x38", field_info={'fieldname': 'vis_atp_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'vis_atp_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(1))  # Enable test mux
    I2C_WRITE("0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=hex(4))  # Enable tests 1uA current
    # Step 4: Current Measurement
    expected_curr = 0.5e-6    # 0.5 uA target
    curr_error = 0.05e-6      # ±0.05 uA tolerance
    imeas = AMEASURE(signal="IODATA1", reference="GND", expected_value=expected_curr, error_spread=curr_error)
    print(f'Measured Current: {imeas * 1e6:.3f} uA [Target: {expected_curr * 1e6:.1f}uA ±{curr_error * 1e6:.1f}uA]')
    # Pass/Fail Criteria
    AMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf'))
    if abs(imeas - expected_curr) <= curr_error:
        print("PASS: Current within ±0.05uA specification")
    else:
        print(f"FAIL: Current error {abs(imeas - expected_curr) * 1e6:.1f}uA exceeds limit")
    I2C_WRITE("0x38", field_info={'fieldname': 'vis_atp_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 1, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'vis_atp_en', 'Mask': '0x2', 'Length': 1, 'FieldMSB': 1, 'FieldLSB': 1, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)  # disable analog test mux
    I2C_WRITE("0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)  

if __name__ == "__main__":
    vis_2ua_curr1_meas()
