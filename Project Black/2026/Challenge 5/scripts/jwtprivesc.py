import jwt
import time

secret = "ThisIsTheVeryVerySecretKey"  # Decoded from Base64

payload = {
    'iss': 'http://projectblack.io',
    'aud': 'http://projectblack.io',
    'iat': int(time.time()),
    'nbf': 1357000000,
    'exp': int(time.time()) + 31536000,
    'role': 'admin',
    'username': 'eddie',
    'userId': 42
}

token = jwt.encode(payload, secret, algorithm='HS256')
print(token)
