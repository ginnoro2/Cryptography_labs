message = "BAD"

cipher = message.replace("B", "X")
cipher = cipher.replace("A","M")
cipher = cipher.replace("D", "T")

print("Original message:", message)
print("Encrypted message:", cipher)