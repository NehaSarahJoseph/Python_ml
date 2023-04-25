num = int(input("Enter a number: "))
if num%2==0:
    if num in range(2,6):
        print("Not weird")
    elif num in range(6,21):
        print("Weird")
    else:
        print("Not weird")
else:
    print("Weird")


