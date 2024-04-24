import json
def json_inventario(inventario):
    with open('data/inventario.json',"w") as ce:
        json.dump(inventario,ce,indent=3)

def add_book():
    name_book= input(str("Enter the name of the book"))  
    genre=input(str("book genre"))