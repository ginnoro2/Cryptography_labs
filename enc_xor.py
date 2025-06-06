message = "BADDAD"
cipher = ""
KEY = 0x1F  # XOR key (can be any number between 1–255)

for ch in message:
    encrypted_char = chr(ord(ch) ^ KEY)
    cipher += encrypted_char

print("Original message:", message)
print("Encrypted message:", cipher)