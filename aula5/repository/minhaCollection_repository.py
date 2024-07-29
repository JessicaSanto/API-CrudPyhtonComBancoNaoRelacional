from typing import Dict, List

from bson import ObjectId

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
# ******************************INSERÇÃO DE DADOS****************************************************************
        
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

#********************************************************************************************************
# ********************************* AULA 4 **************************************************************
# ******************************BUSCA DE DADOS****************************************************************
# BUSCAR VÁRIOS DOCUMENTO POR VEZ

    def select_many(self) -> List[Dict]:
# Define um método chamado select_many que pertence a uma classe (indicada pelo uso de self) e retorna uma lista de dicionários (List[Dict]).
        collection = self.db_connection.get_collection(self.__collection_name)
# Obtém uma referência à coleção do banco de dados usando a conexão (self.db_connection) e o nome da coleção (self.__collection_name) armazenados no objeto.
        data = collection.find({"name":  "Caique"},
        # Dentro das {}, adicionamos o filtro que queremos. Se deixar vazio, ele retorna todos os dados do banco.
        {"endereco": 0, "_id": 0})
        # Opções de Retorno. Para ocultar um determinado campo, valor : 0
        for x in data:
         print (x)

# BUSCAR UM DOCUMENTO POR VEZ

    def select_one(self) -> Dict:
# Define um método chamado select_one que pertence a uma classe (indicada pelo uso de self) e retorna um dicionário (Dict).
        collection = self.db_connection.get_collection(self.__collection_name)
# Obtém uma referência à coleção do banco de dados usando a conexão (self.db_connection) e o nome da coleção (self.__collection_name) armazenados no objeto.
        response = collection.find_one({"name":  "Jessica"})
        # Dentro das {}, adicionamos o filtro que queremos. Se deixar vazio, ele retorna todos os dados do banco.
        if response:
# Verifica se a consulta retornou algum document
                print(response)
        else:
                print("Nenhum documento encontrado.")
        return response
        # Opções de Retorno. Para ocultar um determinado campo, valor : 0

    
# ********************************* AULA 5 **************************************************************
# ******************************EDIÇÃO DE DADOS****************************************************************
# EDITAR UM DOCUMENTO POR VEZ

    def edit_registro(self) -> None:
# Define um método chamado edit_registro que pertence a uma classe (indicada pelo uso de self). Este método não retorna nada (None).
        collection = self.db_connection.get_collection(self.__collection_name)
# Obtém uma referência à coleção do banco de dados usando a conexão (self.db_connection) e o nome da coleção (self.__collection_name) armazenados no objeto.
        data = collection.update_one(
                {"_id": ObjectId("66a1abb4c47a3de9decc91f8")},
                {"$set": {"name": "Caique Zaneti"}}
        )
# Realiza uma atualização em um único documento que corresponde ao filtro { "_id": ObjectId("66a1abb4c47a3de9decc91f8") }.
# O filtro usa um ObjectId específico para identificar o documento.
# O operador $set é usado para atualizar o campo name para o valor "Caique Zaneti".
        print(data.modified_count)
# Imprime o número de documentos que foram modificados pela operação de atualização. 
# data.modified_count retorna o número de documentos que foram modificados (0 se nenhum documento foi modificado).


# EDITAR VÁRIOS DOCUMENTO 
    def edit_registros(self) -> None:
# Define um método chamado edit_registros que pertence a uma classe (indicada pelo uso de self). Este método não retorna nada (None).
        collection = self.db_connection.get_collection(self.__collection_name)
# Obtém uma referência à coleção do banco de dados usando a conexão (self.db_connection) e o nome da coleção (self.__collection_name) armazenados no objeto.
        data = collection.update_many(
                {"name": "Jessica"},
                {"$set": {"name": "Jessica Franzon"}}
        )
        print(data.modified_count)
# Realiza uma atualização em múltiplos documentos que correspondem ao filtro { "name": "Jessica" }.
# O operador $set é usado para atualizar o campo name para o valor "Jessica Franzon".
# Imprime o número de documentos que foram modificados pela operação de atualização. ,
# data.modified_count retorna o número de documentos que foram modificados (0 se nenhum documento foi modificado).
        
# EDITAR COLUNAS DO DOCUMENTO
    def edit_coluna(self, filtro, propriedades) -> None:
# Define um método chamado edit_coluna que pertence a uma classe (indicada pelo uso de self).
# Este método aceita dois parâmetros: filtro e propriedades, e não retorna nada (None).
        collection = self.db_connection.get_collection(self.__collection_name)
# Obtém uma referência à coleção do banco de dados usando a conexão (self.db_connection) e o nome da coleção (self.__collection_name) armazenados no objeto.
        data = collection.update_many(
                filtro,
                {"$set": propriedades}
        )
        print(data.modified_count)
# Realiza uma atualização em múltiplos documentos que correspondem ao filtro fornecido.
# O operador $set é usado para atualizar os campos especificados no dicionário propriedades.
# Imprime o número de documentos que foram modificados pela operação de atualização. 
# data.modified_count retorna o número de documentos que foram modificados (0 se nenhum documento foi modificado).
        
# ************************* EXCLUSÃO DE DADOS *********************************
# DELETAR VÁRIOS REGISTROS
    def delete_registros(self) -> None:
# Define um método chamado delete_registros que pertence a uma classe (indicada pelo uso de self). Este método não retorna nada (None).
        collection = self.db_connection.get_collection(self.__collection_name)
# Obtém uma referência à coleção do banco de dados usando a conexão (self.db_connection) e o nome da coleção (self.__collection_name) armazenados no objeto.
        data = collection.delete_many({"nome": "Caique"})
# Realiza uma exclusão em múltiplos documentos que correspondem ao filtro { "nome": "Caique" }.
        print(data.deleted_count)
# Imprime o número de documentos que foram excluídos pela operação de exclusão. 
# data.deleted_count retorna o número de documentos que foram excluídos (0 se nenhum documento foi excluído).

#DELETAR UM REGISTRO POR VEZ
    def delete_registro(self) -> None:
# # Define um método chamado delete_registros que pertence a uma classe (indicada pelo uso de self). Este método não retorna nada (None).
        collection = self.db_connection.get_collection(self.__collection_name)
# # Obtém uma referência à coleção do banco de dados usando a conexão (self.db_connection) e o nome da coleção (self.__collection_name) armazenados no objeto.
        data = collection.delete_one({"nome": "Jessica"})
# Realiza uma exclusão em múltiplos documentos que correspondem ao filtro { "nome": "Jessica" }.
        print(data.deleted_count)
# # Imprime o número de documentos que foram excluídos pela operação de exclusão. 
# data.deleted_count retorna o número de documentos que foram excluídos (0 se nenhum documento foi excluído).
