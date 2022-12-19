from math import gcd


def lowestprime(n):
    for i in range(n, 1, -1):
        flag = 1
        for j in range(2, i//2+1):
            if i % j == 0:
                flag = 0
                break
        if flag:
            return i
    return 2


x = input("Enter string 1 : ")
y = input("Enter string 2 : ")
p, q = lowestprime(len(x)), lowestprime(len(y))
if p == q:
    i = q+2
    while True:
        flag = 1
        for j in range(2, i//2+1):
            if i % j == 0:
                flag = 0
                break
        if flag:
            q = i
            break
        i += 1
print(f"Value of p is {p}")
print(f"Value of q is {q}")
n = p*q
phi = (p-1)*(q-1)
i = 2
while True:
    if gcd(i, phi) == 1 and i != p and i != q:
        e = i
        break
    i += 1
i = 1
while True:
    if (i*e) % phi == 1 and i != e:
        d = i
        break
    i += 1
print(f"Value of e is {e}")
print(f"Value of d is {d}")
pt = int(input("Enter numerical plain text : "))
if pt > phi:
    pt = pt % phi
    print(f"Since PT>phi so taking mod...")
print(f"Final plain text is {pt}")
ct = (pt**e) % n
print(f"Cipher text is {ct}")
decrypt = (ct**d) % n
print(f"Decrypted text is {decrypt}")
