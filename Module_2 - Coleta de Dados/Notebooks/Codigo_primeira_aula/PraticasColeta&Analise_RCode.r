install.packages('RMariaDB')

#importação do pacote
library(RMariaDB)
# require(RMariaDB)

#Importa pacote RMariaDB se ele ainda não foi carregado
if(!"RMariaDB" %in% (.packages())){require(RMariaDB)}

#Conecta ao SGBD MySQL --> Banco de dados bootcamp
con <- dbConnect(MariaDB(), user = "root", password = "igti",
                 dbname = "aula1", host = "localhost",serverTimezone='UTC')

#Para listar quais tabela existem no esquema .bootcamp. execute:

#Lê a lista de tabelas no BD
tables <- dbListTables(con) 
tables

#Para consultar quais os dados de uma tabela execute:
# dbReadTable(nome-da-conexao,"nome-da-tabela")

#Consulta os dados da tabela *estado*
tabledata <- dbReadTable(con,"estado")
tabledata

#Consulta os dados da tabela *tipounidade*
tabledata <- dbReadTable(con,"tipounidade")
tabledata

#Para executar um comando SQL execute:
#dbSendQuery(nome-da-conexao,"comando")

# Vamos inserir uma nova linha na tabela tipounidade
# Cria o comando e salva na variável query
query <-  "INSERT INTO tipounidade(idTipoUnidade,dscTipoUnidade) VALUES('7','Loft');"

# Opcional.
#print(query)

results <- dbSendQuery(con,query)
results

# Limpa resultados
dbClearResult(results)

#Consulta os dados da tabela *tipounidade*
tabledata <- dbReadTable(con,"tipounidade")
tabledata

id <- 8
desc <- 'Chácara'

query <-  paste("INSERT INTO tipounidade(idTipoUnidade,dscTipoUnidade) VALUES(",id,",'",desc,"');",sep='')

# Opcional.
print(query)

results <- dbSendQuery(con,query)
results

# Limpa resultados
dbClearResult(results)

#Consulta os dados da tabela *tipounidade*
tabledata <- dbReadTable(con,"tipounidade")
tabledata

#install.packages('xlsx')

#Importa pacote xlsx se ele ainda não foi carregado
if(!"xlsx" %in% (.packages())){require(xlsx)}

datasetpath <- 'C:/Bootcamp/Datasets/XLS'

filename <- paste(datasetpath,"/estados.xlsx",sep='')
filename

insertdata <- read.xlsx(filename, sheetIndex=1, header=TRUE,encoding="UTF-8")
insertdata


dbWriteTable(con,'estado',insertdata,append = TRUE)

#Consulta os dados da tabela *estado*
tabledata <- dbReadTable(con,"estado")
tabledata

#Importa pacote xlsx se ele ainda não foi carregado
# if(!"xlsx" %in% (.packages())){require(xlsx)}

query <- "SELECT * FROM estado;"

# Opcional.
#print(query)

results <- dbGetQuery(con,query)
results


resultado <- dbReadTable(con,"caracteristicasgerais")
resultado

#Antes de excutar esta célula, garanta que o caminho do arquivo estados.xlsx esteja correto.

filename <- "C:/Bootcamp/Datasets/CSV/caracteristicasgerais.csv"

insertdata <- read.csv(filename)


dbWriteTable(con,'caracteristicasgerais',insertdata,append = TRUE)

#Consulta os dados da tabela *caracteristicasgerais*

results <- dbReadTable(con,"caracteristicasgerais")
results
