import random
import math

# Generate random prime numbers
def generate_primes():
    primes = []
    while len(primes) < 2:
        n = random.randint(100, 1000)
        if is_prime(n):
            primes.append(n)
    return primes

# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# Calculate the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Calculate the modular inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Encrypt a message
def encrypt(message, public_key):
    e, n = public_key
    cipher = [(ord(char) ** e) % n for char in message]
    return cipher

# Decrypt a message
def decrypt(cipher, private_key):
    d, n = private_key
    message = ''.join([chr((char ** d) % n) for char in cipher])
    return message

# Generate the public and private keys
def generate_keys():
    p, q = generate_primes()
    n = p * q
    phi_n = (p-1) * (q-1)
    e = random.randint(1, phi_n)
    while gcd(e, phi_n) != 1:
        e = random.randint(1, phi_n)
    d = mod_inverse(e, phi_n)
    return ((e, n), (d, n))

message = input("Enter message\n")
public_key, private_key = generate_keys()
cipher = encrypt(message, public_key)
decrypted_message = decrypt(cipher, private_key)
print("Original message: ", message)
print("Encrypted message: ", cipher)
print("Decrypted message: ", decrypted_message)