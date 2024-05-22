from datetime import datetime

from testEasyParking import Parqueadero
from testEasyParking import Tarifa

def ejecutar_prueba():
    print("--- SELECCIÓN DE PARQUEADERO ---")
    num_puestos = int(input("Ingrese el número de puestos (36, 64 o 100): "))
    while num_puestos not in [36, 64, 100]:
        print("Número de puestos inválido. Intente nuevamente.")
        num_puestos = int(input("Ingrese el número de puestos (36, 64 o 100): "))

    parqueadero = Parqueadero(num_puestos)

    while True:
        print(f"\n--- MENÚ PRINCIPAL (Parqueadero de {num_puestos} puestos) ---")
        print("1. Registrar ingreso")
        print("2. Consultar puesto")
        print("3. Registrar salida")
        print("4. Generar reportes")
        print("5. Zona más utilizada y ocupación total")
        print("6. Porcentajes de sexo, marcas y años")
        print("0. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del conductor: ")
            edad = int(input("Ingrese la edad del conductor: "))
            sexo = input("Ingrese el sexo del conductor (M/F): ").upper()
            marca = input("Ingrese la marca del vehículo: ")
            anio = int(input("Ingrese el año del vehículo: "))
            parqueadero.registrar_ingreso(nombre, edad, sexo, marca, anio)

        elif opcion == "2":
            puesto = input("Ingrese el puesto a consultar: ").upper()
            parqueadero.consultar_puesto(puesto)

        elif opcion == "3":
            puesto = input("Ingrese el puesto a registrar la salida: ").upper()
            parqueadero.registrar_salida(puesto)

        elif opcion == "4":
            parqueadero.generar_reportes()

        elif opcion == "5":
            parqueadero.zona_mas_utilizada()
            parqueadero.ocupacion_total()

        elif opcion == "6":
            parqueadero.porcentaje_sexo()
            parqueadero.porcentaje_marcas()
            parqueadero.porcentaje_anios()

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_prueba()