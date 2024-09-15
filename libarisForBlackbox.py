# hex_string = "\x69\x68\x61\x63\x6b\x79\x6f\x75"
# decoded_string = hex_string  # It's already decoded
# print(decoded_string) 


import hashlib

# string = "adidi"

# hex = hashlib.md5(string.encode()).hexdigest()

# print(hex)

import base64

# encoded_data = b'SGVsbG8sIHdvcmxkIQ=='

# decoded_data = base64.b64decode(encoded_data)
# print(decoded_data)

import socket

ip_addr = "127.0.0.1"
port_addr = 65211

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_sock.connect((ip_addr, port_addr))


msg = "i love adidi!"

# basic so now sending amount of bytes(msg length)
#client_sock.sendall(msg.encode())

# better...

client_sock.sendall(len(msg).to_bytes(4, "big"))
client_sock.sendall(msg.encode())