import numpy as np

class Moto:
    __patente: str
    __marca: str
    __nombre_conductor: str
    __apellido_conductor: str
    __kilometraje: int
    
    def __init__(self, patente: str, marca: str, nombre: str, apellido: str, kilometraje: int) -> None:
        
        self.__patente = patente
        self.__marca = marca
        self.__nombre_conductor = nombre
        self.__apellido_conductor = apellido
        self.__kilometraje = kilometraje
        
        
    def set_patente(self, patente):
        self.__patente = patente
        
        
    def get_patente(self):
        return self.__patente
    
    
    def set_marca(self, marca):
        self.__marca = marca
        
        
    def get_marca(self):
        return self.__marca
    
    
    def set_nombre_conductor(self, nombre: str):
        self.__nombre_conductor = nombre
        
        
    def get_nombre_conductor(self):
        return self.__nombre_conductor
    
    
    def set_apellido_conductor(self, apellido: str):
        self.__apellido_conductor = apellido
        
        
    def get_apellido_conductor(self):
        return self.__apellido_conductor
    
    
    def set_kilometraje(self, kilometraje):
        self.__apellido_conductor = kilometraje
        
        
    def get_kilometraje(self):
        return self.__kilometraje
     
      
    
class Pedido:
    __patente_moto: str
    __id_pedido: str
    __comidas: list
    __tiempo_estimado_entrega: int
    __tiempo_real_entrega: int
    __importe_total_pedido: float
    
    
    def __init__(self, patente: str, id_pedidodo: str, comidas: str, tiempo_estimado: int, total, tiempo_real = 0) -> None:
        self.__patente_moto = patente
        self.__id_pedido = id_pedidodo
        self.__comidas = comidas
        self.__tiempo_estimado_entrega =tiempo_estimado
        self.__tiempo_real_entrega = tiempo_real
        self.__importe_total_pedido = total
        
    
    # def __str__(self):
    #     return f'ID Pedido {self.__id_pedido}'
    
    
    def __str__(self):
        return ", ".join(str(comida) for comida in self.__comidas)
    
    
    def set_tiempo_real_entrega(self, tiempo):
        self.__tiempo_real_entrega = tiempo
        
        
    def __lt__(self, otra_patente):
        return self.__get_patente_moto() < otra_patente.get_patente_moto()
    
            
    def get_tiempo_real_entrega(self):
        return(self.__tiempo_real_entrega)
    
    
    def set_patente_moto(self, patente):
        self.__patente_moto = patente
        
    
    def get_patente_moto(self):
        return self.__patente_moto
    
    
    def set_comidas(self, comida):
        self.__comidas.append(comida)
        
    
    def get_comidas(self):
        return self.__comidas
    
    def set_id_pedido(self, idpedido):
        self.__id_pedido = idpedido
        
        
    def get_id_pedido(self):
        return self.__id_pedido
    
    
    def set_tiempo_estimado_entrega(self, tiempo):
        self.tiempo_estimado_entrega = tiempo
        
    
    def get_tiempo_estimado_entrega(self):
        return self.__tiempo_estimado_entrega
    
    
    def set_importe_total(self, importe: float):
        self.__importe_total_pedido = importe
        
        
    def get_importe_total(self):
        return self.__importe_total_pedido
    
    
        
        
        