from datetime import datetime

# Obtener la entrada del usuario como una cadena
fecha_str = input("Ingrese la fecha (en formato DD/MM/YYYY): ")

# Convertir la cadena a un objeto datetime
try:
    fecha = datetime.strptime(fecha_str, "%d/%m/%Y").date()
    print("Fecha ingresada:", fecha.strftime("%d/%m/%Y"))
except ValueError:
    print("Formato de fecha incorrecto. Por favor, ingrese la fecha en formato DD/MM/YYYY.")
