import hashlib
import time

six_digits = "052538"

for i in range(10):
    for j in range(10):
        for k in range(10):
            for q in range(10):
                combined_string = six_digits + str(i) + str(j) + str(k) + str(q)
                if hashlib.md5(combined_string.encode()).hexdigest() == "6688795677c1c8f2d3cd14b710f60153":
                    print(six_digits + str(i) + str(j) + str(k) + str(q))
# print(len(hashlib.md5(six_digits.encode() + ).hexdigest()))

# print(len("6688795677c1c8f2d3cd14b710f60153"))