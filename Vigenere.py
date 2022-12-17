def Vigenere(text, s, Flag):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if(Flag):
            result += chr((ord(char)-97 + ord(s[i])-97) % 26 + 97)
        else:
            result += chr((ord(char) - ord(s[i]) + 26) % 26 + 97)
    return result


if __name__ == "__main__":
    Key = ''.join(input("Enter Key: ").lower().split())
    Plain = ''.join(input("Enter PlainText: ").lower().split())
    s = ''
    caterpillar = 0
    for i in range(len(Plain)):
        s += Key[caterpillar % len(Key)]
        caterpillar += 1
    CipherText = Vigenere(Plain, s, True)
    print("CipherText: ", CipherText)
    print("PlainBack: ", Vigenere(CipherText, s, False))
