import random
import gmpy2

e = 0x10001

with open('flag.txt', 'rb') as f:
    m = f.read()
    m = int.from_bytes(m, 'big')

base = random.randint(2, 9)
no_of_bits = random.randint(256, 512)

while True:
    p = random.getrandbits(no_of_bits)
    q = int(gmpy2.digits(p, base))

    # Ensure that they are prime
    if not gmpy2.is_prime(p): continue
    if not gmpy2.is_prime(q): continue

    # Ensure that d exists
    if (p-1) % e == 0: continue
    if (q-1) % e == 0: continue

    break

n = p * q
assert 0 <= m < n

c = pow(m, e, n)

# Writing to out.txt
with open('out.txt', 'w') as f_out:
    f_out.write(f'{n = }\n')
    f_out.write(f'{e = }\n')
    f_out.write(f'{c = }\n')

