from __future__ import print_function
from tor_inventory import devices
from router_object_v2 import Router

# grab the first device from inventory
print("This is the first device in inventory: " + str(devices[0]))
router = devices[0]
for key, value in router.items():
    d = Router(hostname=key, os='iosv', **value)
    output = d.check_cdp()
    if output == 'no cdp run': 
        print("cdp is turned off")
    else: 
        print("turning off cdp")
        output = d.turn_off_cdp()
        print(output)



