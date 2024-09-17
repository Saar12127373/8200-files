# import socket


# #recover all data sent                          
# def recv_all(length, client_sock):
#     content = b""
#     while(length > 0):
#         tempContent = client_sock.recv(length)
#         length -= len(tempContent)
#         content += tempContent
#     return content




# def send_message(message):

#     # Convert message to bytes and send length
#     message_bytes = message.encode()
#     msg_len = len(message_bytes)
#     msg_len_bytes = msg_len.to_bytes(4, byteorder='big')
#     client_socket.sendall(msg_len_bytes)

#     # Send message
#     client_socket.sendall(message_bytes)



# def recv_response():
#     # Receive response

#     #response_len = int.from_bytes(recv_all(4, client_socket), byteorder='big')
    
#     #response_data = recv_all(response_len, client_socket)
    
#     response_data = recv_all(1024, client_socket)

#     print(f"Received response: {response_data.decode()}")


#     client_socket.close()

# if __name__ == "__main__":
#     server_address = ("127.0.0.1", 8543)  # Replace with the server's IP and port
#     message = "Hello from the client!"
    
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect(server_address)
    
#     #send_message(message)

#     recv_response()
    
    import base64

    print(base64.b64decode("bWdkZjMyZ2Y0M0AAAAAAAA=="))