import hashlib

password = "list"
result = hashlib.sha256(password.encode('utf-8'))

print(result.hexdigest())