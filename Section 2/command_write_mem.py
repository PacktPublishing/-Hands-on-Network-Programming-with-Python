#!/usr/bin/env python

from __future__ import print_function, unicode_literals
from netmiko import ConnectHandler

lax_tor_r1 = {
    'device_type': 'cisco_ios',
    'ip': '172.16.1.10',
    'username': 'cisco',
    'password': 'cisco',
    'secret': 'cisco',
    'verbose': False,
}

net_connect = ConnectHandler(**lax_tor_r1)
output = net_connect.send_command_expect('write memory')
print(output)


