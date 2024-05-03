from datetime import datetime, date

class Fecha_futbol:
    """se define la clase Fecha_futbol con sus atribitos y el tipo de dato de c/u de ellos
    """
    __id_equipoLocal: int
    __id_equipoVisitante: int
    __canGolLocal: int
    __canGolVis: int
    __fecha_partido: date
    
    
    def __init__(self, idLocal, idVisit, golLocal, golVis, fecha) -> None:
        self.__id_equipoLocal = idLocal
        self.__id_equipoVisitante = idVisit
        self.__canGolLocal = golLocal
        self.__canGolVis = golVis
        self.__fecha_partido = fecha
        
        
    def set_id_equipoLocal(self, id):
        self.__id_equipoLocal = id
        
        
    def get_id_equipoLocal(self):
        return self.__id_equipoLocal
    
        
    def set_id_equipoVisitante(self, id):
        self.__id_equipoVisitante = id
        
        
    def get_id_equipoVisitante(self):
        return self.__id_equipoVisitante
    
    
    def set_canGolLocal(self, goles):
        self.__canGolLocal = goles
        
        
    def get_canGolLocal(self):
        return self.__canGolLocal
    
    
    def set_canGolVis(self, goles):
        self.__canGolVis = goles
        
        
    def get_canGolVis(self):
        return self.__canGolVis
    
    
    def set_fecha(self, fecha):
        self.__fecha_partido = fecha
        
    
    def get_fecha_partido(self):
        return self.__fecha_partido