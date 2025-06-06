from itertools import permutations

# Encrypted message
ciphertext = "YXZZXZ"

# All uppercase letters (possible character pool)
alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# Get unique characters in ciphertext
unique_cipher_chars = list(set(ciphertext))

# Number of unique cipher characters
num_unique = len(unique_cipher_chars)

print(f"Unique cipher characters: {unique_cipher_chars}")
print(f"Trying all {len(alphabet)}P{num_unique} = {len(alphabet)}! / {(len(alphabet)-num_unique)}! permutations...\n")

# Try all possible injective mappings from cipher chars to plaintext chars
for perm in permutations(alphabet, num_unique):
    # Create mapping: cipher_char -> plain_char
    mapping = dict(zip(unique_cipher_chars, perm))
    
    # Decrypt using this mapping
    attempt = ""
    for ch in ciphertext:
        attempt += mapping.get(ch, '?')  # '?' for unmapped characters (shouldn't happen here)
    
    print(f"Mapping {mapping}: '{attempt}'")