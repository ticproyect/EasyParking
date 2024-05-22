from collections import defaultdict
from datetime import datetime

class Parqueadero:
    def __init__(self, num_puestos):
        self.num_puestos = num_puestos
        self.dimensiones = self.calcular_dimensiones()
        self.puestos = self.generar_puestos()
        self.costos = self.establecer_costos()
        self.ocupados = {}
        self.registro = []
        self.ingresos = 0

    def calcular_dimensiones(self):
        if self.num_puestos == 36:
            return (6, 6)
        elif self.num_puestos == 64:
            return (8, 8)
        else:
            return (10, 10)

    def generar_puestos(self):
        puestos = {}
        filas = 'ABCDEFGHIJ'[:self.dimensiones[0]]
        for fila in filas:
            for col in range(1, self.dimensiones[1] + 1):
                puesto = f'{fila}{col}'
                puestos[puesto] = {'ocupado': False}
        return puestos

    def establecer_costos(self):
        costos = {}
        for puesto in self.puestos:
            fila = ord(puesto[0]) - ord('A')
            if self.num_puestos == 36:
                costo = 2000 + (fila * 500)
            elif self.num_puestos == 64:
                costo = 3000 + (fila * 500)
            else:
                costo = 5000 + (fila * 500)
            costos[puesto] = costo
        return costos

    def registrar_ingreso(self, nombre, edad, sexo, marca, anio):
        if edad < 18 or (datetime.now().year - anio) > 10:
            print("No se admiten conductores menores de edad o vehículos con más de 10 años de antigüedad.")
            return

        preferencias = self.solicitar_preferencias()
        puesto = self.asignar_puesto(preferencias)
        if puesto:
            self.ocupados[puesto] = {'nombre': nombre, 'edad': edad, 'sexo': sexo, 'marca': marca, 'anio': anio, 'ingreso': datetime.now()}
            self.registro.append({'puesto': puesto, 'nombre': nombre, 'edad': edad, 'sexo': sexo, 'marca': marca, 'anio': anio, 'ingreso': datetime.now()})
            print(f"Se asignó el puesto {puesto} al vehículo de {nombre}.")
        else:
            print("No hay puestos disponibles en este momento.")

    def solicitar_preferencias(self):
        fila_preferida = input("Ingrese la fila preferida (A-J) o 'N' si no tiene preferencia: ").upper()
        cerca_entrada = input("¿Desea un puesto cerca de la entrada? (S/N): ").upper() == 'S'
        return fila_preferida, cerca_entrada

    def asignar_puesto(self, preferencias):
        fila_preferida, cerca_entrada = preferencias
        puestos_disponibles = [puesto for puesto, data in self.puestos.items() if not data['ocupado']]
        if fila_preferida != 'N':
            puestos_fila = [puesto for puesto in puestos_disponibles if puesto.startswith(fila_preferida)]
            if puestos_fila:
                puestos_disponibles = puestos_fila
        if cerca_entrada:
            puestos_disponibles.sort(key=lambda puesto: (ord(puesto[0]), int(puesto[1:])))
        else:
            puestos_disponibles.sort(key=lambda puesto: (ord(puesto[0]), int(puesto[1:])), reverse=True)
        if puestos_disponibles:
            puesto = puestos_disponibles[0]
            self.puestos[puesto]['ocupado'] = True
            return puesto
        return None

    def consultar_puesto(self, puesto):
        if puesto in self.ocupados:
            data = self.ocupados[puesto]
            print(f"El puesto {puesto} está ocupado por el vehículo de {data['nombre']} desde {data['ingreso'].strftime('%H:%M')}")
        else:
            print(f"El puesto {puesto} está disponible.")

    def registrar_salida(self, puesto):
        if puesto in self.ocupados:
            data = self.ocupados.pop(puesto)
            ingreso = data['ingreso']
            salida = datetime.now()
            tiempo = salida - ingreso
            horas = tiempo.seconds // 3600
            minutos = (tiempo.seconds % 3600) // 60
            total_horas = horas + (minutos > 0)
            costo = self.costos[puesto] * total_horas
            self.ingresos += costo
            self.puestos[puesto]['ocupado'] = False
            print(f"El costo por el puesto {puesto} es: ${costo:,}")
        else:
            print(f"El puesto {puesto} no está ocupado.")

    def generar_reportes(self):
        print(f"Dinero recaudado: ${self.ingresos:,}")
        print(f"Vehículos ingresados: {len(self.registro)}")
        print(f"Puestos utilizados: {len(self.ocupados)}")

    def zona_mas_utilizada(self):
        ocupacion_filas = defaultdict(int)
        ocupacion_columnas = defaultdict(int)
        for puesto in self.ocupados:
            fila, columna = puesto[0], int(puesto[1:])
            ocupacion_filas[fila] += 1
            ocupacion_columnas[columna] += 1
        max_fila = max(ocupacion_filas.items(), key=lambda x: x[1])
        max_columna = max(ocupacion_columnas.items(), key=lambda x: x[1])
        print(f"La fila más utilizada es: {max_fila[0]} con {max_fila[1]} puestos ocupados.")
        print(f"La columna más utilizada es: {max_columna[0]} con {max_columna[1]} puestos ocupados.")

    def ocupacion_total(self):
        ocupados = len(self.ocupados)
        total_puestos = self.num_puestos
        porcentaje = (ocupados / total_puestos) * 100
        print(f"La ocupación total del parqueadero es: {porcentaje:.2f}%")

    def porcentaje_sexo(self):
        hombres = sum(1 for data in self.ocupados.values() if data['sexo'] == 'M')
        mujeres = sum(1 for data in self.ocupados.values() if data['sexo'] == 'F')
        total = hombres + mujeres
        porc_hombres = (hombres / total) * 100 if total > 0 else 0
        porc_mujeres = (mujeres / total) * 100 if total > 0 else 0
        print(f"Porcentaje de hombres: {porc_hombres:.2f}%")
        print(f"Porcentaje de mujeres: {porc_mujeres:.2f}%")

    def porcentaje_marcas(self):
        marcas = defaultdict(int)
        for data in self.ocupados.values():
            marcas[data['marca']] += 1
        total = sum(marcas.values())
        for marca, cantidad in marcas.items():
            porcentaje = (cantidad / total) * 100
            print(f"Porcentaje de vehículos {marca}: {porcentaje:.2f}%")

    def porcentaje_anios(self):
        anios = defaultdict(int)
        for data in self.ocupados.values():
            anios[data['anio']] += 1
        total = sum(anios.values())
        for anio, cantidad in anios.items():
            porcentaje = (cantidad / total) * 100
            print(f"Porcentaje de vehículos del año {anio}: {porcentaje:.2f}%")

# Ejemplo de uso
parqueadero = Parqueadero(100)  # Crea un parqueadero de 100 puestos

# Registro de ingresos
parqueadero.registrar_ingreso("Juan Pérez", 30, "M", "Chevrolet", 2018)
parqueadero.registrar_ingreso("María Rodríguez", 25, "F", "Toyota", 2020)
parqueadero.registrar_ingreso("Pedro Gómez", 40, "M", "Ford", 2015)

# Consulta de puesto
parqueadero.consultar_puesto("A1")

# Registro de salida
parqueadero.registrar_salida("A1")

# Generación de reportes
parqueadero.generar_reportes()

# Zona más utilizada y ocupación total
parqueadero.zona_mas_utilizada()
parqueadero.ocupacion_total()

# Porcentajes de sexo, marcas y años
parqueadero.porcentaje_sexo()
parqueadero.porcentaje_marcas()
parqueadero.porcentaje_anios()