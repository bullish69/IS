p = int(input("Enter the value of p:"))
q = int(input("Enter the value of q:"))
e = int(input("Enter the value of e:"))

n = p*q
phi_n = (p-1)*(q-1)

print(f"The public key is ({e},{n})")

for i in range(phi_n):
    if (e*i) % phi_n == 1:
        d = i

print(f"The private key is ({d},{n})")

# Encryption
pt = int(input("Enter the plain text:"))
ct = pt**e % n

print("The plain text is:", pt)
print("After Encryption\nThe cipher text is:", ct)

pt = ct**d % n

print("After Decryption\nThe plain text is:", pt)
