import os

import jwt
from chalice import UnauthorizedError

SECRET_KEY = os.getenv('JWT_SECRET_KEY')

def decode_jwt(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise UnauthorizedError("Token expired")
    except jwt.InvalidTokenError:
        raise UnauthorizedError("Invalid token")


def require_role(role):
    def wrapper(func):
        def decorated_function(*args, **kwargs):
            from app import app  # Importa o app aqui para evitar dependências cíclicas
            request = app.current_request
            token = request.headers.get('Authorization')

            if not token:
                raise UnauthorizedError('Missing token')

            # Decodificar o token para verificar o role
            token = token.replace('Bearer ', '')  # Remove o prefixo 'Bearer ' se estiver presente
            payload = decode_jwt(token)
            user_role = payload.get('role')

            if user_role == role or user_role == 'root' or (role == 'user' and user_role == 'admin'):
                return func(*args, **kwargs)

            raise UnauthorizedError(f'Access denied. Admins only. You are logged in as {user_role}')

        return decorated_function

    return wrapper
