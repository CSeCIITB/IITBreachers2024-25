#!/usr/bin/env python3
from secret import flag, params
from Crypto.Util.number import *
from random import *

def sol(m, z):
	p = 2
	while True:
		R = list(range(1, 150))
		shuffle(R)
		for r in R[:z]:
			p += getRandomRange(0, 2) * m ** r
		if isPrime(p):
			return p
		else:
			p = 2


p, q, r = [sol(*params) for _ in '007']
n = p * q * r
m = bytes_to_long(flag)
c = pow(m, params[0] ** 3 + params[1] - 2, n)
print(f'n = {n}')
print(f'c = {c}')

# flag FORMAT (without the quotations): "FLAG{some_text}"
