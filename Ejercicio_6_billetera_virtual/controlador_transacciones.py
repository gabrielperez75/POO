import csv
from clase_transaccion import *
from controlador_cuentas import *

class ControladorTransaccion:
    __listaTransacciones: list 
    
    def __init__(self) -> None:
        self.__listaTransacciones = []
        
    
    def cargarTransaccion(self):
        with open('transaccionesBilletera.csv', 'r') as archivo:
            transacciones = csv.reader(archivo)
            next(archivo)
            for linea in transacciones:
                linea = Transaccion(*linea)
                self.__listaTransacciones.append(linea)
     
                
    def get_listaTransacciones(self):
        return self.__listaTransacciones
    
    
    def buscarDatosPorCvu(self, cvu, controlador):
        encontrado = False
        i = 0
        while encontrado == False and i < len(self.__listaTransacciones):
            if cvu == self.__listaTransacciones[i].get_cvu():
                            
                encontrado = controlador.buscarDatosPorCvu(cvu)
            else:
                i += 1
        return encontrado
    
    def actualizarDatos(self, controlador):
        arreglo = controlador.get_arreglo()
        # print(arreglo)
        for transaccion in self.__listaTransacciones:
            # print(transaccion)
            for cuenta in arreglo:
                # print(f'Parece que las cvu coinciden {transaccion.get_cvu()} {cuenta.get_cvu()}')
                # print(cuenta)
                if str(transaccion.get_cvu()) == str(cuenta.get_cvu()):
                    # print(f'Parece que las cvu coinciden {transaccion.get_cvu()} {cuenta.get_cvu()}')
                    importe = float(transaccion.get_importe())
                    # print(type(importe))
                    if transaccion.get_tipoTransaccion() == 'D':
                        importe = importe*(-1)
                    
                    cuenta.set_saldo(importe)
            
    
    


# transacciones = ControladorTransaccion()
# transacciones.cargarTransaccion()
# for t in transacciones.get_listaTransacciones():
#     print(t)