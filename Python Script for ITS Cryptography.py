import random

def xor_bytes(b1, b2):
    return bytes([a ^ b for a, b in zip(b1, b2)])

def generate_key(length):
    return bytes([random.randint(0, 255) for _ in range(length)])

def encrypt(plaintext, key):
    return xor_bytes(plaintext, key)

def decrypt(ciphertext, key):
    return xor_bytes(ciphertext, key)

# Example usage
plaintext = b"Hello, world!"
key = generate_key(len(plaintext))
ciphertext = encrypt(plaintext, key)
decrypted_plaintext = decrypt(ciphertext, key)

print("Plaintext: ", plaintext)
print("Key: ", key)
print("Ciphertext: ", ciphertext)
print("Decrypted plaintext: ", decrypted_plaintext)
