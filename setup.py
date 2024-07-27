from setuptools import setup, find_packages

setup(
    name='my_telegram_bot',  # Nome do pacote
    version='0.1',  # Versão do pacote
    packages=find_packages(),  # Inclui todos os pacotes no diretório
    install_requires=[
        'requests',  # Dependência necessária para a biblioteca
    ],
    author='Vinicius Gomes Batista',  # Seu nome
    author_email='viniciusgo18@gmail.com',  # Seu email
    description='Uma biblioteca simples para interagir com o Telegram Bot API',  # Descrição curta
    long_description=open('README.md').read(),  # Descrição longa retirada do README.md
    long_description_content_type='text/markdown',  # Tipo de conteúdo do README
    url='https://github.com/iniciusgomesbatista/my_telegram_bot',  # URL do repositório
    classifiers=[
        'Programming Language :: Python :: 3',  # Classificador de linguagem de programação
        'License :: OSI Approved :: MIT License',  # Licença do pacote
        'Operating System :: OS Independent',  # Sistema operacional
    ],
)
