def charToBin(s):
    ans = ""
    for i in s:
        ans += str(bin(ord(i))).replace("b", "")
    return ans


def expand(s):
    ans = []
    bits = []
    for i in range(8):
        ans.append(s[:4])
        bits.append([s[0], s[3]])
        s = s[4:]
    for i in range(1, 7):
        ans[i] = bits[i-1][1]+ans[i]+bits[i+1][0]
    ans[0] = bits[-1][1]+ans[0]+bits[1][0]
    ans[-1] = bits[-2][1]+ans[-1]+bits[0][0]
    return "".join(ans)


def xor(s, k, n):
    ans = ""
    for i in range(n):
        ans += str(int(s[i]) ^ int(k[i]))
    return ans


def compress(s, box):
    ans = ""
    for i in range(8):
        row = int(s[0]+s[5], 2)
        col = int(s[1:5], 2)
        val = str(bin(box[row][col])).replace("0b", "")
        while len(val) < 4:
            val = "0"+val
        ans += val
        s = s[6:]
    return ans


def encrypt(s, k, box):
    sbin = charToBin(s)
    lpt = sbin[:32]
    rpt = sbin[32:]

    kbin = charToBin(k)
    k1 = kbin[:48]
    k2 = kbin[48:]

    # Round 1
    rpt = expand(rpt)
    rpt = xor(rpt, k1, 48)
    rpt = compress(rpt, box[0])
    rpt = xor(rpt, lpt, 32)

    # Round 2
    lpt, rpt = rpt, lpt
    rpt = expand(rpt)
    rpt = xor(rpt, k2, 48)
    rpt = compress(rpt, box[1])
    rpt = xor(rpt, lpt, 32)

    lpt, rpt = rpt, lpt
    return lpt + rpt


s = input("Enter plain text of 8 characters : ")  # 64 bit input
# 96 bit key (Divide into 2 : each of 48 bit)
k = input("Enter key of 12 characters : ")

box = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

       [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]]

print("The encrypted text is :", encrypt(s, k, box))
