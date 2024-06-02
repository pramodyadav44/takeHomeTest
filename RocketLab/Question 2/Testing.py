#import All the drivers
from Driver import EthernetDriver, RS422Driver, RS485Driver

#importing Device module
from Device import Device

def quick_test_procedure(device):
    """ Performing quick test Procedure """
    print("Starting Quick Test Procedure...")
    device.initialize()
    result = device.send_command("QUICK")
    device.shutdown()
    return result

def full_test_procedure(device):
    """ Performing full test Procedure """
    print("Starting Full Test Procedure...")
    device.initialize()
    result = device.send_command("FULL")
    device.shutdown()
    return result

# Testing Ethernet device
ethernet_device = Device(EthernetDriver())
quick_test = quick_test_procedure(ethernet_device)
print(f"Quick Test Result: {'Pass' if quick_test else 'Fail'} \n")

# Testing Given RS422 Driver
rs422_device = Device(RS422Driver())
full_test = full_test_procedure(rs422_device)
print(f"Full Test Result: {'Pass' if full_test else 'Fail'} \n")

# Testing RS-485 Driver
rs485_device = Device(RS485Driver())
full_test = full_test_procedure(rs485_device)
print(f"Full Test Result: {'Pass' if full_test else 'Fail'} \n")

#help(quick_test_procedure)
#help(full_test_procedure)

