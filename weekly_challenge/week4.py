# needs to return if thers a sum taht wil lgive me s

def is_sum(s, arr):
    pointer1 = arr[0]
    pointer2 = arr[len(arr)]
    while pointer1 < pointer2:
        if(pointer1 + pointer2 == s):
            return True
        else:
            pointer1 = arr[]