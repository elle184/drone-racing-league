import jwt

def decode(token) :
    return jwt.decode(jwt=token, key="secret_phrase", algorithms=["HS256"])