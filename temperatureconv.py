n = (input("Enter your temperature (for e.g. 150C or 150F or 150K):"))

d = n[-1]

print(d)
print(type(d))
e = "C"
f = "F"
g = "K"

u = n[0:-1]
print(type(u))
u = int(u)
print(u)
print(type(u))

g = (input("Enter the scale to which you want to convert (either Celsius or Fahrenheit or Kelvin): "))
g = g[0]
print(g)


