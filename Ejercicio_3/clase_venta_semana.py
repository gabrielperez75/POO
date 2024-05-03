class VtaSemana:
    __vtaLunes: float
    __vtaMartes: float
    __vtaMiercoles: float
    __vtaJueves: float
    __vtaViernes: float
    __vtaSabado: float
    __vtaDomingo: float
    
    def __init__(self, lunes: float, martes: float, miercoles: float, jueves: float, viernes: float, sabado: float, domingo: float) -> None:
        self.__vtaLunes = lunes
        self.__vtaMartes = martes
        self.__vtaMartes = miercoles
        self.__vtaJueves = jueves
        self.__vtaViernes = viernes
        self.__vtaSabado = sabado
        self.__vtaDomingo = domingo
        
    def get_lunes(self):
        return self.__vtaLunes
        
    def get_martes(self):
        return self.__vtaMartes
    
    def get_miercoles(self):
        return self.__vtaMiercoles
    
    
    def get_jueves(self):
        return self.__vtaJueves
    
    def get_viernes(self):
        return self.__vtaViernes
    
    
    def get_sabado(self):
        return self.__vtaSabado
    
    
    def get_domingo(self):
        return self.__vtaDomingo
    
    
    
    
    
    
    
    
        
    