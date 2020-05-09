from netaddr import *

net_list = []

class BlockList:
    def __init__(self):
        pass

    def block_ip(self):
        pass

    def block_ip_range(self):
        pass

    def block_ip_mask(self):
        pass

    def unblock_ip(self):
        pass

    def unblock_ip_range(self):
        pass

class IPList:
    def __init__(self):
        pass

    def create_network_list(self):
        with open("file.txt" , "r") as f:
            lines = f.readlines()
            for line in lines:
                if "/" in line:
                    net_list.append(IPNetwork(line))
                else:
                    net_list.append(IPAddress(line))
            
        self.net_list = net_list
        return net_list


    def check_ip_in_net_list(self, ip_address):
        for entry in self.net_list:
            if ip_address == entry:
                return True

    def check_ip_range_in_list(self, ip_range):
        pass

    def check_ip_mask_in_list(self,ip_mask):
        pass


class Network:
    def __init__(self, net_list):
        self.s1 = IPSet()

    def host_list(self):
        return self.s1

    def add_ip_to_set(self):
        self.s1.add(IPRange("10.0.0.0", "10.0.0.255"))


    def add_ip_range(self):
        self.s1.add(IPRange("10.0.0.0", "10.0.0.255"))


    def remove_ip_from_set(self):
        self.s1.remove('10.0.0.2')
        self.s1.remove('10.0.0.3')
        self.s1.remove(IPRange("10.0.0.128", "10.10.10.10"))




ip_list = IPList()
net_list = ip_list.create_network_list()

