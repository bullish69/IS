s = input("Enter plain text : ")
n = len(s)
k = int(input("Enter the shift (key) : "))

# Replacing space with "_"
s = list(s)
for i in range(n):
    if s[i] == " ":
        s[i] = "_"
s = "".join(s)

# Adding "_" tomake divisible by 16
if n % 16:
    for i in range(16-n % 16):
        s += "_"
        n += 1

# Dividing into groups of 16
groups = []
for i in range(n//16):
    groups.append(s[:16])
    s = s[16:]

# Converting char in each group to binary
ans = []
for group in groups:
    temp = ""
    for char in group:
        temp += str(bin(ord(char))).replace("b", "")
    ans.append(temp)

# Circular shift by len(key) bits
for i in range(len(ans)):
    rev = ans[i][::-1]
    a = rev[:k]
    b = rev[k:]
    ans[i] = a[::-1]+b[::-1]

print("Encrypted binary string is :", "".join(ans))
