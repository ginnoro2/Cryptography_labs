from itertools import permutations

# Encrypted message
ciphertext = "YXZZXZ"

alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
unique_cipher_chars = list(set(ciphertext))
num_unique = len(unique_cipher_chars)

print(f"Unique cipher characters: {unique_cipher_chars}")
print(f"Trying all {len(alphabet)}P{num_unique} = {len(alphabet)}! / {(len(alphabet)-num_unique)}! permutations...\n")

for perm in permutations(alphabet, num_unique):
    mapping = dict(zip(unique_cipher_chars, perm))
    
    # Decrypting
    attempt = ""
    for ch in ciphertext:
        attempt += mapping.get(ch, '?') 
    
    print(f"Mapping {mapping}: '{attempt}'")