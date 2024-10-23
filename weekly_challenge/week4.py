# needs to return if thers a sum taht wil lgive me s

def is_sum(s, arr):
    i = 0
    y = len(arr - 1)

    while(arr[i] < arr[y]): 
        if(arr[i] + arr[y] == s):
            return True
        elif(arr[i] + arr[y] < s):
            i += 1
        else:
            y -= 1