#!/usr/bin/env python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

dev = Device(host='172.16.0.1', user='netconf', password='test123')
dev.open()
print(dev.facts)

with Config(dev, mode='private') as cu:
    cu.load('set system services netconf traceoptions file test.log', format='set')
    cu.pdiff()
    cu.commit()

dev.close()

