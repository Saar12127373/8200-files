# server side:
import socket
import keyboard
import pyautogui
from pynput import mouse
from PIL import Image
from pynput import keyboard


HOST = ""
PORT = 8090
myDict = {}
# creating socket, specifing ipv4 and tcp
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# as a tuple giving ip and port
soc.bind((HOST, PORT))
    # waiting for connection
soc.listen(1)
print("Server is listening!")

# client sock is a new socket object for send and recv msg
# client addr is the ip and port 
        
client_sock, client_addr = soc.accept()

# recover all data sent
def recv_all(length, client_sock):
    content = b""
    while(length > 0):
        tempContent = client_sock.recv(length)
        length -= len(tempContent)
        content += tempContent
    return content


# 
def keyDown(event):
    # Sending choice for key down
    # client_sock.sendall(b"1")

    
    # if len(button) != 1:
    #     button = event.name

    

    
    # key_len = len(button)
    # client_sock.sendall(key_len.to_bytes(1, "big"))
    

    # Sending the key that was pressed
    # client_sock.sendall(button.encode())
    # print(f"Key down: {button}")
    # vk = event.value.vk
    # val = 0
    # print(vk)
    val = 0
    vk = 0
    try:
        val = event.name
        vk = event.value.vk
    except:
        val = event.char
        vk = event.vk
        
    
    myDict[vk] = val

def keyUp(event):
    # Sending choice for key up
    print(myDict)
    # client_sock.sendall(b"2")

    # button = str(event)

    # key_len = len(button)
    # client_sock.sendall(key_len.to_bytes(1, "big"))
    
    # # Sending the key that was released
    # client_sock.sendall(button.encode())
    # print(f"Key up: {button}")


# def MousePositian(x,y):
#     client_sock.sendall(b"3")

#     currentMouseX, currentMouseY = int(x), int(y)
#     # placment will be between 1 -2 bytes so not worth sending length
#     #sending placements
#     client_sock.sendall(currentMouseX.to_bytes(2,"big"))
#     client_sock.sendall(currentMouseY.to_bytes(2, "big"))





with keyboard.Listener(on_press=keyDown, on_release=keyUp) as listener:
    listener.join()

# with mouse.Listener(on_move=MousePositian) as listener:
#     listener.join()i love my girlfrienda

keyboard.wait("esc")

client_sock.close()
soc.close()




