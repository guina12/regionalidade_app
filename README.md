Configuração do Ambiente para o Projeto
Pré-requisitos
Antes de começar, certifique-se de que você possui os seguintes softwares e bibliotecas instalados:

Python 3.10 ou superior: O interpretador de Python necessário para rodar o projeto.
MySQL: Banco de dados relacional utilizado no projeto.
pip: Gerenciador de pacotes Python para instalar bibliotecas e dependências.

Passos para Configuração
1. Instalar o MySQL
Baixe e instale o MySQL a partir do site oficial. Durante a instalação:

Configure uma senha para o usuário root.
Anote a senha, pois será necessária para conectar ao banco de dados.

2. Criar o Banco de Dados
Após instalar o MySQL, siga os passos abaixo para criar o banco de dados:

Abra o terminal e conecte-se ao MySQL:
markdownCopymysql -u root -p

Insira a senha que você configurou durante a instalação do MySQL.
Crie um novo banco de dados e selecione-o:
markdownCopyCREATE DATABASE nome_do_banco;
USE nome_do_banco;


3. Instalar Dependências do Projeto
Execute os seguintes comandos para instalar as dependências necessárias:
markdownCopypip install mysql-connector-python
pip install pymysql
pip install flask
Alternativamente, você pode criar um arquivo requirements.txt com o seguinte conteúdo:
markdownCopymysql-connector-python
pymysql
flask
E então instalar todas as dependências de uma vez com:
markdownCopypip install -r requirements.txt
4. Estrutura do Projeto
Organize seu projeto com a seguinte estrutura:
markdownCopymeu_projeto/
├── app.py               # Arquivo principal do Flask
├── config.py            # Arquivo de configuração para banco de dados
├── requirements.txt     # Arquivo com dependências do projeto
└── templates/           # Diretório para templates HTML (se aplicável)
5. Configurar Variáveis de Ambiente
Para maior segurança e flexibilidade, é recomendado usar variáveis de ambiente para armazenar informações sensíveis. Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:
markdownCopyDB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua_senha
DB_NAME=nome_do_banco
FLASK_ENV=development
Instale a biblioteca python-dotenv para carregar as variáveis de ambiente:
markdownCopypip install python-dotenv
Adicione python-dotenv ao seu requirements.txt.
6. Configurar a Conexão com o Banco de Dados
No arquivo config.py, use as variáveis de ambiente para configurar a conexão com o banco de dados:
pythonCopyimport os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME')
}
7. Iniciar o Projeto
Com tudo configurado, você pode iniciar seu projeto Flask executando:
markdownCopypython app.py
Certifique-se de substituir os valores no arquivo .env pelos valores corretos que você definiu durante a configuração.
Notas Adicionais

Não se esqueça de adicionar .env ao seu arquivo .gitignore para evitar o compartilhamento acidental de informações sensíveis.
Para ambientes de produção, considere usar um gerenciador de configuração mais robusto ou variáveis de ambiente do sistema.
