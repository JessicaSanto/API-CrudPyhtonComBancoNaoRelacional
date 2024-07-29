# RODAR O COMANDO DE INSTALAÇÃO - pip install pymongo
# Pymongo - é quem vai possibilitar a nossa conexão com o banco 
from pymongo import MongoClient

# ****************
# CONEXÃO COM BANCO DE DADOS 

connection_string = "mongodb://localhost:27017/"
# Para conectarmos com o banco, precisamos de uma string de conexão 
# String de Conexão - conjunto de informações necessárias para que uma aplicação estabeleça uma conexão com um banco de dados.
# Vai em 3 pontinhos -> Copy Connection String

client = MongoClient(connection_string)
# Utiliza uma string de conexão para conectar-se ao servidor MongoDB.
# A connection_string é uma string de conexão que contém informações necessárias para se conectar ao banco de dados 

db_connection = client["PrimeiroBanco"]
#  Seleciona o banco de dados chamado "PrimeiroBanco" do servidor conectado.

print(db_connection)
# Para testar se a nossa conexão deu certo. 

# ******************************
# REFERENCIAR A CONEXÃO COM A BASE DE DADOS CRIADA NO MONGO 

collection = db_connection.get_collection("primeiracolection")
# Especificamos que queremos trabalhar com a coleção chamada "primeiracolection" dentro do banco de dados "PrimeiroBanco". 
# A partir desse ponto, a variável collection pode ser usada para realizar operações CRUD de documentos dentro dessa coleção.

print(collection)
# Para testar se a nossa conexão com a base deu certo. 

# ********************************
# PARA BUSCAR INFORMAÇÕES NO BANCO DE DADOS

search_filter = { "idade": 30 } 
# Filtro no MongoBD, é uma especie de dicionário. 
# Então vamos passar que queremos que ele retorne todos os registros que tenham o campo "name" e com registro "Jessica"

response = collection.find(search_filter)
# print(response)
# Executa uma consulta na coleção "primeiracolection" usando os critérios definidos em search_filter.
# Este cursor permite manipular grandes conjuntos de dados de forma eficiente, sem carregar todos os resultados na memória de uma vez.

for registry in response:
    print(registry)
# Para cada registro dentro do response, exiba esse registro. 

