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
        if n_pt % n_key != 0:
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


pt = input("Enter Plain Text : ")
key = input("Enter a Key :")

print('The plain text is:', pt)
print('the keyword is:', key)

keyvalue = getKeyValues(key)
print('The value of characters in key is:')
print(keyvalue)

print('\n\n')
mat = add_X(pt, key)
print("The matrix after 1st is:")
print(list(key))
for row in mat:
    print(row)

ct = encryption(mat, key, keyvalue)
print('After 1st Encryption\nThe text is:', ct, '\n')

mat1 = add_X(ct, key)
print("The matrix after 2nd is:")
print(list(key))
for row1 in mat1:
    print(row1)
ct1 = encryption(mat1, key, keyvalue)
print('After 2nd Encryption\nThe cipher text is:', ct1, '\n')

pt1 = decryption(ct1, key, keyvalue)
print('After Decryption\nThe text is:', pt1, '\n')

pt = decryption(pt1, key, keyvalue)
print('After 2nd decryption\nThe plain text is:', pt)
