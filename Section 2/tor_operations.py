#!/usr/bin/env python

from __future__ import print_function
from tor_inventory import devices
from router_object_v2 import Router

# List inventory file and values (optional)
print("Loop thru all devices")
for d in devices: 
    for key, value in d.items():
        print(key, d[key])

# grab the first device from inventory for further operation
print("This is the first device in inventory: " + str(devices[0]))
router = devices[0]
for key, value in router.items():
    print("Key is the hostname: " + key)
    print("Unpacking individual values: " + router[key]['device_type'] + " " + router[key]['ip'])
    d = Router(hostname=key, os='iosv', **value)
    output = d.show_interface()
    print(output)
    output = d.save_config()
    print(output)


