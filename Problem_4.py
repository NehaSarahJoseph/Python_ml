def swapi(x):
    k = " "
    for i in x:
        if i.islower():
             k += i.upper()
        else:
             k += i.lower()
    return k
name = input("Enter a name: ")
ret = swapi(name)
print(ret)

#here k is a local variable while name is a global variable






