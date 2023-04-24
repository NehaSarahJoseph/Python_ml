# a = coefficient of x^2
# b = coefficient of x^1
# c = coefficient of x^0
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
k = (b**2) - (4*a*c)
#neglecting 0 and negative case
d = k**0.5
x1 = (-b + d)/(2*a)
x2 = (-b - d)/(2*a)
print("Roots are ", x1,x2)