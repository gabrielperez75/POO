from clase import *
from funciones import *


if __name__ == '__main__':
    
    continuar = True
    while continuar:
        menu()
        opcion = validar_opcion()
        if opcion == '1':
            listado_cajas = test_cuenta()
            
        elif opcion == '2':
            # cuil, importe = pedir_datos_para_operar()
            cuil = validar_cuil(input('Ingrese el número de CUIL: '))
            
            datos_de_cuenta = buscar_dato_de_cuenta(cuil, listado_cajas)
            if datos_de_cuenta == 0:
                print('cuenta no encontrada')
                
            else:
                importe = float(input('ingrese importe: '))
            
                resultado = depositar(importe)
                if resultado == 1:
                    grabar_deposito(importe, datos_de_cuenta)
                    print(f'Nuevo Saldo: {datos_de_cuenta.get_saldo()}')
            
        elif opcion == '3':
            # cuil, importe = pedir_datos_para_operar()
            cuil = validar_cuil(input('Ingrese el número de CUIL: '))
            
            datos_de_cuenta = buscar_dato_de_cuenta(cuil, listado_cajas)
            if datos_de_cuenta == 0:
                print('cuenta no encontrada')
            else:
                importe = float(input('ingrese importe: '))
                disponible = verificar_saldo(importe, datos_de_cuenta.get_saldo())
                if disponible == -1:
                    print(f'Saldo Insuficiente el disponible es {datos_de_cuenta.get_saldo()}')
                else:
                    grabar_extraccion(importe, datos_de_cuenta)
                    print(f'Operación Exitosa! Nuevo Saldo Disponible: {datos_de_cuenta.get_nombre()} {datos_de_cuenta.get_saldo()}')
                    
            
        elif opcion == '4':
            
            cuil_buscado = validar_cuil(input('Ingrese el cuil para buscar datos: '))
            cuenta_encontrada = buscar_dato_de_cuenta(cuil_buscado, listado_cajas)
            if cuenta_encontrada == 0:
                print('No se pudo encontrar el usuario')
            else:
                print(f'\nEl usuario encontrado es: {cuenta_encontrada.get_nombre()} {cuenta_encontrada.get_apellido()}')
             
             
        elif opcion == '0':
            continuar = False
    
    
    print('\nGracias por operar con nosotros')
    # listado_cajas = test_cuenta()
    

        
    