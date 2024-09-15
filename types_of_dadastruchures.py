import keyboard
import time
# def cx(x):
#     x = 7
#     return x

# x = 10
# cx(x)
# print(x)


# def mod_lst(lst):
#     lst.append(4)
#     mod_lst = [1]

# lst = [1,2,3]
# mod_lst(lst)
# print(lst)


# y = (1,2)
# print(y)
# print(id(y))

# y += (2,5)
# print(y)
# print(id(y))

# def receive_screenshot():
#     # i took down the part of checking the orded of the packets - the reason is: the deiffrence between the 
#     image_parts = [None] * 128

#     while data != b"2":
#         data, addr = screen_soc.recvfrom(65535)
        

#         if(data[2:3].isdigit()):
#             part_id_len = 7
#         elif(data[1:2].isdigit()):
#             part_id_len = 6
#         else:
#             part_id_len = 5

#         part_id = data[:part_id_len].decode()
#         part_data = data[part_id_len:]
        
#         # check the packet number:
#         part_number_str = part_id[4:]

#         part_index = int(part_number_str)


#         # if part_id == f'part{expected_part}':
#         image_parts[part_index] = part_data


# def load_Screnshot():
#     parts = [Image.open(io.BytesIO(part)) for part in image_parts]

#     # Ensure the width and height calculations match image layout
#     part_width, part_height = parts[0].size
#     width, height = part_width * 16, part_height * 8

#     full_image = Image.new('RGB', (width, height))

#     for i in range(8):
#         for j in range(16):
#             full_image.paste(parts[i * 16 + j], (j * part_width, i * part_height))

#     cv_image = np.array(full_image)
#     cv_image = cv_image[:, :, ::-1]  # from RGB to BGR
#     cv2.imshow('Live Video', cv_image)
#     cv2.waitKey(4)

# except Exception as e:
#     print(f"Error processing image: {e}")


# def handle_Screenshots():
    

# list = '123'

# print(list[1:3])


import base64

decoded = base64.b64decode("ODQxMjM0==")
print(decoded)
print(decoded.decode())


