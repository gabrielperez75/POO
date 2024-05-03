from clase import *

def menu():
    print("""
          Ingrese la Opción deseda:
          
          1_ Ejecutar Test
          2_ Depositar
          3_ Extraer
          4_ Buscar Nmbre
          0_ Salir
          
          """)
def validar_opcion():
    """
    valida que la opcion del menu ingresada por el usuario sea correcta
    """
    opciones_validas = ['0', '1', '2', '3', '4']
    opcion = input('ingrese la opción deseada: ')
    while opcion not in opciones_validas:
        print('Opción incorrecta')
        menu()
        opcion = input('ingrese la opción deseada: ')
    return opcion


def validar_cuil(cuil):
    
    try:
        
    
        correcto = False
        
        while not correcto:
            if len(cuil) != 11:
                cuil = input('La cantidad de digitos es incorrecta, intente Nuevamente: ')
                continue
        
            cuil_n = [int(digit) for digit in cuil]
        
            cuil_n[0]  = int(cuil[0])
            cuil_n[1]  = int(cuil[1])
            cuil_n[2]  = int(cuil[2])
            cuil_n[3]  = int(cuil[3])
            cuil_n[4]  = int(cuil[4])
            cuil_n[5]  = int(cuil[5])
            cuil_n[6]  = int(cuil[6])
            cuil_n[7]  = int(cuil[7])
            cuil_n[8]  = int(cuil[8])
            cuil_n[9]  = int(cuil[9])
            cuil_n[10]  = int(cuil[10])
        
            suma = sum([(cuil_n[0] * 5) + 
                       (cuil_n[1] * 4) +
                       (cuil_n[2] * 3) +
                       (cuil_n[3] * 2) +
                       (cuil_n[4] * 7) +
                       (cuil_n[5] * 6) +
                       (cuil_n[6] * 5) +
                       (cuil_n[7] * 4) +
                       (cuil_n[8] * 3) + 
                       (cuil_n[9] * 2)]
                       )
            resto = suma % 11
        
            if resto == 0 and cuil_n[10] == 0:
                correcto = True
            elif resto == 1 and cuil_n[0] == 2 and cuil[1] == 3:
                if cuil_n[10] == 9:
                    correcto = True
                elif cuil_n[10] == 4:
                    correcto = True
                else:
                    print('Cuit erroneo')
                    cuil = input('Ingrese nuevamente el CUIL: ')
            elif (11 - resto) == cuil_n[10]:
                    correcto = True
            else:
                 print('Cuit erroneo')
                 cuil = input('Ingrese nuevamente el CUIL: ')
                 
    except ValueError:
        print('la cantidad de digitos es incorrecta.')
                 
    return cuil
    
  
    
def pedir_datos_para_operar():
    """se usa para no tener que escribir los input a cada rato"""
    cuil_p = input('ingrese numero de cuil: ')
    cuil = validar_cuil(cuil_p)
    
    monto = float(input('ingrese importe: '))
    return cuil, monto
    
    
def buscar_dato_de_cuenta(cuil, listado_cajas):
    """Busca el cuil ingresado por el usuario en el listado 
    devuelve la instancia completa si hay coincidencia
    devuelve cero si no hay coincidencia
    """
    encontrado = False
    datos_caja = 0
    i = 0
    while i < len(listado_cajas) and not encontrado:
        if cuil == listado_cajas[i].get_cuil():
            datos_caja = listado_cajas[i]
            encontrado = True
        i += 1
    return datos_caja
    
    
    
def verificar_saldo(importe, datos_de_cuenta):
    
    """
    valida que el saldo de la cuenta sea suficiente para retirar los fondos solicitados
    """
    if importe > datos_de_cuenta:
        importe = -1
    return importe


def grabar_extraccion(importe, datos_de_cuenta):
    """actualiza el saldo de la cuenta que está operando """
    # print(f'Estoy en extraer saldo, la cuenta es de {datos_de_cuenta.get_nombre()} y el saldo es {datos_de_cuenta.get_saldo()} y el importe a extraer es de {importe}')
    datos_de_cuenta.set_saldo(datos_de_cuenta.get_saldo()-importe)
    # print(f'Estoy en extraer saldo, despues de la extraccion la cuenta es de {datos_de_cuenta.get_nombre()} y el saldo es {datos_de_cuenta.get_saldo()}')
        

def depositar(monto):
    """
    valida que el monto ingresado para depósito sea positivo
    """
    if monto <= 0:
        estado = 0
    else:
        estado = 1
    return estado
    
    
def grabar_deposito(monto_deposito, datos_de_cuenta):
    """
    actualiza el saldo de la cuenta que está depositando
    """
    datos_de_cuenta.set_saldo(datos_de_cuenta.get_saldo() + monto_deposito)
    
    
def test_cuenta():
    """
    sirve para testear el init de la clase
    si se quiere usar ingreso manual, se debe descomentar y luego comentar las instancias predeterminadas
    """
    lista_cajas = []
    """
    for i in range(1,3):
        
        cuenta = str(input('Ingrese numero de cuenta: '))
        cuil = validar_cuil(str(input('Ingrese numero de cuil: ')))
        apellido = str(input('Ingrese apellido: '))
        nombre = str(input('Ingrese nombre: '))
        opcion = input('Desea ingresar saldo en la cuenta s/n: ')
        if opcion == 's':
            saldo = float(input('Ingrese saldo de la cuenta: '))
            una_caja = CajaDeAhorro(cuenta, cuil, apellido, nombre, saldo)
            lista_cajas.append(una_caja)
            # caja = CajaDeAhorro(cuenta, cuil, apellido, nombre, saldo)
            
        else:
            una_caja = CajaDeAhorro(cuenta, cuil, apellido, nombre, 0)
            lista_cajas.append(una_caja)
    
    return lista_cajas
    """
        
    
    lista_cajas.append(CajaDeAhorro("6800", "20249487180", "Perez", "Gabriel", 10000))
    
    lista_cajas.append(CajaDeAhorro("6801", "27248366554", "Perez", "Noelia", 20000))
    
    lista_cajas.append(CajaDeAhorro("6802", "23480148333", "Perez", "Sebastian", 30000))
    
    return lista_cajas

    
        
        
        