# pip install hashlib

import hashlib

def hash_password(password):
    hash_obj = hashlib.sha256()
    hash_obj.update(password.encode('utf-8'))
    return hash_obj.hexdigest()

password = 'SMK_TamharDevID'
hash_password = hash_password(password)
print(hash_password)