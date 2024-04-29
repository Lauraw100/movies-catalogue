import os
from tabulate import tabulate
# import modules.importJson as imp
# import modules.add as add
# import modules.edit as edit
# import modules.delete as delete
# import modules.search as search
# import modules.assingnations as assg
# import modules.reports as list 
import modules.validations as v

# data = imp.readJson('data')
# history = imp.readJson('history')

def menuPRINCIPAL():
    try:
        os.system('cls')
        title=[["SISTEMA G&C DE INVENTARIO CAMPUSLANDS"]]
        print(tabulate(title,tablefmt="double_grid"))
        opciones = [["1.", "ACTIVOS"], ["2.", "PERSONAL "], ["3.", "ZONAS "], ["4.", "ASIGNACION DE ACTIVOS "],
                    ["5.", "REPORTES"], ["6.", "MOVIMIENTOS DE ACTIVOS"],["7.", "SALIR"]]
        print(tabulate(opciones, tablefmt="fancy_grid"))
        option =v.validacionInt2()

        if option == "1":
            menuACTIVOS()
        elif option == "2":
            menuPERSONAL()
        elif option == "3":
            menuZONAS()
        elif option == "4":
            menuASIGACTIVOS()
        elif option == "5":
            menuRep()
        elif option == "6":
            menuMOVIMIENTOSDEACTIVOS()
        elif option == "7":
            print("Vuelva pronto!")
            os.system('pause')
            exit()
        else:
            menuPRINCIPAL()
    except KeyboardInterrupt as i:
        exit()
    except ValueError as i:
        print('El valor ingresado no es valido')
        os.system('pause')
    except EOFError as i:
        print('El valor ingresado no es valido')
        os.system('pause')



#OPCION 1
def menuACTIVOS(): 
    try:
        os.system('cls')
        titulo=[["MENU ACTIVOS"]]
        print(tabulate(titulo,tablefmt="double_grid"))
        opciones = [["1.", "AGREGAR "], ["2.", "EDITAR "], ["3.", "ELIMINAR "], ["4.", "BUSCAR "], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
        print(tabulate(opciones, tablefmt="fancy_grid"))
        opcion =v.validacionInt2()
        
        if opcion == "1":
            add.addactivos(data)
            imp.writeJson(data, 'data')
        elif opcion == "2":
            edit.activosEdit(data)
            imp.writeJson(data, 'data')
        elif opcion == "3":
            delete.activosDelete(data)
            imp.writeJson(data, 'data')
        elif opcion == "4":
            search.activosSearch(data, 2)
            imp.writeJson(data, 'data')
        elif opcion == "5": 
            menuPRINCIPAL()
        else:
            menuACTIVOS()
    except KeyboardInterrupt as i:
        exit()
    except ValueError as i:
        print('El valor ingresado no es valido')
        os.system('pause')
    except EOFError as i:
        print('El valor ingresado no es valido')
        os.system('pause')

#OPCION2 
def menuPERSONAL():
    try: 
        os.system('cls')
        titulo=[["MENU PERSONAL"]]
        print(tabulate(titulo,tablefmt="double_grid"))
        opciones = [["1.", "AGREGAR "], ["2.", "EDITAR "], ["3.", "ELIMINAR "], ["4.", "BUSCAR "], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
        print(tabulate(opciones, tablefmt="fancy_grid"))
        opcion =v.validacionInt2()
        
        if opcion == "1":
            add.addpeople(data)
            imp.writeJson(data, 'data') 
        elif opcion == "2":
            edit.peopleEdit(data)
            imp.writeJson(data, 'data')
        elif opcion == "3":
            delete.peopleDelete(data)
            imp.writeJson(data, 'data')
        elif opcion == "4":
            search.personaSearch(data, 2)
            imp.writeJson(data, 'data')
        elif opcion == "5":   
            menuPRINCIPAL()
        else:
            menuPERSONAL()
    except KeyboardInterrupt as i:
        exit()
    except ValueError as i:
        print('El valor ingresado no es valido')
        os.system('pause')
    except EOFError as i:
        print('El valor ingresado no es valido')
        os.system('pause')

#OPCION3
def menuZONAS():
    try: 
        os.system('cls')
        titulo=[["MENU ZONAS"]]
        print(tabulate(titulo,tablefmt="double_grid"))
        opciones = [["1.", "AGREGAR "], ["2.", "EDITAR "], ["3.", "ELIMINAR "], ["4.", " Buscar"], ["5.", "REGRESAR AL MENU PRINCIPAL"]]
        print(tabulate(opciones, tablefmt="fancy_grid"))
        opcion =v.validacionInt2()
        
        if opcion == "1":
            add.addzone(data)
            imp.writeJson(data, 'data') 
        elif opcion == "2":
            edit.zonaEdit(data)
            imp.writeJson(data, 'data')
        elif opcion == "3":
            delete.zonDelete(data)
            imp.writeJson(data, 'data')
        elif opcion == "4":
            search.zonaSearch(data, 2)
            imp.writeJson(data, 'data')
        elif opcion == "5":
            menuPRINCIPAL()
        else:
            menuZONAS()
    except KeyboardInterrupt as i:
        exit()
    except ValueError as i:
        print('El valor ingresado no es valido')
        os.system('pause')
    except EOFError as i:
        print('El valor ingresado no es valido')
        os.system('pause')            

#OPCION4    
def menuASIGACTIVOS():
    try: 
        os.system('cls')
        titulo=[["ASIGNACION DE ACTIVOS"]]
        print(tabulate(titulo,tablefmt="double_grid"))
        opciones = [["1.", "CREAR ASIGNACION "], ["2.", "BUSCAR ASIGNACION "],["3.", "REGRESAR AL MENU PRINCIPAL"]]
        print(tabulate(opciones, tablefmt="fancy_grid"))
        opcion =v.validacionInt2()
        
        if opcion == "1":
            assg.newAssing(data)
            imp.writeJson(data, 'data')
            add.addHistoryAssing(data, history)
            imp.writeJson(data, 'data')
            imp.writeJson(history, 'history')
        elif opcion == "2":
            search.asigSearch(data, 2)
            imp.writeJson(data, 'data')
            imp.writeJson(history, 'history')
        elif opcion == "3":
            menuPRINCIPAL()
        else:
            menuASIGACTIVOS()
    except KeyboardInterrupt as i:
        exit()
    except ValueError as i:
        print('El valor ingresado no es valido')
        os.system('pause')
    except EOFError as i:
        print('El valor ingresado no es valido')
        os.system('pause')

      
#OPCION5
def menuRep():
    try:
        os.system('cls')
        titulo=[["MENU REPORTES"]]
        bandera= True
        op = 0 
        while op!="6":
            os.system('cls')
            print(tabulate(titulo,tablefmt="double_grid"))
            opciones = [["1.","LISTAR TODOS LOS ACTIVOS: \n>>"],["2.","LISTAR ACTIVOS POR CATEGORIA: \n>> "],["3.","LISTAR ACTIVOS DADOS DE BAJA POR DAÑO: \n>>"],
                        ["4.","LISTAR ACTIVOS Y ASIGNACION:\n>>"],["5.","LISTAR HISTORIAL DE MOV. DE ACTIVO: \n>>"],["6.","REGRESAR AL MENU PRINCIPAL: \n>>"]]
            print(tabulate(opciones, tablefmt="fancy_grid"))
            op =v.validacionInt2()
            if op == "1":
                list.listActivosall(data)
            elif op == "2":
                list.listActivoscategoria(data)
            elif op == "3":
                list.listActivosdaño(data)
            elif op == "4":
                list.listActivos_asg(data)
            elif op == "5":
                list.listHist(data)
            elif op =="6":
                menuPRINCIPAL()
            else:
                menuRep()
                print('Valor no encontrado\n')
    except KeyboardInterrupt as i:
        exit()
    except ValueError as i:
        print('El valor ingresado no es valido')
        os.system('pause')
    except EOFError as i:
        print('El valor ingresado no es valido')
        os.system('pause')
       
#OPCION5 
def menuMOVIMIENTOSDEACTIVOS(): 
    try:
        os.system('cls')
        titulo=[["MOVIMIENTOS DE ACTIVOS"]]
        print(tabulate(titulo,tablefmt="double_grid"))
        opciones = [["1.", "RETORNO DE ACTIVO"], ["2.", "DAR DE BAJA ACTIVO"], ["3.", "CAMBIAR ASIGNACION DE ACTIVO"],
                    ["4.", "ENVIAR A GARANTIA ACTIVO"], ["5.",  "REGRESAR AL MENU PRINCIPAL"]]
        print(tabulate(opciones, tablefmt="fancy_grid"))
        opcion =v.validacionInt2()
        
        if opcion == "1":
            activoEdit = edit.returnEdit(data, history)
            add.addHistoryState(data, history, activoEdit)
            imp.writeJson(data, 'data')
            imp.writeJson(history, 'history')
        elif opcion == "2":
            activoEdit = edit.estadoEdit(data, 2)
            add.addHistoryState(data, history, activoEdit)
            imp.writeJson(data, 'data')
            imp.writeJson(history, 'history')
        elif opcion == "3":
            edit.activeAssingEdit(data, history)
            imp.writeJson(data, 'data')
            imp.writeJson(history, 'history')
        elif opcion == "4":
            activoEdit = edit.estadoEdit(data, 3)
            add.addHistoryState(data, history, activoEdit)
            imp.writeJson(data, 'data')
            imp.writeJson(history, 'history')
        elif opcion == "5":
            menuPRINCIPAL()
        else:
            menuMOVIMIENTOSDEACTIVOS()
    except KeyboardInterrupt as i:
        exit()
    except ValueError as i:
        print('El valor ingresado no es valido')
        os.system('pause')
    except EOFError as i:
        print('El valor ingresado no es valido')
        os.system('pause')





















































































































