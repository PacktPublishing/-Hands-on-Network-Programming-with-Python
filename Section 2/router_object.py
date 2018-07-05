class Router(object):
    def __init__(self, hostname, os):
        self.hostname = hostname
        self.os = os
        if self.os == "nxos":
            self.interfaces = 48
        else: 
            self.interfaces = 2

    def print_hostname(self):
        print("router hostname is " + self.hostname)


if __name__ == "__main__":
    r1 = Router("lax-tor-r1", "iosv")
    print("router interface count: " + str(r1.interfaces))
    r1.print_hostname()


