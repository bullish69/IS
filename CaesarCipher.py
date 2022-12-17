message = input("Enter a Message :")
alpha = 'abcdefghkijklmnopqrstuvwxyz'
key = input("Enter a Key :")
encrypt = ''
decrypt = ''

for i in message:
    post = alpha.find(i)
    newpost = (post+5) % 26
    encrypt += alpha[newpost]
print(encrypt)

for i in encrypt:
    pos = alpha.find(i)
    newpos = (pos-5) % 26
    decrypt += alpha[newpos]
print(decrypt)
