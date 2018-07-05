from netmiko import ConnectHandler

class Router(object):
    def __init__(self, hostname=None, os=None, device_type='cisco_ios', ip=None, username='cisco', password='cisco', secret='cisco'):
        self.hostname = hostname
        self.os = os
        self.interfaces = 2
        self.device_type = device_type
        self.ip = ip
        self.username = username
        self.password = password

    def show_interface(self):
        self.net_connect = ConnectHandler(device_type=self.device_type, ip=self.ip, username=self.username, password=self.password)
        output = self.net_connect.send_command('show ip int brief')
        return output

    def save_config(self):
        self.net_connect = ConnectHandler(device_type=self.device_type, ip=self.ip, username=self.username, password=self.password)
        output = self.net_connect.send_command_expect('write memory')
        return output

    def check_cdp(self):
        self.net_connect = ConnectHandler(device_type=self.device_type, ip=self.ip, username=self.username, password=self.password)
        output = self.net_connect.send_command('show run | i cdp')
        return output 

    def turn_off_cdp(self):
        self.net_connect = ConnectHandler(device_type=self.device_type, ip=self.ip, username=self.username, password=self.password) 
        self.net_connect.enable()
        config_commands = ['no cdp run']
        output = self.net_connect.send_config_set(config_commands)
        return output

if __name__ == "__main__":
    r1 = Router(hostname='lax-tor-r1', os='iosv', device_type='cisco_ios', ip='172.16.1.17', username='cisco', password='cisco')
    print("router interface count: " + str(r1.interfaces))
    output = r1.show_interface()
    print(output)



