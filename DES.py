def blocksof4(text):
    blocks = []
    while(text!=''):
        blocks.append(text[:4])
        text = text[4:]
    
    return blocks

def expansionPermutation(RPT, KEY):
    blocksRPT = blocksof4(RPT)
    n = len(blocksRPT)
    
    expandedRPT = []
    for inx, word in enumerate(blocksRPT):
        if inx==0:
            temp = blocksRPT[-1][-1] + word + blocksRPT[1][0]
        elif inx==(n-1):
            temp = blocksRPT[-2][-1] + word + blocksRPT[0][0]
        else:
            temp = blocksRPT[inx-1][-1] + word + blocksRPT[inx+1][0]
        
        expandedRPT.append(temp)

    expandedRPT_str = ''.join(expandedRPT)
    
    XORed = ''
    for pt, k in zip(expandedRPT_str, KEY):
        XORed += str(int(pt)^int(k))
    
    blocksof6 = []
    while XORed!='':
        blocksof6.append(XORed[:6])
        XORed = XORed[6:]

    sbox = []
    for i in blocksof6:
        temp = i[1:5]
        sbox.append(temp)
 
    sbox_str = ''.join(sbox)

    return sbox_str

def encryption(PT, KEY1, KEY2):
    n = len(PT)
    n = n//2
    lpt = pt[:n]
    rpt = pt[n:]
    
    for i in range(2):
        print('\nLPT :', lpt)
        print('RPT :', rpt)
        if(i==0):
            sbox = expansionPermutation(rpt, KEY1)
        else:
            sbox = expansionPermutation(rpt, KEY2)

        xor = ''
        for l, k in zip(lpt, sbox):
            xor += str(int(l)^int(k))
        
        lpt = xor
        lpt, rpt = rpt, lpt

    
    return lpt + rpt

pt = '0100110010100001101101111110111000000110010111110100010001010010'
# pt = pt.upper()
print(pt)

key1 = '001111111010110111000011111100010110110011110100'
key2 = '110000000101001000111100000011101001001100001011'
# key = key.upper()
print(key1)
print(key2)

f"Plain Text: {pt}"

ct = encryption(pt, key1, key2)
f"Ciphered TExt: {ct}"