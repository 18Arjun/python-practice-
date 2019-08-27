ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter


def animal(a,b):
    if a[0].lower() == b[0].lower():
        return True
    else:
        return False

a=str(input("Enter string"))
b=str(input("Enter second string"))
print(animal(a,b))




or



def animal(text):
    word = text.lower().split()
    return word[0][0] == word[1][0]

print(animal("Ajay shish"))
