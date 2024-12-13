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


def get_current_user():
    from app import app
    request = app.current_request
    token = request.headers.get('Authorization')
    if not token:
        raise UnauthorizedError('Missing token')
    # Decodificar o token para verificar o role
    token = token.replace('Bearer ', '')  # Remove o prefixo 'Bearer ' se estiver presente
    payload = decode_jwt(token)
    return payload


def require_role(role):
    def wrapper(func):
        def decorated_function(*args, **kwargs):
            payload = get_current_user()
            user_role = payload.get('role')

            from app import app
            # if app.app_name != payload.get('project_slug'):
            #     raise UnauthorizedError(f'App name is not the same from token')

            if user_role == role or user_role == 'root' or (role == 'user' and user_role == 'admin'):
                return func(*args, **kwargs)

            raise UnauthorizedError(f'Access denied: {role} only. You are logged in as {user_role}')

        return decorated_function

    return wrapper
