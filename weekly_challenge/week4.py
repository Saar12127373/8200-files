# needs to return if thers a sum taht wil lgive me s

def is_sum(s, arr):
    i = 0
    y = len(arr)
    pointer1 = arr[i]
    pointer2 = arr[y]
    while pointer1 < pointer2:
        if(pointer1 + pointer2 == s):
            return True
        else:
            i += 1
            pointer1 = arr[i]