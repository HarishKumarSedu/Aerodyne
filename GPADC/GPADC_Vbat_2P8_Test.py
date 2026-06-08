from time import sleep
Test_Name = 'GPADC_Vbat_2P8_Test'
from Procedures.Startup import startup
def gpadc_vbat_2P8_test():
    print(f'............ {Test_Name} ........')
    startup()

    # designers must go through the details and correct the procedure
    '''
        Procedure 
        before to start the bandgap has to be trimmed
        1.Enable the SAR ADC with extenal clock
        2.Force VBAT at 2.8 V
        3.Measure VBAT and save the result in Variable VB0
        4.Measure the Vbat register after 8 average save in the Variable CODE0
        5. Check that 518<CODE0<522
    '''
    FREQFORCE(signal="IOCLK0",reference="GND",value=3.072e6)   # force clock 
    sleep(0.001)

    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x1)
    sleep(0.001)
    pvdd_forced_voltage = VFORCE(signal="PVDD", reference="GND", value=2.8,error_spread=0)
    sleep(0.01)
    VB0 = VMEASURE(signal="PVDD", reference="GND", expected_value=2.8,error_spread=0)
    sleep(0.001)
    expected_value=round(((VB0*22/(22+79))*1024/(0.6*2)))

    Vbat_min=expected_value-2
    Vbat_max=expected_value+2

    HCODE0=I2C_READ(device_address="0x38",field_info={'fieldname': 'vbat_meas', 'length': 10, 'registers': [{'REG': '0x23', 'POS': 0, 'RegisterName': 'VBAT measurement reg 1', 'RegisterLength': 8, 'Name': 'vbat_meas[9:8]', 'Mask': '0x3', 'Length': 2, 'FieldMSB': 9, 'FieldLSB': 8, 'Attribute': '000000RR', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}, {'REG': '0x24', 'POS': 0, 'RegisterName': 'VBAT measurement reg 2', 'RegisterLength': 8, 'Name': 'vbat_meas[7:0]', 'Mask': '0xFF', 'Length': 8, 'FieldMSB': 7, 'FieldLSB': 0, 'Attribute': 'RRRRRRRR', 'Default': '0x00', 'User': '00000000', 'Clocking': 'REF', 'Reset': 'C', 'PageName': 'PAG0'}]},expected_value=0x207)
    CODE0=int(HCODE0)

    if Vbat_min <= CODE0 <= Vbat_max:
      print(f'............ {Test_Name} Passed ........')
        # write the optimized code if the trim passed


    print(f"VBAT2P8 Code: {CODE0}")
    print(f"Vbat_min Code: {Vbat_min}")
    print(f"Vbat_max Code: {Vbat_max}")
    
    sleep(0.001)
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'global_en', 'length': 1, 'registers': [{'REG': '0x0F', 'POS': 0, 'RegisterName': 'GLOBAL_EN_REG', 'RegisterLength': 8, 'Name': 'global_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=0x0)

if __name__ == "__main__":
    gpadc_vbat_2P8_test()