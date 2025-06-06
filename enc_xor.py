message = "BADDAD"
cipher = ""
# XOR key (can be any number between 1–255)
KEY = 0x1F  

for ch in message:
    encrypted_char = chr(ord(ch) ^ KEY)
    cipher += encrypted_char

print("Original message:", message)
print("Encrypted message:", cipher)