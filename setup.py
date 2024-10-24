from setuptools import setup, find_packages

# Lê o conteúdo do README.md para usar como descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chalice_auth_middleware",  # Nome do pacote
    version="0.1.0",  # Versão inicial
    author="Fabio AM",  # Seu nome ou nome da organização
    author_email="fabio@am.com",  # Seu email
    description="Um módulo de middleware Chalice para controle de acesso baseado em roles.",  # Descrição curta
    long_description=long_description,  # Descrição longa lida do README.md
    long_description_content_type="text/markdown",  # Tipo do conteúdo do README
    url="https://github.com/seuprojeto/chalice_auth_middleware",  # URL do projeto
    packages=find_packages(),  # Localiza automaticamente os pacotes no diretório
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Requer Python 3.6 ou superior
    install_requires=[
        # Dependências necessárias, caso seu middleware precise de bibliotecas específicas
        "chalice",
        "PyJWT",  # Exemplo de dependência para decodificar JWT
    ],
    test_suite="tests",  # Configuração dos testes
)
