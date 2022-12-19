import math

# check if p and q are prime if not convert it into just closer prime number


def make_prime(number, *exclude):
    while True:
        for i in range(2, number):
            if number in exclude:
                number += 1
            if number % i == 0:
                number += 1
                break
        if i == number-1:
            break
    return number

# to get e which is relavtively prime to phi_n and less than phi_n


def get_e(p, q, phi_n):
    for i in range(2, phi_n):
        if math.gcd(i, phi_n) == 1 and i != p and i != q:
            return i

# extended euclidean method to calculate d value


def eem(phi_n, e):
    r = [phi_n, e]
    qt = ['-', '-']
    x = [1, 0]
    y = [0, 1]

    while r[-1] != 1:
        qt.append(r[-2] // r[-1])
        r.append(r[-2] % r[-1])
        x.append(x[-2] - qt[-1]*x[-1])
        y.append(y[-2] - qt[-1]*y[-1])

    print('r\tqt\tx\ty')
    for i in range(len(r)):
        print(f'{r[i]}\t{qt[i]}\t{x[i]}\t{y[i]}')

    return y[-1] % phi_n


# p and q are string input and pt is integer
p = len(input("Enter p(str): "))
q = len(input("Enter q(str): "))

p = make_prime(p)
q = make_prime(q, p)
# p = 7
# q = 11
# e = 13
print('The p value is:', p)
print('The q value is:', q, '\n')

n = p*q
phi_n = (p-1)*(q-1)
e = get_e(p, q, phi_n)
d = eem(phi_n, e)

print()
print('Public key:', (e, n))
print('Private key:', (d, n))
print()

pt = int(input("Enter plain text(int): "))

ct = pt**e % n
print("After encryption\nThe cipher text is:", ct, '\n')

pt = ct**d % n
print('After decryption\nThe plain text is:', pt)
