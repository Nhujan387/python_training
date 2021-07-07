n=15
r=3
fact= i = 1
while i<=n:
    fact = i*fact
    i = i+1
numerator = fact
sub = n-r
fact = i = 1

while i<=sub:
    fact = i*fact
    i += 1

denominator = fact
fact = i = 1
while i<=r:
    fact = i*fact
    i +=1

denominator = fact*denominator
comb = numerator/denominator
print("combination=",comb)
