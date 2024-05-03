from clase_controlador import *
from funciones import *


if __name__ == '__main__':
    lista_opción_menu = [0, 1, 2, 3, 4, 5, ]
    lista_semana = [1, 2, 3, 4, 5, 6, 7]
    lista_sucursales = [1, 2, 3, 4, 5]
    instancia = Controlador()
    
    continuar = False
    
    while not continuar:
        
        menu_principal()
        elección = int(input('Elija la opción deseada: '))
        validar_opcion(elección, lista_opción_menu)
        
        if elección == 0:
            continuar = True
        
        elif elección == 1:
            
            instancia.cargar_datos_automatico()
            # menú_de_semana()
            # print('Elija la opción del dia: ')
            # dia = validar_opcion(int(input('Ingrese la opción deseada: ')), lista_semana)
            # sucursal = validar_opcion(int(input('Ingrese numero de sucursal: ')), lista_sucursales)
            # importe = float(input('Ingrese el importe de la venta: '))
            # instancia.cargar_datos_manual(dia, sucursal, importe)  
            
                      
        elif elección == 3:
            dia = validar_opcion(int(input('Ingrese el dia de la semana: ')), lista_semana)
            instancia.sucursal_mas_ventas_en_un_dia(dia)
            
            
        elif elección == 2:
             sucursal = validar_opcion(int(input('Ingrese numero de sucursal: ')), lista_sucursales)
             instancia.calcular_vta_acum(sucursal)
             
             
        elif elección == 4:
            instancia.sucursal_menos_ventas_semana()
            
            
        elif elección ==5:
            instancia.total_facturacion_semanal()
            
