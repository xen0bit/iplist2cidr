import netaddr
import ipaddress

#Controls the maximum mask applied to blocks
granularity = 512
ipInts = []
with open('list.txt', 'r') as ips:
    for ip in ips:
        print(ip)
        #Cast IP as int32
        ipInts.append(int(ipaddress.IPv4Address(ip.replace('\n','').replace('\r',''))))

#Sort the list of IP's cast as int32
ipInts.sort()

#Setup
startIpInt = ipInts[0]
#Shift array
ipInts = ipInts[1:]
accumulator = []
accumulator.append(str(ipaddress.IPv4Address(startIpInt)))
out = []
for ip in ipInts:
        if ip - startIpInt > granularity:
            try:
                out.append(str(netaddr.spanning_cidr(accumulator)))
            #There's only one IP within that granularity
            except ValueError:
                out.append(str(ipaddress.IPv4Address(startIpInt))+'/32')
            #Reset
            accumulator = []
            startIpInt = ip
        else:
            accumulator.append(str(ipaddress.IPv4Address(ip)))

print(out)
