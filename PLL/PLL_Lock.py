from dfttools import *
from time import sleep
from Procedures.Startup import startup

def pll_lock_test():
    Test_Name = 'PLL_Lock'
    print(f'............ {Test_Name.lower()} ........')
    pll_target_value_1 = 12.288e6                 # 12.288MHz
    BLCK_Set_1 = 3.072e6                          # 3.072MHz
    pll_target_value_2 = 13.68e6                  # 13.6MHz
    BLCK_Set_2 = 3.4e6                            # 3.4MHz
    pll_error_spread_1 = pll_target_value_1*0.01  # 1% of target value
    pll_error_spread_2 = pll_target_value_2*0.01  # 1% of target value
    '''
      Wait for 100us, check lock signal is high
      Bring out on the digital test point the PLL output and measure the frequency. It must be 12.288MHz
      Measure the Output Frequency. It must be 13.6MHz 
     '''
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_mode', 'length': 2, 'registers': [{'REG': '0x84', 'POS': 6, 'RegisterName': 'PLL_REG_5', 'RegisterLength': 8, 'Name': 'pll_mode[1:0]', 'Mask': '0xC0', 'Length': 2, 'FieldMSB': 1, 'FieldLSB': 0, 'Attribute': 'NNNNNNNN', 'Default': '0x17', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(2))      #dig_pll_freerun_en_vddd=0
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_p', 'length': 6, 'registers': [{'REG': '0x81', 'POS': 0, 'RegisterName': 'PLL reg 2', 'RegisterLength': 8, 'Name': 'pll_p[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': '00NNNNNN', 'Default': '0x06', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(6))         #dig_pll_prediv_vddd<5:0>=6d 
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_n', 'length': 6, 'registers': [{'REG': '0x82', 'POS': 0, 'RegisterName': 'PLL reg 3', 'RegisterLength': 8, 'Name': 'pll_n[5:0]', 'Mask': '0x3F', 'Length': 6, 'FieldMSB': 5, 'FieldLSB': 0, 'Attribute': '00NNNNNN', 'Default': '0x18', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(24))        #dig_pll_n<5:0>=24d 
    I2C_WRITE(device_address="0x38",field_info={'fieldname': 'pll_ldet_cnt', 'length': 5, 'registers': [{'REG': '0x83', 'POS': 0, 'RegisterName': 'PLL reg 4', 'RegisterLength': 8, 'Name': 'pll_ldet_cnt[4:0]', 'Mask': '0x1F', 'Length': 5, 'FieldMSB': 4, 'FieldLSB': 0, 'Attribute': '000NNNNN', 'Default': '0x00', 'User': '000YYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]},write_value=hex(16)) #rfu_pll_ldet_cnt<4:0>=16d
    FREQFORCE(signal="IOCLK0",reference="GND",value=BLCK_Set_1)                          #BCLK frequency=3.072MHz
    sleep(0.0001)                                                                    #wait 100us
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'i2c_page_sel', 'length': 1, 'registers': [{'REG': '0xFE', 'POS': 0, 'RegisterName': 'Page selection', 'RegisterLength': 8, 'Name': 'i2c_page_sel', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': '000000YY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1)  #Change page in regmap
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_en', 'length': 7, 'registers': [{'REG': '0x03', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_1', 'RegisterLength': 8, 'Name': 'dig_test_en[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x18)  #enable "ADDR" and "IODATA1" TMUX
    I2C_WRITE(device_address="0x38", field_info={'fieldname': 'dig_test_sel', 'length': 7, 'registers': [{'REG': '0x04', 'POS': 0, 'RegisterName': 'DIGITAL_TEST_SETTINGS_2', 'RegisterLength': 8, 'Name': 'dig_test_sel[6:0]', 'Mask': '0x7F', 'Length': 7, 'FieldMSB': 6, 'FieldLSB': 0, 'Attribute': '0NNNNNNN', 'Default': '0x00', 'User': '00000000', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG1'}]}, write_value=0x23) #bring out the pll output on "IODATA1" and pll lock on "ADDR"
  
    lock_status=VMEASURE(signal="ADDR", reference="GND", expected_value=0.9, error_spread=0.5) #measure the lock signal on "ADDR" pin
  
    pll_measured_value_1 = FREQMEASURE(signal="IODATA1", reference="GND", expected_value=pll_target_value_1, error_spread=pll_error_spread_1) #measure the frequency on "IODATA1" pin
    VMEASURE(signal="ADDR", reference="GND", expected_value=float('Inf')) # remove switch
    if (pll_target_value_1 - pll_error_spread_1) < pll_measured_value_1 < (pll_target_value_1 + pll_error_spread_1) and (lock_status > 0.9):
      # check for the intial lock frequency pass 12.288MHz and lock signal is high
      # BCLK frequency=3.072MHz
      FREQFORCE(signal="IOCLK0",reference="GND",value=BLCK_Set_2)                          #move to the second BCLK frequency=3.4MHz
      sleep(0.0001)                                                                    #wait 100us
      pll_measured_value_2 = FREQMEASURE(signal="IODATA1", reference="GND", expected_value=pll_target_value_2, error_spread=pll_error_spread_2)
      if (pll_target_value_2 - pll_error_spread_2) < pll_measured_value_2 < (pll_target_value_2 + pll_error_spread_2):
        # check for the intial lock frequency pass 13.6MHz
        #  BCLK frequency=3.4MHz
        print(f'.... {Test_Name.lower()}.., Passed....')
        print(f'Initial Lock signal = {lock_status}V')
        print(f'BCLK = {BLCK_Set_1 / 1e6}MHz , pll Freq Measured : {pll_measured_value_1 / 1e6}MHz')
        print(f'BCLK = {BLCK_Set_2 / 1e6}MHz , pll Freq Measured : {pll_measured_value_2 / 1e6}MHz')
      else:
        print(f'.... {Test_Name.lower()}.., Frequency Locking Failed ....')
        print(f'BCLK = {BLCK_Set_2 / 1e6}MHz , pll Freq Measured : {pll_measured_value_2 / 1e6}MHz')
    else:
      print(f'.... {Test_Name.lower()}.., Initial Frequency Locking Failed ....')
      print(f'BCLK = {BLCK_Set_1 / 1e6}MHz , pll Freq Measured : {pll_measured_value_1 / 1e6}MHz')
    FREQMEASURE(signal="IODATA1", reference="GND", expected_value=float('Inf')) # remove switch
if __name__ == "__main__":
    pll_lock_test()
