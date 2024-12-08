import random

from Crypto.Util.Padding import pad
from cryptography.hazmat.primitives.asymmetric import rsa

# Your Solution should NOT depend on the value of key
# it is kept as 100 for help in testing
key = 1000

with open("flag.txt", "r") as file:
    flag = file.read().strip()

private_key = rsa.generate_private_key(
    public_exponent=3,
    key_size=2048,
)

public_key = private_key.public_key()

public_numbers = public_key.public_numbers()
modulus = public_numbers.n
e = public_numbers.e


# Encrypting the flag after padding
flag = pad(flag.encode(), 256)
flag_int = int.from_bytes(flag, byteorder="big")
ciphertext_int = pow(flag_int, e, modulus)

ciphertext1 = ciphertext_int.to_bytes(
    (ciphertext_int.bit_length() + 7) // 8, byteorder="big"
)

print(f"Modulus (n): {modulus}")


# Generate a random polynomial of a random degree
def generate_polynomial():
    degree = random.randint(1, 10)
    coefficients = [random.randint(0, key) for _ in range(degree + 1)]
    return coefficients


def evaluate_polynomial(coefficients, x):
    result = 0
    for coefficient in reversed(coefficients):
        result = result * x + coefficient
    return result


coefficients = generate_polynomial()
print("Welcome to the Challenge! No way you can break this encryption!")
print("Input x: ", end="")
x = int(input())
print("Here is f(x):", evaluate_polynomial(coefficients, x) % modulus)
print("Input y: ", end="")
y = int(input())
print("Here is f(y):", evaluate_polynomial(coefficients, y) % modulus)


int_2 = evaluate_polynomial(coefficients, flag_int) % modulus
# Now we encrypt int_2 as well
ciphertext_int_2 = pow(int_2, e, modulus)


# Printing the ciphertexts
print(f"Ciphertext1 (hex): {ciphertext1.hex()}")
print(
    f"Ciphertext2 (hex): {ciphertext_int_2.to_bytes((ciphertext_int_2.bit_length() + 7) // 8, byteorder='big').hex()}"
)
