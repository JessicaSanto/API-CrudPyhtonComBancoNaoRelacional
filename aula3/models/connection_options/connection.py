from pymongo import MongoClient
from models.connection_options.mongodb_configs import mongo_db_infos
# Vamos importar as informações de conexões que temos

# 1. STRING DE CONEXÃO - conjunto de informações necessárias para que uma aplicação estabeleça uma conexão com um banco de dados.

class DBConnectionHandler:
# Gerente de conexão e vamos iniciar o método construtor e adicionar nossa string de conexão
    def __init__(self) -> None:
    # Dois __ significa que será privado
        self.__connection_string = 'mongodb://{}:{}/'.format(
    # a função format() permite que cada {} da URI seja descrita abaixo na ordem
            mongo_db_infos["HOST"],
            mongo_db_infos["PORT"]
    # podemos adicionar também o usuario e a senha
            # mongo_db_infos["USERNAME"],
            # mongo_db_infos["PASSWORD"],
        )
        
# 2. SALVAR AS INFORMAÇÕES DE CLIENT E CONEXÃO
 
        self.__database_name = mongo_db_infos["DB_NAME"]
    # Atribuir o nome do banco de dados a uma variável de instância
        self.__client = None
    # Esta variável será usada para armazenar a instância do cliente MongoDB após a conexão ser estabelecida.
        self.__db_connection = None
    # Esta variável será usada para armazenar a referência ao banco de dados específico após a conexão ser estabelecida.
        
# 3. EFETIVAMENTE CONECTAR NO BANCO DE DADOS

    def connect_to_db(self):
    # Este método será chamado para conectar-se ao MongoDB e selecionar o banco de dados especificado.
        self.__client = MongoClient(self.__connection_string)
    # Cria uma instância de MongoClient usando a string de conexão e estabelecer a conexão com o servidor MongoDB. 
    # Esta string de conexão inclui informações como o endereço do servidor MongoDB, a porta e credenciais de autenticação. 
    # A instância do cliente MongoDB é armazenada em self.__client.
        self.__db_connection = self.__client[self.__database_name]
    # Selecionar o banco de dados específico no servidor MongoDB e armazena a referência
    # Usa a instância do cliente MongoDB (self.__client) para acessar o banco de dados cujo nome está armazenado em self.__database_name. 

# 4. ACESSO À CONEXÃO DO BANCO DE DADOS PARA CAPTURAR ALGUM ELEMENTO CASO SEJA NECESSÁRIO

    def get_db_connection(self):
        return self.__db_connection
    # Fornecer acesso à conexão com o banco de dados.
    
    def get_db_client(self):
        return self.__client
    # Fornecer acesso ao cliente MongoDB usada para conectar ao servidor.