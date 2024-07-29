from typing import Dict, List

class MinhaCollectionRepository:
# Esta classe será responsável por interagir com a coleção primeiracollection no banco de dados MongoDB.

    def __init__(self, db_connection) -> None:
# __init__ -> Define o construtor da classe, que será chamado quando uma nova instância da classe for criada.
# METODO CONSTRUTOR -> em uma classe Python é um método especial chamado __init__. 
# Este método é automaticamente chamado quando você cria uma nova instância da classe.
# O propósito do construtor é inicializar a nova instância da classe, configurando os atributos iniciais necessários e 
# realizando qualquer configuração ou preparação que a instância precise.
# db_connection -> Recebe uma conexão com o banco de dados MongoDB.

        self.__collection_name = "primeiracollection"
# Armazena o nome da coleção na variável privada __collection_name para uso posterior.

        self.db_connection = db_connection
# Permite que a instância da classe utilize a conexão do banco de dados para realizar operações na coleção.

# ******************************************************************************************************************
        
# INSERIR UM DOCUMENTO POR VEZ
    
    def insert_document(self, document: Dict) -> Dict:
# def -> Define uma nova função/método.
# insert_document -> Nome do método.
# -> Dict: Anotação de tipo que indica que este método deve retornar um dicionário.
# Declaração do parâmetro document, que é esperado ser um dicionário (Dict). 
# DICIONARIO -> estrutura de dados que permite armazenar/organizar informações de forma eficiente, utilizando uma estrutura de chave-valor.

        collection = self.db_connection.get_collection(self.__collection_name)
# collection -> Variável local que armazenará a referência à coleção MongoDB.
# self.db_connection -> Acessa o atributo db_connection da instância atual, que contém a conexão com o banco de dados.
# get_collection(self.__collection_name) -> Método da conexão do banco de dados que retorna a coleção chamada self.__collection_name, que neste caso é "primeiracollection".
# Objetivo: Obter a coleção específica do banco de dados MongoDB onde o documento será inserido.

        collection.insert_one(document)
# collection -> A variável que armazena a referência à coleção MongoDB obtida na linha anterior.
# insert_one(document) -> Método da coleção que insere um único documento (dicionário) no banco de dados.
# document -> O dicionário que foi passado como argumento ao método insert_document.
# Objetivo: Inserir o documento fornecido na coleção MongoDB.

        return document
# O método retorna o próprio documento que foi inserido.
    
# INSERIR MAIS DE UM DOCUMENTO POR VEZ

    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
# list_of_documents: List[Dict] -> Declaração do parâmetro list_of_documents, que é esperado ser uma lista de dicionários (List[Dict]). 
# -> List[Dict]: Anotação de tipo que indica que este método deve retornar uma lista de dicionários.

        collection = self.db_connection.get_collection(self.__collection_name)
# collection: Variável local que armazenará a referência à coleção MongoDB.
# self.db_connection: Acessa o atributo db_connection da instância atual, que contém a conexão com o banco de dados.
# get_collection(self.__collection_name): Método da conexão do banco de dados que retorna a coleção chamada self.__collection_name, que neste caso é "primeiracollection".
# Objetivo: Obter a coleção específica do banco de dados MongoDB onde os documentos serão inseridos.

        collection.insert_many(list_of_documents)
# collection: A variável que armazena a referência à coleção MongoDB obtida na linha anterior.
# insert_many(list_of_documents): Método da coleção que insere múltiplos documentos (lista de dicionários) no banco de dados.
# list_of_documents: A lista de dicionários que foi passada como argumento ao método insert_list_of_documents.
# Objetivo: Inserir os documentos fornecidos na coleção MongoDB.

        return list_of_documents
# O método retorna a própria lista de documentos que foi inserida.
