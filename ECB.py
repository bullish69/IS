plain_text = input("Enter Plain Text :")
key = input("Enter Key: ")

def split_into_16(plain_text):
    chunks = []
    for i in range(0, len(plain_text), len(key)):
        chunks.append(plain_text[i:i+len(key)])

    while len(chunks[-1])<16:
        chunks[-1]+=' ' # append space ' ' to make the last string of 16 characters

    return chunks

split_into_16(plain_text)

def string_to_bin(string):
    bin_str = ''
    for char in string:
        bin_str += format(ord(char), '08b')
    return bin_str

def text_to_binary_list(plain_text):
    # str_16 is a list containing strings of 16 characters each 
    str_16 = split_into_16(plain_text)

    # str_128 = list containing string representing 16*8 = 128 bits binary format of corresponding str_16 
    str_128 = []
    for s in str_16:
        str_128.append(string_to_bin(s))

    return str_128
    
text_to_binary_list(plain_text)

def xor(X, Y):
    val = ''
    for x, y in zip(X, Y):
        if x == y:
            val+='0'
        else:
            val+='1'
    return val

format(ord('a'), '08b')
chr(int('01100001', 2))

def encrypt_128(plain_text, key):
    key_128 = string_to_bin(key)
    bin_list = text_to_binary_list(plain_text)
    xor_list = []
    cipher_txt = ''
    for ele in bin_list:
        ''' take xor of element and key '''
        xor_list.append(xor(ele, key_128))


    ''' Now iterate ovr this XOR list '''
    for str_128 in xor_list:
        # print(str_128[:8])
        ''' get nth 8 bits out of 128 bits '''
        for i in range(0, 128, 8):
            temp_8 = str_128[i:i+8]
            ''' circular left shift on 8 bits'''
            str_8 = temp_8[1:] + temp_8[0]

            '''convert to char'''
            cipher_txt += chr(int(str_8, 2))
            # print(chr(int(str_8, 2)))
            
    return cipher_txt
ct = encrypt_128(plain_text, key)
print(ct)