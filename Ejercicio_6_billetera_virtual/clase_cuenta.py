class Cuenta:
    __dni: str
    __apellido: str
    __nombre: str 
    __telefono: str
    __saldo: float
    __cvu: str
    __rendAnual = 68
    
    
    def __init__(self, dni, apellido, nombre, telefono, saldo: float, cvu) -> None:
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__telefono = telefono
        self.__saldo = saldo
        self.__cvu = cvu
        
    
    def __str__(self) -> str:
        return f"""
        DNI:{'_'*17} {self.__dni}
        Apellido y Nombre:{'_'*3} {self.__apellido} {self.__nombre}
        Saldo:{'_'*15} {self.__saldo}
        CVU: {'_'*16} {self.__cvu}    

    """

    def get_dni(self):
        return self.__dni
    
    
    def get_apellido(self):
        return self.__apellido
    
    
    def get_nombre(self):
        return self.__nombre
    
    
    def get_telefono(self):
        return self.__telefono
    
    
    def set_saldo(self, importe):
        self.__saldo += importe
        
    
    def get_saldo(self):
        return self.__saldo
    
    
    def get_cvu(self):
        return self.__cvu
    
    @classmethod
    def set_rendimientoAnual(cls, porcentaje):
        cls.__rendAnual = porcentaje
        
    @classmethod
    def get_rendimientoAnual(cls):
        return cls.__rendAnual
    