def ValidationsInt():
    try:
        x=int(input('>>'))
        if x<0:
            print('Solo positivos')
            return ValidationsInt()
        else:
            return x
    except ValueError:
        print('Solo numeros, ingrese nuevamente')
        return ValidationsInt()

def ValidationsKeyNew(data:dict,tipo):
    try:
        x=input('>>').upper()
        data[tipo][x]
        print('LLave ya existente')
        return ValidationsKeyNew(data,tipo)
    except KeyError:
        return x
    
def ValidationsInt2():
    try:
        x=int(input('>>'))
        if x<0:
            print('Solo positivos')
            return ValidationsInt()
        else:
            return str(x)
    except ValueError:
        print('Solo numeros, ingrese nuevamente')
        return ValidationsInt2()
    
def ValidationsKeyNew2(data:dict,tipo):
    try:
        x=int(input('>>'))
        data[tipo][x]
        print('LLave ya existente')
        return ValidationsKeyNew2(data,tipo)
    except ValueError:
        print('Solo numeros')
        return ValidationsKeyNew2(data,tipo)
    except KeyError:
        return x
    
def OutOfRange(range):
    try:
        x=int(input('>>'))
        if x<0:
            print('Solo positivos')
            return OutOfRange(range)
        if x>range:
            print('Numero esta afuera del rango')
            return OutOfRange(range)
        else:
            return x
    except ValueError:
        print('Solo numeros, ingrese nuevamente')
        return ValidationsInt()    
    