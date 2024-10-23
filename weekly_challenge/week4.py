# needs to return if thers a sum taht wil lgive me s

def is_sum(s, arr):
    i = 0
    y = len(arr - 1)

    while True:
        if(arr[i] + arr[y] == s):
            return True
        if(arr[i] < arr[y]):
            i += 1
        else:
            y -= 1
