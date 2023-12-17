from scapy.all import *

COAP_PORT = 5683
interval = 0.5
num_of_packages = 7200
bytes = 400
ip = "192.168.1.102"

coap_packet = IP(dst=ip)/UDP(sport=12345, dport=COAP_PORT)/Raw(RandString(size=bytes))
send(coap_packet, inter=interval, loop=True, count=num_of_packages)