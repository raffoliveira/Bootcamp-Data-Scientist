import mysql.connector, csv

def connect_database():
    
    mydb = mysql.connector.connect(host='localhost', user='root', password='mjovh', auth_plugin='mysql_native_password',
    database='bootcamp')

    print(mydb)

    return mydb

def show_databases(mycursor):

    #Retorna todos os esquemas criados no seu servidor de Banco de Dados
    mycursor.execute("SHOW DATABASES") 

    for db in mycursor:
        print(db)

def show_tables(mycursor):

    #Retorna todas as tabelas criados no seu esquema de Banco de Dados 
    mycursor.execute("SHOW TABLES")

    for db in mycursor:
        print(db)

def consult_tables(mycursor, table_name):

    #Consultar a tabela
    mycursor.execute(f"SELECT * FROM {table_name}")

    myresult = mycursor.fetchall() #todos os registros
    # myresult = mycursor.fetchone() #todos os registros

    if myresult == []:
        print('No register.')
    else:
        for mydata in myresult:
            print(mydata)

def insert_values_tables(mycursor, table_name, mydb):

    # Inserir dados em uma tabela

    query = f"INSERT INTO {table_name} (idcaracteristicasGerais, dsccaracteristicasGerais) VALUES (%s, %s)"
    values = (14, 'Terraço')

    mycursor.execute(query, values)

    #Fazer a confirmação da inserção
    mydb.commit()

    print(mycursor.rowcount, "registro(s) inserido(s).")

def insert_multiples_values_tables(mycursor, table_name, mydb):

    #Inserindo multiplos valores

    query = f"INSERT INTO {table_name} (idcaracteristicasGerais, dsccaracteristicasGerais) VALUES (%s, %s)"
    values = [(15, "Despensa"),(16,"Playground")]

    mycursor.executemany(query, values)

    mydb.commit()

    print(mycursor.rowcount, "registro(s) inserido(s).")

def insert_values_from_file_csv(mycursor, table_name, mydb, file_name):

    filename = f'/home/rafael/Documents/Bootcamp/Trabalho 2/arquivoscomplementaresTrabalhoPratico/{file_name}'

    #Abrir arquivo e inserir cada linha do arquivo na tabela cidade

    with open(filename, 'r') as incsvfile:
        reader = csv.reader(incsvfile, delimiter=',')
        next(reader, None)  # skip the headers
        for line in reader:       
            mycursor.execute (f"INSERT INTO {table_name} (CodigoCompletoIBGE, CodigoCidadeIBGE, NomeCidade, CodEstadoIBGE)\
            VALUES (%s, %s, %s, %s)", line)        
   
    mydb.commit()

    #db.close()
    incsvfile.close() #Fechar arquivo

def insert_values_from_file_txt(mycursor, table_name, mydb, file_name):

    filename = f'/home/rafael/Documents/Bootcamp/Trabalho 2/arquivoscomplementaresTrabalhoPratico/{file_name}'

    #Abrir arquivo e inserir cada linha do arquivo na tabela cidade

    with open(filename, 'r') as intxtfile:
        for line in intxtfile:       
            mycursor.execute (f"INSERT INTO {table_name} (idcaracteristicasGerais, idImovel, temCaracteristica)\
            VALUES (%s, %s, %s)", line.split(','))        
   
    mydb.commit()

    intxtfile.closed

def main():

    mydb = connect_database()
    mycursor = mydb.cursor()
    tables = ['caracteristicageralimovel', 'caracteristicasgerais', 'cidade', 'estado', 'imovel', 'tipounidade']
    file_name =['cidades.csv', 'caracteristicageralimovel.txt']

    #Para criar um banco de dados use o comando abaixo
    #mycursor.execute("CREATE DATABASE mydatabase")

    # show_databases(mycursor)
    # show_tables(mycursor)
    # consult_tables(mycursor, tables[1])
    # insert_values_tables(mycursor, tables[1], mydb)
    # insert_multiples_values_tables(mycursor, tables[1], mydb)
    # insert_values_from_file_csv(mycursor, tables[2], mydb, file_name[0])
    insert_values_from_file_txt(mycursor, tables[0], mydb, file_name[1])
    consult_tables(mycursor, tables[0])

if __name__ == '__main__':
    main()