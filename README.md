# Configuração do Ambiente para o Projeto

## Pré-requisitos

Antes de começar, certifique-se de que você possui os seguintes softwares e bibliotecas instalados:

- [Python 3.10 ou superior](https://www.python.org/downloads/): O interpretador de Python necessário para rodar o projeto.
- [MySQL](https://dev.mysql.com/downloads/mysql/): Banco de dados relacional utilizado no projeto.
- [pip](https://pip.pypa.io/en/stable/installation/): Gerenciador de pacotes Python para instalar bibliotecas e dependências.

## Passos para Configuração

### 1. Instalar o MySQL

Baixe e instale o MySQL a partir do [site oficial](https://dev.mysql.com/downloads/mysql/). Durante a instalação:

- Configure uma senha para o usuário `root`.
- Anote a senha, pois será necessária para conectar ao banco de dados.

### 2. Criar o Banco de Dados

Após instalar o MySQL, siga os passos abaixo para criar o banco de dados:

1. Abra o terminal e conecte-se ao MySQL:

   ```
   mysql -u root -p
   ```

2. Insira a senha que você configurou durante a instalação do MySQL.

3. Crie um novo banco de dados e selecione-o:

   ```
   CREATE DATABASE nome_do_banco;
   USE nome_do_banco;
   ```

### 3. Instalar Dependências do Projeto

Execute os seguintes comandos para instalar as dependências necessárias:

```
pip install mysql-connector-python
pip install pymysql
pip install flask
```

### 4. Estrutura do Projeto

Organize seu projeto com a seguinte estrutura:

```
meu_projeto/
├── app.py               # Arquivo principal do Flask
├── config.py            # Arquivo de configuração para banco de dados
├── requirements.txt     # Arquivo com dependências do projeto
└── templates/           # Diretório para templates HTML (se aplicável)
```

### 5. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=nome_do_banco
FLASK_ENV=development
```

Instale a biblioteca python-dotenv:

```
pip install python-dotenv
```

### 6. Configurar a Conexão com o Banco de Dados

No arquivo `config.py`, use as variáveis de ambiente para configurar a conexão com o banco de dados:

```python
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}
```

### 7. Iniciar o Projeto

Com tudo configurado, você pode iniciar seu projeto Flask executando:

```
python app.py
```

Certifique-se de substituir os valores no arquivo `.env` pelos valores corretos que você definiu durante a configuração.

### Notas Adicionais

- Adicione `.env` ao seu arquivo `.gitignore` para evitar o compartilhamento acidental de informações sensíveis.
- Para ambientes de produção, considere usar um gerenciador de configuração mais robusto ou variáveis de ambiente do sistema.
