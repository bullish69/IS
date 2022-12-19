def ascii_to_binary(a):
    # this will print a in binary
    bnr = bin(a).replace('0b', '')
    x = bnr[::-1]  # this reverses an array
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    # print(bnr)
    return bnr


def binary_to_ascii(a):
    a_rev = a[::-1]
    val = 0
    for i in range(len(a_rev)):
        if a_rev[i] == '1':
            val += 2**i
    return val


def left_shift(string, key):
    # slicing the string into 2 parts at key value and then append it in new empty string
    l = string[:key]
    string = string[key:]
    string += l
    return string


def encryption(pt, key, t):
    # converting pt into blocks of 16 char
    pt_block = []
    while pt != "":
        temp = pt[:16]
        pt_block.append(temp)
        pt = pt[16:]

    print(pt_block)

    # converting each block 1st into ascii value and that ascii value into binary 8 bits number
    binary_pt = []
    for i in range(len(pt_block)):
        b = ''
        for j in range(len(pt_block[i])):
            asc = ord(pt_block[i][j])
            binaryasc = ascii_to_binary(asc)
            b += binaryasc
        binary_pt.append(b)

    # print(binary_pt)

    # for appending 0s if len of binary string is not 128
    if len(binary_pt[-1]) < 128:
        size = 128 - len(binary_pt[-1])
        for i in range(size):
            binary_pt[-1] += '0'

    print('binary pt', binary_pt)

    ls_list = []
    for i in binary_pt:
        a = left_shift(i, t)
        ls_list.append(a)

    print('left shift list', ls_list)

    ls_list = ''.join(ls_list)
    print('left shift list', ls_list)

    ct = ''

    while ls_list != '':
        temp = ls_list[:8]
        br = binary_to_ascii(temp)
        xor = br ^ key
        ch = chr(xor)
        ct += ch
        ls_list = ls_list[8:]

    print(ct)
    return ct


pt = input("Enter Plain Text: ")
pt = pt.upper()
ct = encryption(pt, 65, 2)
print("The cipher text is:", ct)
