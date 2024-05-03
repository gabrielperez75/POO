from clase_fecha import *
import csv
from datetime import date

class ManejadorFecha:
    __lista_fechas: list
    
    def __init__(self) -> None:
        
        self.__lista_fechas = []
   
        
    def cargarFechas(self):
        
        try:
            with open('fechasFutbol.csv', 'r') as archivo:
                next(archivo)
                for fila in archivo:
                    idLocal, idVisitante, golLocal, golVisitante, fecha = fila.strip().split(';')
                    fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
                    instanciaF = Fecha_futbol(int(idLocal), int(idVisitante), int(golLocal), int(golVisitante), fecha)
                    self.__lista_fechas.append(instanciaF)
            
        except FileExistsError:
            print('archivo no encontrado')
    
            
    def get_lista_fechas(self):
        return self.__lista_fechas
    
    
    def mostrar_info(self, nombre, idEquipo):
        totgolfav = 0
        totgolcont = 0
        totptos = 0
        print(f'Equipo: {nombre}')
        print(f'Fecha\t\tGoles a Favor\tGoles en Contra\t\tDiferencia de Goles\tPuntos')
        for equipo in self.__lista_fechas:
            # print('éntré al for')
            # print(f'el id del equipo iterando es {type(equipo.get_id_equipoLocal())} y el ingresado es {type(idEquipo)}')
            if equipo.get_id_equipoLocal() == idEquipo:
                
                if equipo.get_canGolVis() > equipo.get_canGolLocal():
                    puntos = 0
                elif equipo.get_canGolVis() < equipo.get_canGolLocal():
                    puntos = 3
                else:
                    puntos = 1
                print(f'{(equipo.get_fecha_partido()).strftime("%d/%m/%Y")}\t\t{equipo.get_canGolLocal()}\t\t{equipo.get_canGolVis()}\t\t\t{equipo.get_canGolLocal()-equipo.get_canGolVis()}\t\t {puntos}')
                totgolfav += equipo.get_canGolLocal()
                totgolcont += equipo.get_canGolVis()
                totptos += puntos
            
            elif equipo.get_id_equipoVisitante() == idEquipo:
                
                if equipo.get_canGolVis() > equipo.get_canGolLocal():
                    puntos = 3
                elif equipo.get_canGolVis() < equipo.get_canGolLocal():
                    puntos = 0
                else:
                    puntos = 1
                    
                totgolfav += equipo.get_canGolVis()
                totgolcont += equipo.get_canGolLocal()
                totptos += puntos
                print(f'{(equipo.get_fecha_partido()).strftime("%d/%m/%Y")}\t\t{equipo.get_canGolVis()}\t\t{equipo.get_canGolLocal()}\t\t\t{equipo.get_canGolVis()-equipo.get_canGolLocal()}\t\t {puntos}')
            
        print('------------------------------------------------------------------------------------')
        print(f'Totales: \t\t{totgolfav}\t\t{totgolcont}\t\t\t{totgolfav-totgolcont}\t\t {totptos}')
    
        