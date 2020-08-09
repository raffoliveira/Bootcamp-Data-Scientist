#!/usr/bin/env python
# coding: utf-8

# # Coleta de Dados no MySQL utilizando o Python

# #### Antes de executar este notebook pela primeira vez, instale o pacote mysql.connector
# 
# Para instalar o pacote, utilizando o prompt do Anaconda, execute o comando abaixo:
# 
# ##### *conda install -c anaconda mysql-connector-python*

# In[ ]:


# importa pacote SEMPRE antes de usar

import mysql.connector


# In[ ]:


# conexão ao SGBD
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='igti',
    database='aula1'
)

print(mydb)

mycursor = mydb.cursor()


# In[ ]:


mycursor.execute("SHOW TABLES")

for db in mycursor:
    print(db)


# In[ ]:


mycursor.execute("SELECT * FROM caracteristicasgerais")

myresult = mycursor.fetchall()

for mydata in myresult:
    print(mydata)


# In[ ]:


# Inserir dados em uma tabela

query = "INSERT INTO caracteristicasgerais (idcaracteristicasGerais, dsccaracteristicasGerais) VALUES (%s, %s)"
values = (1, "Portaria 24 horas")

mycursor.execute(query, values)

#Fazer a confirmação da inserção
#mydb.commit()

#print(mycursor.rowcount, "registro(s) inserido(s).")


# In[ ]:


mydb.commit()

print(mycursor.rowcount, "registro(s) inserido(s).")


# In[ ]:


mycursor.execute("SELECT * FROM caracteristicasgerais")

myresult = mycursor.fetchall()

for mydata in myresult:
    print(mydata)


# In[ ]:


#Inserindo multiplos valores
values = [(2, "Elevador"),(3,"Piscina")]

mycursor.executemany(query, values)

#mydb.commit()

#print(mycursor.rowcount, "registro(s) inserido(s).")


# In[ ]:


mycursor.execute("SELECT * FROM caracteristicasgerais")

myresult = mycursor.fetchall()

for mydata in myresult:
    print(mydata)


# In[ ]:


import csv

#Leitura de arquivo sem utilizar biblioteca Pandas

filename = 'C:\Bootcamp\Datasets\CSV\cidades.csv'


# In[ ]:


with open(filename, 'r') as incsvfile:
    reader = csv.reader(incsvfile, delimiter=',')
    next(reader, None)  # skip the headers
    query = "INSERT INTO cidade (CodigoCompletoIBGE, CodigoCidadeIBGE, NomeCidade, CodEstadoIBGE) VALUES (%s, %s, %s, %s)"    
    for line in reader:       
        #mycursor.execute ("INSERT INTO cidade (CodigoCompletoIBGE, CodigoCidadeIBGE, NomeCidade, CodEstadoIBGE)\
        #          VALUES (%s, %s, %s, %s)",line)        
        mycursor.execute(query, line)


# In[ ]:


mydb.commit()

# Fecha arquivo
incsvfile.close()


# In[ ]:


mycursor.execute("SELECT count(*) FROM cidade")

myresult = mycursor.fetchone()

print(myresult)


# In[ ]:


# fecha conexão
mydb.close()


# ## Agora vamos usar o Knime 

# ##### Vamos realizar a atividade 12

# ### Retornamos com a atividade 10

# In[ ]:


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='igti',
    database='aula1'
)

mycursor = mydb.cursor()


# In[ ]:


filename = 'C:\Bootcamp\Datasets\TXT\caracteristicaImovel.txt'

with open(filename, "r", encoding='utf-8') as fileobject:
    for line in fileobject:
        query = "INSERT INTO caracteristicageralimovel (idcaracteristicasGerais,idImovel,temCaracteristica)            VALUES (%s)" % line
        mycursor.execute(query)

mydb.commit()


# In[ ]:


#Consultar a tabela
mycursor.execute("SELECT * FROM caracteristicageralimovel")

myresult = mycursor.fetchall() #todos os registros

for mydata in myresult:
    print(mydata)


# ##### Testar as assertivas

# In[ ]:


query = "INSERT INTO caracteristicageralimovel (idcaracteristicasGerais,idImovel,temCaracteristica) VALUES (%s, %s, %s)"     
values = (4,22,1)

mycursor.execute(query, values)

mydb.commit()

print(mycursor.rowcount, "registro(s) inserido(s).")


# In[ ]:


query = "INSERT INTO caracteristicageralimovel (idcaracteristicasGerais,idImovel,temCaracteristica) VALUES(%s, %s, %s)"     
values = [(4,22,1),(4,23,1),(4,26,0)]
          
mycursor.executemany(query, values)

mydb.commit()

print(mycursor.rowcount, "registro(s) inserido(s).")


# In[ ]:


value = "6,29,0"
query = "INSERT INTO caracteristicageralimovel (idcaracteristicasGerais,idImovel,        temCaracteristica) VALUES (%s)" % value

mycursor.execute(query, value)

mydb.commit()

print(mycursor.rowcount, "registro(s) inserido(s).")


# In[ ]:


query = "INSERT INTO caracteristicageralimovel (idcaracteristicasGerais,idImovel,temCaracteristica) VALUES (%s, %s, %s)"     
values = (4,22,1)
          
mycursor.sendQuery(query, values)

mydb.commit()

print(mycursor.rowcount, "registro(s) inserido(s).")


# In[ ]:


mydb.close() #fecha BD
infile.close() #Fechar arquivo


# ### Voltamos ao Knime para realizar a atividade 13

# In[ ]:




