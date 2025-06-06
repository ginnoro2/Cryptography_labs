from itertools import permutations

# Encrypted message we want to crack
ciphertext = "YXZZXZ"

# Known substitutions used in encryption
original_chars = ['A', 'B', 'D']
encrypted_chars = ['X', 'Y', 'Z']

# Try all possible mappings
for perm in permutations(encrypted_chars):
    mapping = dict(zip(perm, original_chars))
    
    # Decrypt using this mapping
    attempt = ""
    for ch in ciphertext:
        attempt += mapping.get(ch, ch)  # Use .get() to avoid KeyError
    
    print(f"Trying mapping {mapping}: '{attempt}'")