import socket
import os

HOST = "127.0.0.1"
PORT = 65432
client_directory_path = r"C:\8200\homework_curse\digital_homework\FirstSocketConnection\all_client_files"


def clientHandeling():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((HOST, PORT)) # connecting to server using tuple!
        print("connected tp server")
       
           
        choice = input("enter 1 or 2 or 3 (1 means entering file into server, 2 means geting file form server,  3 means seeing all file avaible): ")
        soc.sendall(choice.encode())
        try:
                
            if(choice == "1"): # adding file into big directory on server
                print("choice 1 has been made, lets add add our file!")
                
                        # first sending the length of the fileName
                file_path = input("enter file path: ")
                        
                file_name = os.path.basename(file_path)

                soc.sendall(len(file_name).to_bytes(4, "big"))

                        # secondly sending the fileName
                        
                soc.sendall(file_name.encode())


                        # thirdly sending the length of the content
                with open (file_path, "r") as file:
                    
                        file_content =  file.read()
                        
                soc.sendall(len(file_content).to_bytes(4, "big"))
                
                        

                        # forthly sending the content of the file to the server
                soc.sendall(file_content.encode())
                
            
            elif choice == "2": # geting all file names from the server
                print("choice 2 has been made, lets see all the files the server holds!")
                
                file_names_length = int.from_bytes(my_recv(4, soc), "big")
                file_names = my_recv(file_names_length, soc).decode()
                print("the file names avaible from server are " + file_names)

            elif choice == "3": # geting one file from the server
                
                choocing_file = input("enter file (name) you want from server: ")
                
                # sending length of file name to server
                soc.sendall(len(choocing_file).to_bytes(4, "big"))
                # sending file name to server
                soc.sendall(choocing_file.encode())

                content_length = int.from_bytes(my_recv(4, soc), "big")
                file_content = my_recv(content_length, soc).decode()
               
                with open(f"{client_directory_path}\{choocing_file}", "w") as w:
                    w.write(file_content)

            else:
                print("wront input!")

        except:
            print("an error acured while trying to get the file into the server")





def my_recv(length, client_sock):
    content = b""
    while ( length > 0):
        temp_content = client_sock.recv(length)
        length -= len(temp_content)
        content += temp_content
    return content

       


            
if __name__ == '__main__':
    clientHandeling()
