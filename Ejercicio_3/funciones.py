def menu_principal():
   
    print("""
          0_ Terminar
          1_ Cargar Datos
          2_ Calcular Facturación de Sucursal
          3_ Obtener sucursal con mas facturación del día
          4_ Calcular sucursal con menos facuración de la semana
          5_ calcular Facturación total de la semana          
          
          """)
    

def validar_opcion(opcion: int, lista: list):
    while opcion not in lista:
        print('La opcion elegida no es válida: ')
        opcion = int(input('Ingrese una opción correcta: '))
    return opcion
                
        
def menú_de_semana():
    print("""          
          Elija la opción deseada:
          1_ Lunes
          2_ Martes
          3_ Miercoles
          4_ Jueves
          5_ Viernes
          6_ Sabado
          7_ Domingo
          
          """)

    
     
    