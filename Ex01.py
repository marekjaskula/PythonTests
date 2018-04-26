def  ShowVariable(vari):
    print(vari, type(vari))
lista = [100, 20, 5]


slownik = {
    "Samochód" : "Citroen",
    "Typ" : "C5"
}

ShowVariable(lista)
ShowVariable(slownik)

def Wyswietl(vari, lista_var= None, *args, **kargs):
    print("START -> ")
    ShowVariable(vari)
    if lista_var:
        for element in lista_var:
            ShowVariable(element)
    print("Args =", args)
    print("KArgs = ", kargs)
    print("STOP")


Wyswietl(1, [1,2,3], 'arg3', 'arg4', arg5=12, arg6={"stos": "stosik"})
