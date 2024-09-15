import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))  # Replace with your desired IP and port
server_socket.listen()
print("server is listening")
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}") 



#recover all data sent                          
def recv_all(length, client_sock):
    content = b""
    while(length > 0):
        tempContent = client_sock.recv(length)
        length -= len(tempContent)
        content += tempContent
    return content




def handle_client(client_socket):
    while True:
        msg_len = int.from_bytes(recv_all(4, client_socket), "big")
        data = recv_all(msg_len, client_socket)

        if not data:
            break
        print(f"Received: {data.decode()}")


        msg_to_client = "Message received!"

        # Convert message to bytes and send length
        message_bytes = msg_to_client.encode()
        client_socket.sendall(len(message_bytes).to_bytes(4, byteorder='big'))

    # Send message
        client_socket.sendall(msg_to_client.encode())
    



    client_socket.close()

 

if __name__ == "__main__":
    handle_client(client_socket)
    server_socket.close()
    