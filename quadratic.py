# ax**2 + bx + c = 0

a = float(input('Enter a:'))
b = float(input('Enter b:'))
c = float(input('Enter c:'))

# calculate discriminant
d = ((b**2) - (4*a*c))
# the 2 solutions
sol1 = (-b + (d**1/2)) / (2*a)
sol2 = (-b - (d**1/2)) / (2*a)

print(sol1)
print(sol2)