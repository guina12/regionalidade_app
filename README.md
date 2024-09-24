# Configuração do Ambiente para o Projeto

## Pré-requisitos

Antes de começar, certifique-se de que você possui os seguintes softwares e bibliotecas instalados:

- [Python 3.10 ou superior](https://www.python.org/downloads/): O interpretador de Python necessário para rodar o projeto.
- [MySQL](https://dev.mysql.com/downloads/mysql/): Banco de dados relacional utilizado no projeto.
- [MySQL Connector](https://dev.mysql.com/downloads/connector/python/): Biblioteca para conectar o Python ao MySQL.
- [Flask](https://flask.palletsprojects.com/en/3.0.x/): Framework web leve e poderoso para construção de APIs e aplicações web em Python.
- `pip`: Gerenciador de pacotes Python para instalar bibliotecas e dependências.

## Passos para Configuração

### 1. Instalar o MySQL

Baixe e instale o MySQL a partir do [site oficial](https://dev.mysql.com/downloads/mysql/). Durante a instalação, siga estas etapas:

- Configure uma senha para o usuário `root`.
- Anote a senha, pois será necessária para conectar ao banco de dados.

### 2. Criar o Banco de Dados

Após instalar o MySQL, siga os passos abaixo para criar o banco de dados:

1. Abra o terminal e conecte-se ao MySQL:
   ```bash
   mysql -u root -p
2. Crie um novo banco de dados:
   ```sql
   CREATE DATABASE nome_do_banco;
   USE nome_do_banco;
   pip install mysql-connector-python
   pip install pymysql
   pip install flask


