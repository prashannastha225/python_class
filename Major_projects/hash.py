import hashlib

password = "my_secret_password"

encoded_password = password.encode()

# 3. Create the hash (SHA-256 is the industry standard)
hashed_password = hashlib.sha256(encoded_password).hexdigest()

print(f"Original: {password}")
print(f"Hashed: {hashed_password}")