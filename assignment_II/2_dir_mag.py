from math import *
A= (20,30)
B= (30,40)

dir= degrees(atan((B[1]-A[1])/(B[0]-A[0])))

mag= sqrt(((B[0]-A[0])**2)+((B[1]-A[1])**2))

print(dir)
print(mag)



