import socket
import os
HOST = "127.0.0.1"
PORT = 65432
folder_path = r"C:\8200\homework_curse\digital_homework\FirstSocketConnection\all_server_files"
                





def serverHandeling():
    # CREATING socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        # allocating port to a socket (binding) using tuple!
        soc.bind((HOST, PORT))
        # waiting for a client(socket object)
        soc.listen(3)
        # accepting connection - new socket object
        print("Server is listening")
        client_sock, client_addr = soc.accept()
        # conn is a new socket object to send and recv data
        # addr is the ip and port number used by the client
        print(f"connectiong is established form {client_addr}" )
            


        # choocing what to do:
        choice = my_recv(1, client_sock).decode()
                
        if(choice == "1"): # means to put file in the server folder
                    
            # getting from client:name length and name-
            file_name_length = int.from_bytes(my_recv(4, client_sock), "big")
            
            
            file_name = my_recv(file_name_length, client_sock).decode()


                # getting from client: content length and content-
            file_content_length = int.from_bytes(my_recv(4, client_sock), "big")
            file_content = my_recv(file_content_length, client_sock).decode()

                # creating a file in the known directory and writing into it the content:
                    
            with open(f"{folder_path}\{file_name}", 'w') as f: 
                f.write(file_content) 


                print(f"the file {file_name} added to folder, using {file_content_length} bytes")


        elif(choice == "2"):
            file_names = []
            for file_name in os.listdir(folder_path):
                file_names.append(file_name)
            file_names_str = ", ".join(file_names)
           
            file_name_length = len(file_names_str)

            client_sock.sendall(file_name_length.to_bytes(4, "big"))
            client_sock.sendall(file_names_str.encode())

        elif choice == "3":
            # the file name and its length - the client chose
            file_name_length = int.from_bytes(my_recv(4, client_sock), "big")
            file_name = my_recv(file_name_length, client_sock).decode()

            with open (f"{folder_path}\{file_name}", "r") as f:
                content = f.read()
            # file length and content

            client_sock.sendall(len(content).to_bytes(4, "big"))
            client_sock.sendall(content.encode())



def my_recv(length, client_sock):
    content = b""
    while ( length > 0):
        temp_content = client_sock.recv(length)
        length -= len(temp_content)
        content += temp_content
    return content

            
                
if __name__ == '__main__':
    serverHandeling()