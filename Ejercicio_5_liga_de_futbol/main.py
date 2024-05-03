from manejador_equipo import *
from manejador_fechas import *
from clase_equipo import *
from clase_fecha import *
from menu import *

if __name__ == '__main__':
    menu_opciones = {'0': 'Finalizar', '1': 'Cargar lista equipos', '2': 'Cargar lista fechas', '3': 'Obtener info equipo', '4': 'Actualizar tabla equipos', '5': 'Ordenar equipos', '6': 'Guardar datos en archivos'}
    
    continuar = True
    while continuar:
        Menu(menu_opciones)
        
        opcion = validar_opcion(menu_opciones, input('ingrese la opción deseada: '))
        if not opcion:
            print('\nLa opción ingresada es incorrecta')
            
        else:
            if opcion == '0':
                continuar = False
            
            elif opcion == '1':
                instancia_manE = ManejadorEquipo()
                instancia_manE.cargar_equipo()
                # for equipo in instancia_manE.mostrar_lista():
                #     print(equipo.get_id_equipo())
                    
            elif opcion == '2':
                instanciaFecha = ManejadorFecha()
                instanciaFecha.cargarFechas()
                # for fecha in instanciaFecha.get_lista_fechas():
                #     print(f'fecha partido: {fecha.get_fecha_partido().strftime('%d/%m/%Y')} id local = {fecha.get_id_equipoLocal()}')
            
            
            elif opcion == '3':
                nombre_equipo = input('Ingrese el nombre para buscar info: ')
                id_equipo = instancia_manE.devolver_id_equipo(nombre_equipo)
                # print(id_equipo)
                if not id_equipo:
                    print('El equipo no existe')
                else:
                    instanciaFecha.mostrar_info(nombre_equipo, int(id_equipo))
                    
            
                    
                    
            elif opcion == '4':
                instancia_manE.actualizar_info_equipos(instanciaFecha)
                
                
            elif opcion == '5':
                instancia_manE.ordenar()
                
                
            elif opcion == '6':
                instancia_manE.guardar_datos_en_archivo()
                
                
                
                
                
    # instanciaFecha = ManejadorFecha()
    # 
    # instancia_manE.cargar_equipo()
    # instanciaFecha.cargarFechas()
    # 
    # instancia_manE.ordenar_equipos()
    
    
    
    # for equipo in instancia_manE.mostrar_lista():
    #     print(equipo.get_id_equipo())
    #     
    # for fecha in instanciaFecha.get_lista_fechas():
    #     print(f'fecha partido: {fecha.get_fecha_partido().strftime('%d/%m/%Y')} id local = {fecha.get_id_equipoLocal()}')