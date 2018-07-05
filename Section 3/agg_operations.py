#!/usr/bin/env python

from __future__ import print_function
from router_object_v3 import Router
import sqlite3, ast

# Retrieve device information from SQL Database
conn = sqlite3.connect('networks.db')
c = conn.cursor()

# Query for specific device
t = ('lax-agg-r1',)
c.execute('SELECT * FROM devices WHERE hostname=?', t)
device = c.fetchone()
conn.close()

# unpacking returned information 
hostname = device[0]
device_attributes = device[1]
print("Device hostname: %s attribute: %s" % (hostname, device_attributes)) 

# instanciate router object with our model
print('*' * 10)
attr = ast.literal_eval(device_attributes) # string to dict
d = Router(hostname=hostname, os='nxos', **attr)
output = d.show_interface()
print(output)
d.configure_vlan(100)
output = d.show_vlan()
print(output)
print('saving config...')
output = d.save_config()


