import os,time,msvcrt,csv
pedidos = []
def opcion1():
    print("Registrar pedid")
    rut = validarrut()
    nombre = validarnombre()
    direccion = validardireccion()
    comuna = validarcomuna()
    dpedido = detallepedido()
    pedido = {
        "rut": rut,
        "nombre": nombre,
        "direccion": direccion,
        "comuna": comuna,
        "detallePedido": dpedido
    }
    pedidos.append(pedido)
    print("Pedido registrado!")

def opcion2():
    print("LISTAR PEDIDO/S")
    if len(pedidos)==0:
        print("Error, no hay pedidos registrados")
    else:
        for p in pedidos:
            print(f"RUT: {p["rut"]} Cliente: {p["nombre"]} Direccion: {p["direccion"]} Comuna: {p["comuna"]}")

def opcion3():
    print("BUSCAR PEDIDO POR RUT")
    if len(pedidos)==0:
        print("Error, no hay pedidos registrados")
    else:
        brut = input("Ingrese rut: ")
        if brut in pedidos:
            for p in pedidos:
                print(f"RUT: {p["rut"]} Cliente: {p["nombre"]} Direccion: {p["direccion"]} Comuna: {p["comuna"]}")
        else:
            print("Error, rut no registrado")

def opcion4():
    print("IMPRIMIR HOJA DE RUTA")
    if len(pedidos)==0:
        print("Error, no hay pedidos")
    else:
        bcomuna = input("Ingrese sector a buscar: ('SANTIAGO','PIRQUE','Colina')").lower()
        if bcomuna=="santiago" or bcomuna=="colina" or bcomuna=="pirque":
            with open(f"{bcomuna}" + ".csv", "w",newline="") as archivo:
                camps = ("rut","nombre","direccion","comuna","detallePedido")
                write = csv.DictWriter(archivo,fieldnames=camps)
                write.writeheader()
                write.writerows(pedidos)
                print("Archivo creado con exito!")
        else:
            print("Error, seleccione uno de los sectores mencionados")

def opcion5():
    print("ADIOS")
    exit()

def validarrut():
    while True:
        try:
            rut = int(input("Ingrese rut: (Ej: 217867533)"))
            if len(str(rut))==9:
                return rut
            else:
                print("Error, el rut debe contener 9 numeros")
        except:
            print("Error, solo se permiten numeros enteros")

def validarnombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre) >= 3:
            return nombre
        else:
            print("Error, el nombre debe contener al menos 3 caracteres")

def validardireccion():
    while True:
        direccion = input("Ingrese direccion: ")
        if len(direccion) > 3:
            return direccion
        else:
            print("Error, la direccion debe contener al menos 3 caracteres")

def validarcomuna():
    while True:
        comuna = input("Ingrese comuna: ")
        if len(comuna) > 3:
            return comuna
        else:
            print("Error, la comuna debe contener al menos 3 caracteres")

def validaropc():
    while True:
        try:
            opcs = int(input("Ingrese opcion: "))
            if opcs in (1,2,3,4,5):
                return opcs
            else:
                print("Error, opcion no disponible")
        except:
            print("Error, solo se permiten numeros enteros")
    
def limpiar():
    os.system("cls")

def detallepedido():
    while True:
        print("Tipos de cilindros '1) 5KG 12.500$' '2) 15KG 25.500' '3 Salir' ")
        cilincinco = 12500
        cilinquince = 25500
        cantidadcin = 0
        cantidadquin = 0
        total = cantidadquin * cantidadcin
        opcion = int(input("Ingrese tipo de cilindro: "))
        if opcion==1:
            cantidadcin = int(input("Ingrese cantidad: "))
            total = cilincinco * cantidadcin
            return cantidadcin
        elif opcion==2:
            cantidadquin = int(input("Ingrese cantidad: "))
            total = cilinquince * cantidadquin
            return cantidadquin
        else:
            print(total)
            return opcion
                
                
        
