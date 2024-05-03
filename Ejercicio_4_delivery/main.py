from clases import *
from manejadores import *
from Menu import *
opciones = {'0': 'Finalizar', '1': 'leer archivo Motos.', '2': 'Leer archivo Pedidos', '3': 'Cargar pedido manual', '4': 'Modificar tiempo de entrega', '5': 'Generar listado de comisiones', '6': 'Calcular Promedio de entregas'}
instancia_m = Manejador_motos()
instancia_p = Manejador_pedidos() 


if __name__ == '__main__':
    continuar = True
    while continuar:
        Menu(opciones)
        opcion = input('elija la opción deseada: ')
        control = validar_opcion(opcion, opciones)
        if not control:
            print('La opcion no es válida')
        else:
            if opcion == '0':
                continuar = False
                print('\nGracias por usar Perito sofware\n')
                
            elif opcion == '1':
                lista_motos = instancia_m.agregar_moto()
                
            elif opcion == '2':
                lista_pedidos = instancia_p.agregar_pedido()
                
            elif opcion == '3':
                conjunto_motos = instancia_m.crear_set_patentes()
                patente = input('Ingrese la patente a cargar: ')
                encontrado = instancia_m.validar_patente(patente, conjunto_motos)
                if not encontrado:

                    print('\npatente inválida')
                    
                else:
                    pedir_elementos_del_pedido(encontrado, instancia_p)
                    
            elif opcion == '4':
                conjunto_motos = instancia_m.crear_set_patentes()
                patente = input('Ingrese la patente a cargar: ')
                encontrado = instancia_m.validar_patente(patente, conjunto_motos)
                if not encontrado:
                    print('\npatente inválida')
                else:
                    pedido = input('Ingrese el numero de Pedido: ')
                    tpo_real_entrega = int(input('ingrese tiempo de entrega: '))
                    instancia_p.modificar_tiempo_entrega(patente, pedido, tpo_real_entrega)
            
            elif opcion == '5':
                conjunto_motos = instancia_m.crear_set_patentes()
                patente = input('Ingrese patente de Moto: ')
                validar = instancia_m.validar_patente(patente, conjunto_motos)
                if validar:
                    instancia_p.mostrar_pedidos_por_moto(patente, instancia_m)
                    
                else:
                    print('\npatente inválida')
                    
            
            elif opcion == '6':
                conjunto_motos = instancia_m.crear_set_patentes()
                patente = input('Ingrese patente de Moto: ')
                validar = instancia_m.validar_patente(patente, conjunto_motos)
                if validar:
                    promedio_tiempo = instancia_p.calcular_prom_tpo_entrega(patente, instancia_p)
                    conductor = instancia_m.obtener_conductor(patente)
                    
                    print(f'el tiempo promedio de entrega de {conductor} es: {promedio_tiempo:.2f}')
                    
                else:
                    print('\npatente inválida')
                
                
                