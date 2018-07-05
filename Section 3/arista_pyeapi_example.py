#!/usr/bin/env python
# Example from https://eos.arista.com/introducing-the-python-client-for-eapi-pyeapi/
#

import pyeapi, pprint

node = pyeapi.connect_to('veos01')

print('show version output')
pprint.pprint(node.enable('show version'))

print('show multiple command output')
pprint.pprint(node.enable(['show version', 'show ip route']))

print('configure with single line')
node.config('hostname veos01')

print('configure multiline configuration')
node.config(['interface Management1', 'description management interface'])

