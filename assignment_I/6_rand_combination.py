import random
a= int(input("enter a number:"))
b= int(input("enter second number:"))

n1=( random.randint(a,b))
n2=( random.randint(a,b))

print(n1)
print(n2)

if a<b:
    a,b=b,a

fact= i = 1
while i<=n1:
    fact = i*fact
    i = i+1
numerator = fact
sub = n1-n2
fact = i = 1

while i<=sub:
    fact = i*fact
    i += 1

denominator = fact
fact = i = 1
while i<=n2:
    fact = i*fact
    i +=1

denominator = fact*denominator
comb = numerator/denominator
print("combination=",comb)