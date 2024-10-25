# Chalice Auth Middleware

Este middleware é usado para proteger rotas em aplicações Chalice com base em permissões definidas no JWT. Ele permite a verificação de tokens JWT, a validação do papel (`role`) do usuário e a correspondência do aplicativo (`app_name`) ao projeto (`project_slug`) contido no token.

## Funcionalidades

- Verifica se o token JWT está presente nos headers da requisição.
- Decodifica o token JWT usando a chave secreta definida nas variáveis de ambiente (`JWT_SECRET_KEY`).
- Valida se o `role` do usuário possui permissões suficientes para acessar a rota.
- Permite acessar rotas específicas com base no papel do usuário: `user`, `admin` ou `root`.
- Garante que o `app_name` da aplicação corresponda ao `project_slug` no token JWT.

## Dependências

Este middleware não funciona de forma isolada. Ele depende outra app para gerar tokens JWT que contenham as informações de login, como o papel do usuário (`role`), organização (`organization`) e projeto (`project_slug`).

## Instalação

Para instalar este middleware em seu projeto Chalice, siga os passos abaixo:

### 1. Adicionar o middleware ao `requirements.txt`

No arquivo `requirements.txt` do seu projeto, adicione o seguinte:

```plaintext
chalice_auth_middleware @ git+https://github.com/20DASH/chalice_auth_middleware@main
```

Isso garantirá que o middleware seja instalado junto com as dependências do projeto.

### 2. Configurar o middleware nas rotas

Após instalar o middleware, você pode usá-lo para proteger suas rotas. Para isso, adicione o decorator `@require_role` logo abaixo do decorator `@app.route()`, conforme o exemplo:

```python
from chalice import Chalice, Response
from chalice_auth_middleware import require_role, get_current_user

app = Chalice(app_name='my-app')

@app.route('/hello', methods=['POST'])
@require_role('admin')
def hello():
    current_user = get_current_user()

    return {'message': 'Hello, %s!' % current_user.get('sub')}
```

Neste exemplo, a rota `/create` exige que o usuário tenha o papel `admin`. Apenas usuários com o papel `admin` ou `root` terão acesso a esta rota. Se o papel do usuário for `user`, ele não poderá acessar a rota, exceto se houver permissões especiais.


## Estrutura do Token JWT

O token JWT deve conter as seguintes informações no payload para que o middleware funcione corretamente:

- **role**: Define o papel do usuário (e.g., `user`, `admin`, `root`).
- **project_slug**: Deve corresponder ao `app_name` da aplicação Chalice.

## Tratamento de Erros

O middleware trata automaticamente os seguintes erros:

- **Token Expirado**: Retorna `UnauthorizedError("Token expired")`.
- **Token Inválido**: Retorna `UnauthorizedError("Invalid token")`.
- **Acesso Negado**: Se o papel do usuário não tiver as permissões adequadas, retorna `UnauthorizedError(f'Access denied. Admins only. You are logged in as {user_role}')`.
