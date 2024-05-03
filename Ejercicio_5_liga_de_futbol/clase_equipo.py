class Equipo:
    """se define la clase equipo con sus atribitos y el tipo de dato de c/u de ellos
    """
    __id_equipo: str
    __nombre_equipo: str
    __goles_a_favor: int
    __goles_en_contra: int
    __dif_gol: int
    __puntos: int
    
    def __init__(self, idEquipo, nombreequipo, golesafavor: int, golesencontra: int, puntos = 0) -> None:
        # inicializador de cada instancia de la clase equipo
        self.__id_equipo = idEquipo
        self.__nombre_equipo = nombreequipo
        self.__goles_a_favor = golesafavor
        self.__goles_en_contra = golesencontra
        self.__dif_gol = golesafavor - golesencontra
        self.__puntos = puntos
        
        
    def set_id_equipo(self, id):
        self.__id_equipo = id
        
    
    def get_id_equipo(self):
        return self.__id_equipo
    
    
    def set_nombre_equipo(self, nombre):
        self.__nombre_equipo = nombre
        
        
    def get_nombre_equipo(self):
        return self.__nombre_equipo
    
    
    def set_goles_a_favor(self, golesF):
        self.__goles_a_favor += golesF
        
        
    def get_goles_a_favor(self):
        return self.__goles_a_favor
    
    
    def set_goles_en_contra(self, golesC):
        self.__goles_en_contra += golesC
        
        
    def get_goles_en_contra(self):
        return self.__goles_en_contra
    
    
    def set_dif_gol(self, difGol):
        self.__dif_gol += difGol
        
        
    def get_dif_gol(self):
        return self.__dif_gol
    
    
    def set_puntos(self, puntos):
        self.__puntos += puntos
        
        
    def get_puntos(self):
        return self.__puntos
 
 
    def __gt__(self, otro_equipo):
        """sobrecarga el operador de comparación > para trabajar con el tipo de dato Equipo
        """
        resultado = False
        if self.__puntos > otro_equipo.get_puntos():
            resultado = True
        elif self.__puntos == otro_equipo.get_puntos():
            if self.__dif_gol > otro_equipo.get_dif_gol():
                resultado = True
            
            elif self.__dif_gol == otro_equipo.get_dif_gol():
                if self.__goles_a_favor > otro_equipo.get_goles_a_favor():
                    resultado = True
            # elif self.__goles_a_favor == otro_equipo.get_goles_a_favor() and self.__dif_gol == otro_equipo.get_dif_gol():
            #     if self.get_goles_en_contra < otro_equipo.get_dif_gol():
            #         resultado = True
                    
        return resultado

    def __str__(self) -> str:
        # defino el string, sirve para guardar la info en el archivo
        return f'{self.__id_equipo};{self.__nombre_equipo};{self.__goles_a_favor};{self.__goles_en_contra};{self.__puntos}'   