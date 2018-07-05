#
# https://github.com/datacenter/nxos/blob/master/nxapi/samples/show_version.py
# Print Chassis info, Hostname and software version of a given switch.
#

import json
import requests

ip="172.16.1.12"

my_headers = {'content-type': 'application/json-rpc'}
url = "http://"+ip+"/ins"
username = "cisco"
password = "cisco"


payload=[{"jsonrpc": "2.0",
          "method": "cli",
          "params": {"cmd": "show version",
                     "version": 1},
          "id": 1}
         ]

response = requests.post(url, data=json.dumps(payload), headers=my_headers, auth=(username, password)).json()

#Now Process the response
kick_start_image = response['result']['body']['kickstart_ver_str']
chassis_id = response['result']['body']['chassis_id']
hostname =  response['result']['body']['host_name']

print "ip : {0} is a \"{1}\" with hostname: {2} running software version : {3}".format(ip , chassis_id, hostname, kick_start_image)



