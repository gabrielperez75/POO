import numpy as np
from clases import *
import csv

class Manejador_motos():
    
    def __init__(self) -> None:
        self.__lista_motos = []
        
    
    def agregar_moto(self):
        
        with open('motos.csv', 'r') as motos:
            next(motos)
            for linea in motos:
                patente, marca, nombre, apellido, kilometraje = linea.strip().split(';')
                
                instancia = Moto(str(patente), str(marca), str(nombre), str(apellido), int(kilometraje))
                
                self.__lista_motos.append(instancia)
                # pnprint(f'El nombbre recien carado es la lista es: {nombre}')
            # for elemento in self.__lista_motos:
            #    print(elemento.get_nombre_conductor())
                
    
    def crear_set_patentes(self):
        set_patentes = set()
        for linea in self.__lista_motos:
            set_patentes.add(linea.get_patente())
            
        return set_patentes
    
    def validar_patente(self, patente, conjunto_patentes):
        encontrado = False
        if patente in conjunto_patentes:
            encontrado = patente
            
        return encontrado
    
    def obtener_conductor(self, patente):
        encontrado = False
        # print('entre a buscar la moto')
        i = 0
        conductor = None
        # print(f'el largo de la lista es: {len(self.__lista_motos)}')
        while i<= len(self.__lista_motos) and not encontrado:
        
            if self.__lista_motos[i].get_patente() == patente:
                encontrado = True
                nom_conductor = self.__lista_motos[i].get_nombre_conductor()
                ap_conductor = self.__lista_motos[i].get_apellido_conductor()
                conductor = nom_conductor +' '+ ap_conductor
            else:
                 i += 1
                 
        return conductor
            
    


class Manejador_pedidos:
    
    def __init__(self) -> None:
        self.__lista_pedidos = []
        
        
    def agregar_pedido(self):
        
        with open('pedidos.csv', 'r') as pedidos:
            
            next(pedidos)
            
            for linea in pedidos:
                patente, id_pedidodo, comidas, tiempo_estimado, tiempo_real, total = linea.strip().split(';')
                comidas = comidas.split(',')
                total = float(total)
                
                instancia = Pedido(str(patente), str(id_pedidodo), list(comidas), int(tiempo_estimado), float(total), int(tiempo_real))
                self.__lista_pedidos.append(instancia)
        return self.__lista_pedidos
    
    
    def agregar_pedido_manual(self, patente, id_pedido, comidas, tiempo_estimado, total, tiempo_real):
        instancia = Pedido(str(patente), str(id_pedido), list(comidas), int(tiempo_estimado), float(total), int(tiempo_real))
        self.__lista_pedidos.append(instancia)
        return self.__lista_pedidos
    
               
                
    def mostrar_pedidos_por_moto(self, patente_moto, instancia_m):
        coincidencias = []
        for linea in self.__lista_pedidos:
            if patente_moto == linea.get_patente_moto():
                coincidencias.append(linea)
                
        if coincidencias:
            print(f'Patente Moto: {coincidencias[0].get_patente_moto()}')
            print(f'Conductor: {instancia_m.obtener_conductor(patente_moto)}')
            
            print('\nId. de pedido\tTiempo estimado\t\tTiempo real\tPrecio\n')
            
            total = 0
            for pedido in coincidencias:
                print(f'{pedido.get_id_pedido()}\t\t\t{pedido.get_tiempo_estimado_entrega()}  \t\t{pedido.get_tiempo_real_entrega()}\t\t{(pedido.get_importe_total()):.2f}\n')
                total += pedido.get_importe_total()
                
            print(f'\nTotal:    $ {total:,.2f}')
            print(f'Comision: $ {(total*0.20):,.2f}')
    
    
    def modificar_tiempo_entrega(self, patente, pedido, tpo_real_entrega):
        i = 0
        encontrado = False
        # print('entré a modificar el tiempo')
        while i< len(self.__lista_pedidos) and not encontrado:
           # print('Ahora entrré al bucle a buscar patente u peddo')
            if self.__lista_pedidos[i].get_patente_moto() == patente and self.__lista_pedidos[i].get_id_pedido() == pedido:
                # print('ahora entro al if para cambiar el valor de la entrega')
                # print(self.__lista_pedidos[i].get_tiempo_real_entrega())
                self.__lista_pedidos[i].set_tiempo_real_entrega(tpo_real_entrega)
                #nprint(self.__lista_pedidos[i].get_tiempo_real_entrega())
                encontrado = True
                
                
            else:
                i +=1
                
                
    def calcular_prom_tpo_entrega(self, patente, instancia_p):
        sumatoria = []
        for registro in self.__lista_pedidos:
            if registro.get_patente_moto() == patente:
                sumatoria.append(registro.get_tiempo_real_entrega())
                
        return np.mean(sumatoria)
                
            

        
            
        
               
                
    
# instancia_m = Manejador_motos()
# instancia_p = Manejador_pedidos() 
# instancia_m.agregar_moto()
# lista_de_pedidos = instancia_p.agregar_pedido()
# 
# conjunto_motos = instancia_m.crear_set_patentes()
# 
# patente = input('Ingrese la patente a cargar: ')
# encontrado = instancia_m.validar_patente(patente, conjunto_motos)
# 
# if not encontrado:
#     print('La patente no existe')
# else:
#     
#     id_pedido = input('Ingrese el ID pedido: ')
#     comidas = [input('Ingrese las comidas, separadas por coma (,): ')]
#     tpo_estimado = int(input('ingrese el tiempo estimado de entrega:  '))
#     tpo_real = int(input('ingrese el tiempo real de entrega:  '))
#     importe = float(input('Ingrese el importe total del pedido: '))
#     instancia_p.agregar_pedido_manual(patente, id_pedido, comidas, tpo_estimado, importe, tpo_real)
#     
# instancia_p.mostrar_pedidos_por_moto('PKU452')
    

 
                


