class Transaccion:
    __cvu: str
    __numTrans: str
    __importe: float
    __tipoTrans: str
    
    
    def __init__(self, cvu, numTrans, importe, tipoTrans) -> None:
        self.__cvu = cvu
        self.__numTrans = numTrans
        self.__importe = importe
        self.__tipoTrans = tipoTrans
        
    def __str__(self) -> str:
         return f"""
            CVU:{'_'*13} {self.__cvu}
            ID transaccion: {'_'*1} {self.__numTrans}
            Importe: {'_'*8} {self.__importe}
            Tipo: {'_'*11} {self.__tipoTrans}
        """
     
        
    def get_cvu(self):
        return self.__cvu
    
    
    def get_numTransaccion(self):
        return self.__numTrans
    
    
    def get_importe(self):
        return self.__importe
    
    
    def get_tipoTransaccion(self):
        return self.__tipoTrans
    
    