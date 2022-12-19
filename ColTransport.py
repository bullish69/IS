import numpy as np

def getKeyValues(key):
    keylist = list(key)
    sortkeylist = sorted(key)
    visited = []

    for i, char in enumerate(sortkeylist):
        visited.append([char, i+1])

    sahi_keyvalue = []

    for i in key:
        for char in visited:
            if char[0] == i:
                sahi_keyvalue.append(char)
                visited.pop(visited.index(char))
                break

    return sahi_keyvalue


def add_X(pt, key):
    n_pt = len(pt)
    n_key = len(key)

    if n_pt == n_key:
        n_pt = len(pt)

    else:
        k = n_key - n_pt % n_key
        for i in range(k):
            pt += 'X'
        n_pt = len(pt)

    mat = []

    while pt != "":
        temp = list(pt[:n_key])
        mat.append(temp)
        pt = pt[n_key:]

    return mat

# Encryption


def encryption(mat, key, keyValuelist):
    sortedKey = sorted(keyValuelist, key=lambda x: x[1])

    ct = []
    for i in sortedKey:
        ind = keyValuelist.index(i)
        temp = []
        for row in mat:
            temp.append(row[ind])
        ct.append(temp)

    ct1 = ''
    for row in ct:
        temp = ''
        ct1 += temp.join(row)

    return ct1


def decryption(ct, key, keyValuelist):
    n_key = len(key)
    n_ct = len(ct)

    n_rows = n_ct//n_key

    ct = list(ct)
    ct_list = []
    while ct != []:
        ct_list.append(ct[:n_rows])
        ct = ct[n_rows:]

    sortedkeyvalue = sorted(keyValuelist, key=lambda x: x[1])

    mat = [[] for _ in range(n_key)]

    for i, text in enumerate(ct_list):
        for row in keyValuelist:
            if row[1] - 1 == i:
                ind = keyValuelist.index(row)
                mat[ind] = text
                break

    # print(mat)

    newmat_arr = np.array(list(mat))
    # print(newmat_arr)
    transpose = newmat_arr.T
    transpose_list = transpose.tolist()

    pt = ''
    for row in transpose_list:
        print(row)
        pt += ''.join(row)

    return pt


pt = input("Enter Plain Text :")
key = input("Enter a Key :")

print('The plain text is:', pt)
print('the keyword is:', key)

keyvalue = getKeyValues(key)
print('The value of characters in key is:')
print(keyvalue)

print('\n\n')
mat = add_X(pt, key)
print("The matrix is:")
print(key)
for row in mat:
    print(row)

ct = encryption(mat, key, keyvalue)
print('After Encryption\nThe cipher text is:', ct, '\n')

pt = decryption(ct, key, keyvalue)
print('After Decryption\nThe plain text is:', pt)
