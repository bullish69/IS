def generate_key(string, key):
    new_key = ""
    while len(new_key) < len(string):
        new_key += key

    len_diff = len(new_key) - len(string)
    if len_diff == 0:
        return new_key

    return new_key[:-len_diff]


key = generate_key('DJSANGHVICOLLEGE', 'DJSCE')
# print(key)


def vignere_cipher(pt, k):
    key = generate_key(pt, k)
    ct = ""
    for i in range(len(pt)):
        ch_int = ord(pt[i])-65
        key_int = ord(key[i])-65

        temp = (ch_int + key_int) % 26
        ct += chr(temp+65)

    return ct


def vignere_decipher(ct, k):
    key = generate_key(ct, k)
    pt = ""
    for i in range(len(ct)):
        ch_int = ord(ct[i])-65
        key_int = ord(key[i])-65

        temp = (ch_int - key_int + 26) % 26
        pt += chr(temp+65)

    return pt


def my_cipher(pt, key):
    key_len = len(key)
    ct = pt
    for _ in range(key_len):
        ct = vignere_cipher(ct, key)

    return ct


def my_decipher(ct, key):
    key_len = len(key)
    pt = ct
    for _ in range(key_len):
        pt = vignere_decipher(pt, key)

    return pt


my_cipher('TOPSECRETMESSAGE', 'PASSKEY')

my_decipher('UOLOWEDFTIAKUMHE', 'PASSKEY')
