from dfttools import *
def playback():
  Test_Name = 'Playback'
  # Reach the PLAYBACK state in the main FSM
  print(f'............ {Test_Name} ........')
  FREQFORCE(signal="IOCLK0",reference="GND",value=3.072e6)                          #BCLK frequency=3.072MHz
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'spk_en', 'length': 1, 'registers': [{'REG': '0x9F', 'POS': 0, 'RegisterName': 'Enables settings 5', 'RegisterLength': 8, 'Name': 'spk_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000S', 'Default': '0x00', 'User': '0000000Y', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1) 
  I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tdm_rx_en', 'length': 1, 'registers': [{'REG': '0x5E', 'POS': 0, 'RegisterName': 'TDM settings 16', 'RegisterLength': 8, 'Name': 'tdm_rx_en', 'Mask': '0x1', 'Length': 1, 'FieldMSB': 0, 'FieldLSB': 0, 'Attribute': '0000000N', 'Default': '0x00', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=1) # needed ?
  # I2C_WRITE(device_address="0x38", field_info={'fieldname': 'tdm_sync_mode', 'length': 1, 'registers': [{'REG': '0x4E', 'POS': 7, 'RegisterName': 'TDM settings 13', 'RegisterLength': 8, 'Name': 'tdm_sync_mode', 'Mask': '0x80', 'Length': 1, 'FieldMSB': 7, 'FieldLSB': 7, 'Attribute': 'NNNNNNNN', 'Default': '0x99', 'User': 'YYYYYYYY', 'Clocking': 'SMB', 'Reset': 'C', 'PageName': 'PAG0'}]}, write_value=0) # needed ?

if __name__ =='__main__':
    playback()