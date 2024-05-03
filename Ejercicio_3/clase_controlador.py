import numpy as np

class Controlador:

    def __init__(self) -> None:
        self.__ventas = np.zeros([5,7], dtype=float)
        

    def cargar_datos_automatico(self):
        with open('ventas_farmacia.txt') as ventas:
            next(ventas)
            for linea in ventas:
                sucursal, dia, venta = linea.strip().split(',')
                sucursal = int(sucursal)
                dia = int(dia)
                venta = float(venta)
                self.__ventas[sucursal - 1][dia - 1] += venta
                
    
    def cargar_datos_manual(self, sucursal: int, dia: int, importe: float):
        
        self.__ventas[sucursal - 1][dia - 1] += importe
        
        
                       
    def calcular_vta_acum(self, sucursal):
        print(f'el total de la sucursal {sucursal} es $ {sum(self.__ventas[sucursal - 1]):,.2f}')
        
        
    def sucursal_mas_ventas_en_un_dia(self, dia):
        maximo = np.argmax(self.__ventas[:, dia - 1])
        ventas_dia = self.__ventas[maximo][dia - 1]
        print(f'La sucursal con más ventas en el día {dia} es {maximo + 1} con un total de $ {ventas_dia:,.2f}')
        
        
    def sucursal_menos_ventas_semana(self):
        suma_filas = np.sum(self.__ventas, axis=1) # suma todas las columnas de cada fila
        # print(suma_filas)
        indice_minimo = np.argmin(suma_filas)
        # print (indice_minimo)
        fila, columna = np.unravel_index(indice_minimo, self.__ventas.shape)
        # print(f'{fila} {columna}')
        fila1 = fila + 1
        columna1 = columna + 1
        print(f'La sucursal con menos ventas en la semana es la {columna1} con un total de ventas de $ {sum(self.__ventas[columna]):,.2f}')
        
        
        # fila, columna = np.unravel_index(np.argmin(self.__ventas), self.__ventas.shape)
        # sucursal = fila + 1  # Sumamos 1 porque las sucursales comienzan desde 1, no desde 0
        # dia = columna + 1  # Sumamos 1 porque los días comienzan desde 1, no desde 0
        # ventas = self.__ventas[fila, columna]
        # print(f'La sucursal con menos ventas en toda la semana es la {sucursal}, el día {dia}, con un total de $ {ventas:,.2f} ventas.')
        
        
    def total_facturacion_semanal(self):
        print(f'el total de la semana en curso es  $ {np.sum(self.__ventas):,.2f}') 
    
                
# instancia = Controlador()
# 
# instancia.cargar_datos()
# # suc = int(input('Ingrese el numero de sucursal: '))
# # instancia.calcular_vta_acum(suc)
# # instancia.sucursal_mas_ventas_en_un_dia(int(input('ingrese el dia de la semana: ')))
#                 
# instancia.sucursal_menos_ventas_semana()
# instancia.total_facturacion_semanal()
        
    
    