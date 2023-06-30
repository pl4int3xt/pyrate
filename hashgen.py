import hashlib

password = "defcon"
result = hashlib.sha256(password.encode('utf-8'))

print(result.hexdigest())