from time import sleep
import os 
import sys
# example code to install python pacakage
# command = f"{sys.executable} -m pip uninstall dfttools -y"
# os.system(command)
# command = f"{sys.executable} -m pip install git+https://github.com/HarishKumarSedu/dfttools.git@main"
# os.system(command)

Test_Name = 'Startup'
print(f'............ {Test_Name} ........')
from dfttools import *
# VFORCE(signal="VDD",reference="GND",value=1.8)
# VFORCE(signal="RESETB",reference="GND",value=1.8)
VFORCE(signal="PVDD",reference="GND",value=3.7)

sleep(0.2)

# Switch to page 1
I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x01,PageNo=1)
# Unlock test page 
I2C_REG_WRITE( device_address="0x38", register_address=0x2F, write_value=0xAA,PageNo=1)
I2C_REG_WRITE( device_address="0x38", register_address=0x2F, write_value=0xBB,PageNo=1)
# Switch to page 0
I2C_REG_WRITE( device_address="0x38", register_address=0xFE, write_value=0x00,PageNo=0)

