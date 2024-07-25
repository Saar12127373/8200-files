import hashlib

hashed_password = "3cc6520a6890b92fb55a6b3d657fd1f6"


for i in range(1000000):

    i = str(i)

    hash = hashlib.md5()

    hash.update(i.encode())

    hash_hex = hash.hexdigest()
    if(hash_hex == hashed_password):
        print(i)