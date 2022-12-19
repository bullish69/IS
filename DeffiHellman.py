p = int(input("Enter value of p:"))
g = int(input("Enter value of g:"))
a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))


Xa = g**a % p
Xb = g**b % p
print("Xa =", Xa)
print("Xb =", Xb)


Ak = Xb**a % p
Bk = Xa**b % p
print("Ak =", Ak)
print("Bk =", Bk)

if Ak == Bk:
    print("Since the secret key of A and B are equal. Hence connection is successful and they can agree for future communication.")
else:
    print("A and B cannot communicate.")
