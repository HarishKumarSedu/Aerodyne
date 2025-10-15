from dfttools import *
from time import sleep
from Procedures.Startup import startup
from Procedures.Global_enable import global_enable
def pll_vdd_bias_vdd():
    Test_Name = 'PLL_VCO_Bias_VDD'
    print(f'............ {Test_Name.lower()} ........')
    startup()
    global_enable()
    pll_vddvco_target_value = 0.68  # 680mV target VDD_VCO
    BLCK_Set = 3.072e6              # 3.072MHz
    pll_vddvco_error_spread = pll_vddvco_target_value * 0.01  # 1% of target value
    '''
      3.Bring out on the analog test point the "VDD" VCO voltage. Measure it with a high input impedance voltmeter
      4.Target value is around 680mV (typ)
    '''
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_mode', 'length': 2, 'registers': [{'REG': '0x84', 'POS': 6, 'RegisterName': 'PLL_REG_5', 'RegisterLength': 8, 'Name': 'pll_mode[1:0]', 'Mask': '0xC0', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x17', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(2))      #dig_pll_freerun_en_vddd=0
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_p', 'length': 6, 'registers': [{'REG': '0x81', 'POS': 0, 'RegisterName': 'PLL reg 2', 'RegisterLength': 8, 'Name': 'pll_p[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': '00NNNNNN', 'Default': '0x06', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(6))         #dig_pll_prediv_vddd<5:0>=6d 
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_n', 'length': 6, 'registers': [{'REG': '0x82', 'POS': 0, 'RegisterName': 'PLL reg 3', 'RegisterLength': 8, 'Name': 'pll_n[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': '00NNNNNN', 'Default': '0x18', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(24))        #dig_pll_n<5:0>=24d 
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_ldet_cnt', 'length': 5, 'registers': [{'REG': '0x83', 'POS': 0, 'RegisterName': 'PLL reg 4', 'RegisterLength': 8, 'Name': 'pll_ldet_cnt[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': '000NNNNN', 'Default': '0x10', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(16)) #rfu_pll_ldet_cnt<4:0>=16d
    FREQFORCE(signal="IOCLK0",reference="GND",value=BLCK_Set)                            #BCLK frequency=3.072MHz
    sleep(0.0001)                                                                    #wait 100us
    '''
    Bring out all the necessary signals 
    '''
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)  #Change page in regmap
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pll_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'pll_test_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)   #enable ANA_TESTMUX1
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)   #enable "IODATA1"
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=1)      #enable VDD_VCO voltage test
    pll_measured_vddvco_voltage = VMEASURE(signal="IODATA1", reference="GND", expected_value=pll_vddvco_target_value,
                                          error_spread=pll_vddvco_error_spread)        #measure with amperometer shorted to ground
    error = abs(pll_measured_vddvco_voltage - pll_vddvco_target_value) / abs(pll_vddvco_target_value) * 100
    print(f"Measured VDDVCO value : {pll_measured_vddvco_voltage} V, Target value : {pll_vddvco_target_value} V")
    print(f"Percentage Error: {error}%")
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'pll_test_en', 'length': 1, 'registers': [{'REG': '0x16', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN1', 'RegisterLength': 8, 'Name': 'pll_test_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)   #enable ANA_TESTMUX1
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'atp_p_en', 'length': 1, 'registers': [{'REG': '0x17', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_EN2', 'RegisterLength': 8, 'Name': 'atp_p_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000NNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)   #enable "IODATA1"
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'test_sel', 'length': 4, 'registers': [{'REG': '0x15', 'POS': 0, 'RegisterName': 'ANA_TESTMUX_SEL', 'RegisterLength': 8, 'Name': 'test_sel[3:0]', 'Mask': '0xF', 'Length': 4, 'FieldMSB': 3, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0)      #enable VDD_VCO voltage test
    VMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf')) # open path 
if __name__ == "__main__":
    pll_vdd_bias_vdd()
