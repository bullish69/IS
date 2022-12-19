def createTable(key):
    k = []
    for i in key:
        if i not in k:
            if i == "J":
                k.append("I")
            else:
                k.append(i)
    for i in range(65, 91):
        if i == 74:
            continue
        if chr(i) not in k:
            k.append(chr(i))
    table = []
    for i in range(5):
        table.append(k[:5])
        k = k[5:]
    return table


def group2(s):
    l = len(s)
    group = []
    i = 0
    while i < l-1:
        if s[i] != s[i+1]:
            group.append(s[i]+s[i+1])
            i += 2
        else:
            if s[i] == "X":
                t = "Y"
            else:
                t = "X"
            group.append(s[i]+t)
            i += 1
    if i == l-1:
        if s[i] == "X":
            t = "Y"
        else:
            t = "X"
        group.append(s[i]+t)
    return group


def search(table, e):
    for i in range(5):
        for j in range(5):
            if table[i][j] == e:
                return i, j

# Encryption


s = input("Enter plain text : ").upper()
k = input("Enter key : ").upper()


def encrypt(s, k):
    group = group2(s)
    table = createTable(k)
    ans = ""
    for g in group:
        c1, c2 = g[0], g[1]
        i1, j1 = search(table, c1)
        i2, j2 = search(table, c2)
        if i1 == i2:
            ans += table[i1][(j1+1) % 5]+table[i2][(j2+1) % 5]
        elif j1 == j2:
            ans += table[(i1+1) % 5][j1]+table[(i2+1) % 5][j2]
        else:
            ans += table[i1][j2]+table[i2][j1]
    return ans


print("Encrypted text is :", encrypt(s, k))

# Decryption

s = input("Enter cipher text : ").upper()
k = input("Enter key : ").upper()


def decrypt(s, k):
    group = group2(s)
    table = createTable(k)
    ans = ""
    for g in group:
        c1, c2 = g[0], g[1]
        i1, j1 = search(table, c1)
        i2, j2 = search(table, c2)
        if i1 == i2:
            ans += table[i1][(j1+4) % 5]+table[i2][(j2+4) % 5]
        elif j1 == j2:
            ans += table[(i1+4) % 5][j1]+table[(i2+4) % 5][j2]
        else:
            ans += table[i1][j2]+table[i2][j1]
    return ans


print("Decrypted text is :", decrypt(s, k))
