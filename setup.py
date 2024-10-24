from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chalice_auth_middleware",
    version="0.1.0",
    author="Fabio AM",
    author_email="fabio@am.com",
    description="Um módulo de middleware Chalice para controle de acesso baseado em roles.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seuprojeto/chalice_auth_middleware",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "chalice",
        "PyJWT",
    ],
    test_suite="tests",
)
