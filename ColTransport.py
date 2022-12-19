# Encryption

s = input("Enter plain text : ")
k = input("Enter the key : ")


def encrypt(s, k):
    sortedk = sorted(k)
    lk = len(k)
    ls = len(s)
    k = list(k)
    idx = []
    for i in range(lk):
        idx.append(k.index(sortedk[i]))
        k[k.index(sortedk[i])] = "#"

    table = []
    i = 0
    while i < ls:
        temp = []
        for j in range(lk):
            if i < ls:
                temp.append(s[i])
            else:
                temp.append("0")
            i += 1
        table.append(temp)

    ans = ""
    for i in range(lk):
        col = idx[i]
        for row in range(len(table)):
            ans += table[row][col]
    return ans


print("The encyrpted text is :", encrypt(s, k))
print("The double encyrpted text is :", encrypt(encrypt(s, k), k))


# Decryption

s = input("Enter cipher text : ")
k = input("Enter the key : ")


def decrypt(s, k):
    ls = len(s)
    lk = len(k)
    sortedk = sorted(k)
    k = list(k)
    idx = []
    for i in range(lk):
        idx.append(k.index(sortedk[i]))
        k[k.index(sortedk[i])] = "#"

    cols = lk
    rows = ls//lk
    table = []
    for i in range(rows):
        table.append(["0"]*cols)
    x = 0
    for i in range(cols):
        curridx = idx[i]
        for j in range(rows):
            table[j][curridx] = s[x]
            x += 1
    ans = ""
    for i in table:
        ans += "".join(filter(lambda x: x != "0", i))
    return ans


print("The decyrpted text is :", decrypt(s, k))
print("The double decyrpted text is :", decrypt(decrypt(s, k), k))
