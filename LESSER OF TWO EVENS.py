LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd


def lesser(a,b):
    if a%2==0 and b%2==0:
        print(min(a,b))
    else:
        print(max(a,b))

a=lesser(2,5)


or



def lesser(a,b):
    if a%2==0 and b%2==0:    #Both are even
        if a<b:
            return a
        else:
            return b
    else:                   #both are not even
        if a>b:
            return a
        else:
            return b

print(lesser(1,7))
