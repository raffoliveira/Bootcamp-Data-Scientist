import json, pymongo, pprint

def list_databases(con):
    con.list_database_names()

def print_collection_one(collection):
    pprint.pprint(collection.find_one())

def print_collection_many(collection):
    for docs in collection.find():
        pprint.pprint(docs)

def insert_one_docs(collection):
    doc = {'nome': 'Lucas', 'profissao': 'Pedagogo', 'idade': 23}
    collection.insert_one(doc)

def update_doc(collection):
    condition = {'nome': 'Maria'}
    value = {'$set':{'idade': 23}}

    collection.update_one(condition, value) 

def insert_via_file(con, path):
    data_collection = []
    with open(path) as file:
        for line in file:
            data_collection.append(json.loads(line))
            
        collection.insert_many(data_collection)



def main():

    con = pymongo.MongoClient('localhost', 27017)
    list_databases(con)
    db = con.Vendas
    collection = db.clientes
    # insert_one_docs(collection)
    path = '/home/rafael/Documents/Bootcamp/Module_2 - Coleta de Dados/MongoDB_Python/data_insert.json'
    insert_via_file(collection, path)
    print_collection_many(collection)



if __name__ == '__main__':
    main()