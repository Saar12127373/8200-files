from scapy.all import sniff, DNS,DNSQR,Raw,TCP, IP
from scapy.layers import http
import socket

# captuer dns request packets, type A and print them

# def filter_dns(packet):
#     return (DNS in packet and packet[DNS].opcode == 0 and packet[DNSQR].qtype == 1)

# def print_query_name(dns_packet):
#     print(dns_packet[DNSQR].qname)

# # Sniff DNS packets
# packets = sniff(count=3, lfilter=filter_dns, prn= print_query_name)

# for packet in packets:
#     print(packet[DNSQR].qname)


def filter_HTTP(packet):
    return(TCP in packet and Raw in packet and packet[IP].src != "10.0.0.28")

def ip_to_hostname(ip_address):
    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        return hostname
    except socket.herror:
        return "Unknown hostname"


def turn_to_url(packet):
    ip_address = packet[IP].src
    hostname = ip_to_hostname(ip_address)
    print(f"Source IP: {ip_address} resolves to hostname: {hostname}")



sniff(count=1, lfilter=filter_HTTP, prn = turn_to_url )
