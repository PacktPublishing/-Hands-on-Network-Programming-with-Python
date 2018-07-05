#
# Example From: 
# https://xrdocs.io/application-hosting/tutorials/2016-08-15-netmiko-and-napalm-with-ios-xr-quick-look/
# 

from napalm import get_network_driver
import pprint

driver = get_network_driver('iosxr')

device = driver('172.16.1.13', 'cisco', 'cisco')
device.open()
pprint.pprint(device.get_facts())
pprint.pprint(device.get_interfaces())
device.close()

