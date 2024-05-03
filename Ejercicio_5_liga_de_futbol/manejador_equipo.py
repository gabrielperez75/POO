from clase_equipo import Equipo
from manejador_fechas import *
from clase_fecha import Fecha_futbol
import csv

class ManejadorEquipo:
    """se definen las funciones para administrar la clase Equipo
    """
    __lista_equipos: list
    
    def __init__(self) -> None:
        self.__lista_equipos = []
        self.__lista_actualizada = []
        
    
    def cargar_equipo(self):
        """importa los datos de los equipos desde el archivo correspondiente
        los guarda en una lista
        """
        with open('equipos.csv', 'r') as arc_eqp:
            next(arc_eqp)
            for linea in arc_eqp:
                IdEquipo, NombreEquipo, golesafavor, golesencontra, puntos = linea.strip().split(';')
                instanciaE = Equipo(IdEquipo, NombreEquipo, int(golesafavor),int(golesencontra), int(puntos))
                self.__lista_equipos.append(instanciaE)
                
    
    def ordenar_equipos(self):
        """ordena la lista de equipos por puntaje, descendente
        """
        self.__lista_equipos = sorted(self.__lista_equipos, reverse=True)
    
    
    def mostrar_lista(self):
        return self.__lista_equipos
    
    
    def devolver_id_equipo(self, nombre_equipo):
        """busca el id de un equipo cuyo nombre es ingresado por teclado
        recibe nombre equipo str.
        devuelve id equipo int o false si no existe
        """
        id_equipo = False
        i = 0 
        # print(f'longitud de la lista de equipos = {len(self.__lista_equipos)}')
        # print(f'i vale {i}')
        while i < len(self.__lista_equipos) and not id_equipo:
            # print(f'i vale {i}')
            # print(self.__lista_equipos[i].get_nombre_equipo())
            
            if nombre_equipo == self.__lista_equipos[i].get_nombre_equipo():
                id_equipo = self.__lista_equipos[i].get_id_equipo()
            else:
                i += 1
        return id_equipo
    
    
    def actualizar_info_equipos(self, info_fechas):
        """actualiza puntae y goles de equipos según información 
        del archivo de fechas
        """
        # print('entré a actualizar la info')
        
        
        for equipo in info_fechas.get_lista_fechas():
            # print(f'el id del equipo es {equipo.get_id_equipoLocal()}')
            
            for team in self.__lista_equipos:
                registro = False
                # print(f'el id del equipo en la lista es {team.get_id_equipo()}')
                if int(equipo.get_id_equipoLocal()) == int(team.get_id_equipo()):
                    # print(f'el local {equipo.get_id_equipoLocal()} coincide con el equpo de la lista {team.get_id_equipo()}')
                    team.set_goles_a_favor(equipo.get_canGolLocal())
                    team.set_goles_en_contra(equipo.get_canGolVis())
                    team.set_dif_gol(equipo.get_canGolLocal() - equipo.get_canGolVis())
                    
                    if equipo.get_canGolLocal() > equipo.get_canGolVis():
                        puntos = 3
                    elif equipo.get_canGolLocal() == equipo.get_canGolVis():
                        puntos = 1
                    elif equipo.get_canGolLocal() < equipo.get_canGolVis():
                        puntos = 0
                    else:
                        print('No se que pasó, imposible calclar puntos')
                        
                    team.set_puntos(puntos)
                    registro = team
                    
                    # print(f'grabé registro, es local {registro}')
                
                
                elif int(equipo.get_id_equipoVisitante()) == int(team.get_id_equipo()):
                    # print(f'el Visitante {equipo.get_id_equipoVisitante()} coincide con el equpo de la lista {team.get_id_equipo()}')
                    team.set_goles_en_contra(equipo.get_canGolLocal())
                    team.set_goles_a_favor(equipo.get_canGolVis())
                    team.set_dif_gol(equipo.get_canGolVis() - equipo.get_canGolLocal())
                    
                    if equipo.get_canGolLocal() < equipo.get_canGolVis():
                        puntos = 3
                    elif equipo.get_canGolLocal() == equipo.get_canGolVis():
                        puntos = 1
                    elif equipo.get_canGolLocal() > equipo.get_canGolVis():
                        puntos = 0
                    else:
                        print('No se que pasó, imposible calclar puntos')
                        
                    team.set_puntos(puntos)
                    registro = team
                    # print(f'grabé registro, es visitante {registro}')
            # print(f'justo antes del if de regstro {registro}')
            # if registro:
            #     self.__lista_actualizada.append(registro)
                    
                    
    def guardar_datos_en_archivo(self):
        """crea un archivo con la info actualizada según última fecha
        """
        
        with open('archivo_actualizado.csv', 'w') as actualizado:
            actualizado.write('Id Equipo;Nombre Equipo;goles a favor;goles en contra;puntos\n')
            for linea in self.__lista_equipos:
                equipo = str(linea) + '\n'
                actualizado.write(equipo)
        
    
    def ordenar(self):
        self.__lista_equipos.sort(reverse=True)
        self.__lista_actualizada.sort(reverse=True)
        print('Lista de equipos')
        print('ID Equipo\tNombre Equipo\tgoles a favor\tgoles en contra\t  puntos')
        for equipo in self.__lista_equipos:
            print(f'{equipo.get_id_equipo()}\t\t{equipo.get_nombre_equipo():20}\t{equipo.get_goles_a_favor()}\t\t  {equipo.get_goles_en_contra()}\t   {equipo.get_puntos()}')
        
        # print('\nahora vamos a la lista actualizada\n')
        
        
        # for equipo in self.__lista_actualizada:
        #     print(f'{equipo.get_id_equipo()}\t{equipo.get_nombre_equipo():20}\t{equipo.get_goles_a_favor()}\t{equipo.get_goles_en_contra()}\t{equipo.get_puntos()}')
                