# needs to return if thers a sum taht wil lgive me s

def is_sum(s, list1):
    for i in range (list1):
        if(list1[0] + list1[i] == s):
            return True
        