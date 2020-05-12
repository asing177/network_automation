from netaddr import *
import json
import sys
import multiprocessing

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
        self._lock = multiprocessing.Lock()
    
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
            self.ip_set.add(IPRange(start_ip,end_ip))
        else:
            self.ip_set.add(IPAddress(ip_address))

        self.write_to_file()
        
    
    def remove(self, ip_address):
        if "/" in ip_address:
            self.ip_set.remove(IPNetwork(ip_address))
        elif "-" in ip_address:
            start_ip , end_ip = ip_address.split("-")
            self.ip_set.remove(IPRange(start_ip,end_ip))
        else:
            self.ip_set.remove(IPAddress(ip_address))

        self.write_to_file()
    

    def check(self, ip_address):
        if "/" in ip_address:
            if IPNetwork(ip_address) in self.ip_set:
                return {"result" : f"{ip_address} is present" }
            else:
                return {"result" : f"{ip_address} is not present" }
        elif "-" in ip_address:
            start_ip , end_ip = ip_address.split("-")
            if IPRange(start_ip,end_ip) in self.ip_set:
                return {"result" : f"{ip_address} is present" }
            else:
                return {"result" : f"{ip_address} is not present" }
        else:
            if IPAddress(ip_address) in self.ip_set:
                return {"result" : f"{ip_address} is present" }
            else:
                return {"result" : f"{ip_address} is not present" }
    
    def summarize_network(self):
        return cidr_merge(self.ip_set)

    
    def write_to_file(self):
        summarized_net = self.summarize_network()
        with self._lock:
            try:
                with open("file.txt" , "w") as f:
                    f.write("\n".join(str(item) for item in summarized_net))
            except IOError as e:
                print (f"I/O error({e.errno}): {e.strerror}")
            except:
                print ("Unexpected error:", sys.exc_info()[0])




network_list = Network()
network_list.add("11.11.11.0/24")     
network_list.remove("11.11.11.10-11.11.11.20")  
r = network_list.check("11.11.11.21")