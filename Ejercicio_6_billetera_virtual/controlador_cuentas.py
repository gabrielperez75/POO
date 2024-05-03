import numpy as np
import csv
from clase_cuenta import *

class controladorCuenta:
    __arreglo_cuentas: np.array
    
    def __init__(self) -> None:
        self.__arreglo_cuentas = np.array([])
        
        
    def cargaArchivo(self):
        with open('cuentasBilletera.csv', 'r') as archivo:
            cuentas = csv.reader(archivo)
            # print(cuentas)
            for linea in cuentas:
                # print(linea)
                linea[4] = float(linea[4])
                cuenta = Cuenta(*linea)
                # print(cuenta)
                self.__arreglo_cuentas = np.append(self.__arreglo_cuentas, cuenta)
                
                
    def get_arreglo(self):
        return self.__arreglo_cuentas
    
    
    def validarDni(self, numero):
        i = 0
        encontrado = False
        while i < len(self.__arreglo_cuentas)and encontrado == False:
            print(f'i vale {i}')
            if numero == self.__arreglo_cuentas[i].get_dni():
                encontrado = numero
            else:
                i +=1
        print (encontrado)
        return encontrado
    
    def buscarDatosCliente(self, dni):
        print(f'entré a buscar cliente con el dni {dni}')
        encontrado = False
        i = 0
        while i < len(self.__arreglo_cuentas) and encontrado == False:
            if dni == self.__arreglo_cuentas[i].get_dni():
                encontrado = self.__arreglo_cuentas[i]
            else:
                i +=1
                
        return encontrado
    
    def buscarDatosPorCvu(self, cvu):
        encontrado = False
        i = 0
        while i < len(self.__arreglo_cuentas) and encontrado == False:
            if cvu == self.__arreglo_cuentas[i].get_cvu():
                encontrado = self.__arreglo_cuentas[i]
            else:
                i +=1
        return encontrado            
        
    
    def cambiarPorcentaje(self, porcentaje):
        
        Cuenta.set_rendimientoAnual(porcentaje) 
        
        
    def actualizarSaldos(self):
        for cuenta in self.__arreglo_cuentas:
            aumento = cuenta.get_saldo()*Cuenta.get_rendimientoAnual()/100
            cuenta.set_saldo(aumento)
              



# arregloCuentas = controladorCuenta()
# arregloCuentas.cargaArchivo()
