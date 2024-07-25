import socket
import keyboard
import pyautogui

HOST = "10.0.0.8"
PORT = 65432


def recv_all(length, client_sock):
    content = b""
    while(length > 0):
        tempContent = client_sock.recv(length)
        length -= len(tempContent)
        content += tempContent
    return content




soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect((HOST, PORT))
print("server connectes! ")


# open file and ensuring it will me empty

while True:
    # Receive choice
    recieve_choice = recv_all(1, soc)
    
    # 1 is keyboard controling:
    if recieve_choice == b"1":
        # Receive key press

        recieve_key_length = int.from_bytes(recv_all(1, soc), "big")

        recieve_key_down = recv_all(recieve_key_length, soc).decode()

        pyautogui.keyDown(recieve_key_down)
        
        print(recieve_key_down)
    
    # get key released
    elif(recieve_choice == b"2"):
        
        key_len = int.from_bytes(recv_all(1, soc), "big")

        recieve_key_up = recv_all(key_len, soc).decode()
        pyautogui(recieve_key_up)

    # recieve all movements and to them yourself
    # elif(recieve_choice == b"3"):
    #     recieve_x_cords = int.from_bytes(recv_all(2, soc), "big")

    #     recieve_y_cords = int.from_bytes(recv_all(2,soc), "big")

    #     pyautogui.moveTo(recieve_x_cords, recieve_y_cords)



    # elif(recieve_choice == "3"):
    #     pass


    # elif(recieve_choice == "4"):
    #     pass


    # elif(recieve_choice == "5"):
    #     pass

    # else:
    #     pass