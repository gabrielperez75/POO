class CajaDeAhorro:
    __nroCuenta: str
    __cuil: str
    __apellido:str
    __nombre: str
    __saldo: float
    
    
    def __init__(self, cuenta, cuil, apellido, nombre, saldo) -> None:
        self.__nroCuenta = cuenta
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__saldo = saldo
        
    def set_saldo(self, importe):
        self.__saldo = importe
        
    def get_saldo(self):
        return self.__saldo
    
    
    def get_nroCuenta(self):
        return self.__nroCuenta
    
    def get_cuil(self):
        return self.__cuil
    
    def get_apellido(self):
        return self.__apellido
    
    
    def get_nombre(self):
        return self.__nombre
    
    
    def __str__(self) -> str:
        # return f'cuenta: {self.__nroCuenta} cuil: {self.__cuil}, apellido: {self.__apellido} nombre: {self.__nombre} saldo: {self.__saldo}'
        return f"""
                Cuenta: {self.__nroCuenta} 
                Cuil: {self.__cuil} 
                Apellido: {self.__apellido} 
                Nombre: {self.__nombre} 
                Saldo: {self.__saldo}"""
    
    