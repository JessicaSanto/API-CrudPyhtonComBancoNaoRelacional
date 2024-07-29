from models.connection_options.connection import DBConnectionHandler

db_handler = DBConnectionHandler()
# Inicializar uma instância da classe. Passa as informações de conexão mongo_db_infos 
# para o construtor da classe, que as armazena nas variáveis de instância.

conn1 = db_handler.get_db_connection()
# Obter a conexão com o banco de dados antes de chamar o método de conexão.
# Chama get_db_connection que retorna self.__db_connection, que inicialmente é None. Imprime None

print(conn1)
# Imprime o resultado

print("--------------------------------------------------------")
# Separa a impressão dos resultados para melhorar a visibilidade no terminal

db_handler.connect_to_db()
# Estabelecer a conexão com o banco de dados.  Chama connect_to_db, que cria um cliente MongoDB 
# e seleciona o banco de dados, armazenando a referência em self.__db_connection.

conn2 = db_handler.get_db_connection()
# Obter a conexão com o banco de dados após estabelecer a conexão. 
# Chama get_db_connection novamente, que agora retorna a referência ao banco de dados MongoDB. Imprime a referência ao banco de dados, que não será None.

print(conn2)
# Imprime o resultado
