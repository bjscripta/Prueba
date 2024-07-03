from funcionesprin import *

while True:
    limpiar()
    print("""
          1. Registrar pedido
          2. Listar todos los pedidos
          3. Buscar pedido por RUT
          4. Imprimir hoja de ruta
          5. Salir del programa""")
    opc = validaropc()
    if opc==1:
        opcion1()
    elif opc==2:
        opcion2()
    elif opc==3:
        opcion3()
    elif opc==4:
        opcion4()
    else:
        opcion5()
    time.sleep(3)