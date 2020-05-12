from netaddr import *
import json

class Network:
    def __init__(self):
        ip_set = IPSet()
        net_list = []
        with open("file.txt" , "r") as f:
            lines = f.readlines()
            for line in lines:
                if "/" in line:
                    net_list.append(line)
                    ip_set.add(IPNetwork(line))
                elif "-" in line:
                    net_list.append(line)
                    start_ip , end_ip = line.split("-")
                    ip_set.add(IPRange(start_ip, end_ip))
                else:
                    net_list.append(line)
                    ip_set.add(IPAddress(line))
        self.ip_set = ip_set
        self.net_list = net_list
        self._index = 0
    
    def __iter__(self): 
        return self

    
    def __next__(self): 
        if self._index < len(self.net_list):
            result = self.net_list[self._index]
            self._index += 1
            return result
        raise StopIteration

    
    def __repr__(self):
        return "Network List Object"
        

    def add(self, ip_address):
        if "/" in ip_address:
            self.ip_set.add(IPNetwork(ip_address))
        elif "-" in ip_address:
            start_ip , end_ip = ip_address.split("-")
            self.ip_set.add(IPRange(ip_address))
        else:
            self.ip_set.add(IPAddress(ip_address))

        self.write_to_file()
        
    
    def remove(self, ip_address):
        if "/" in ip_address:
            self.ip_set.remove(IPNetwork(ip_address))
        elif "-" in ip_address:
            start_ip , end_ip = ip_address.split("-")
            self.ip_set.remove(IPRange(ip_address))
        else:
            self.ip_set.remove(IPAddress(ip_address))
        self.write_to_file()
    

    def check(self, ip_address):
        if "/" in ip_address:
            if IPNetwork(ip_address) in self.ip_set:
                return True
            else:
                return False
        elif "-" in ip_address:
            start_ip , end_ip = ip_address.split("-")
            if IPRange(start_ip,end_ip) in self.ip_set:
                return True
            else:
                return False
        else:
            if IPAddress(ip_address) in self.ip_set:
                return {"result" : "f'{ip_address}'"}
            else:
                return False

    
    def write_to_file(self):
        with open("file.txt" , "w+") as f:
            f.write(ip_set)



network_list = Network()
r = network_list.check("1.1.1.1")
print(r)
        