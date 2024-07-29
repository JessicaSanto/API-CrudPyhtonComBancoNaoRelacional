from models.connection_options.connection import DBConnectionHandler
from repository.minhaCollection_repository import MinhaCollectionRepository

db_handler = DBConnectionHandler()
# Inicializar uma instância da classe. Passa as informações de conexão mongo_db_infos 
# para o construtor da classe, que as armazena nas variáveis de instância.

db_handler.connect_to_db()
# Estabelecer a conexão com o banco de dados.  Chama connect_to_db, que cria um cliente MongoDB 
# e seleciona o banco de dados, armazenando a referência em self.__db_connection.

db_connection = db_handler.get_db_connection()
# Obter a conexão com o banco de dados após estabelecer a conexão. 
# Chama get_db_connection novamente, que agora retorna a referência ao banco de dados MongoDB. Imprime a referência ao banco de dados, que não será None.


# **************************** AULA 3 ****************************
minha_collection_repository = MinhaCollectionRepository(db_connection)

# O beneficio de trabalhar com um banco de dados não relacional, é a liberdade que temos de trabalhar com as informações.
# Por exemplo, em um pedido de ifood, podemos adicionar uma pizza e um refrigerante. Em outro pedido podemos adicionar uma pizza e um hamburguer. 
#  Além de permitir trabalhar com diversos tipos de dados.

order = {
    "name": "Jessica",
    "endereco": "Rua Niteroi",
    "pedidos": {
        "pizza": "1",
        "refrigerante": "2",
        "batata": "1"
    }
}

order2 = {
    "name": "Caique",
    "endereco": "Rua Niteroi",
    "pedidos": {
        "pizza": "1",
        "hamburguer": 2,
        "pizza doce": 5
    }
}

minha_collection_repository.insert_document(order2)

list_of_documents = [
    {"nome": "Jessica"},
    {"nome": "Caique"},
    {"nome": "Carol"}
]
minha_collection_repository.insert_list_of_documents(list_of_documents)
