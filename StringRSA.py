import math


def encrypt(PT, e):
    ascii_values = []
    encrypted = []
    encrypt = []
    for character in PT:
        ascii_values.append(ord(character))
    phi_n = (p-1) * (q-1)
    n = p*q
    for i in range(len(ascii_values)):
        opp = (pow(ascii_values[i], e)) % n
        encrypted.append(opp)
    for character in encrypted:
        encrypt.append(chr(character))
    encrypt = "".join(encrypt)
    print("Encrypted Text", encrypt)
    return encrypt


def decrypt(CT, d):
    ascii_values = []
    decrypted = []
    decrypt = []
    phi_n = (p-1) * (q-1)
    n = p*q
    for character in CT:
        ascii_values.append(ord(character))
    for i in range(len(ascii_values)):
        opp = (pow(ascii_values[i], d)) % n
        decrypted.append(opp)
    for character in decrypted:
        decrypt.append(chr(character))
    decrypt = "".join(decrypt)
    print("DecryptedText:", decrypt)


p = int(input("Enter p:"))
print("Entered p:", p)
print()

q = int(input("Enter q:"))
print("Entered q:", q)
print()

e = int(input("Enter e:"))
print("Entered e:", e)
print()

phi_n = (p-1)*(q-1)
for i in range(phi_n):
    if (e*i) % phi_n == 1:
        print("DecryptionKey:", i)
print()

PT = input("Enter plaintext:")
print("Entered plaintext:", PT)
print()

e = int(input("Enter key for encryption:"))
print("Entered key for encryption:", e)
print()
CT = (encrypt(PT, e))
print()
d = int(input("Enter key for decryption:"))
print("Entered key for decryption:", d)
print()
decrypt(CT, d)
