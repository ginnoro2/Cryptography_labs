from itertools import permutations

# Encrypted message we want to crack
ciphertext = "YXZZXZ"

original_chars = ['A', 'B', 'D']
encrypted_chars = ['X', 'Y', 'Z']

#Mapping
for perm in permutations(encrypted_chars):
    mapping = dict(zip(perm, original_chars))
    
    # Decryption
    attempt = ""
    for ch in ciphertext:
        attempt += mapping.get(ch, ch)
    
    print(f"Trying mapping {mapping}: '{attempt}'")