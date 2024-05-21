from datetime import datetime
from clase usuario import clase usuario
from clase vehiculo import clase vehiculo
class Parqueadero:
    def __init__(self, nombre:str, filas:int, columnas: int) -> None:
        if filas == columnas:
            if filas in (6, 8, 10):
                self.nombre = nombre
                self.filas = filas
                self.columnas = columnas
                self.puestos = [[None for _ in range (self.columnas)] for _ in range (self.filas)]
                letras_alfabeto = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z')
                self.letras_filas = letras_alfabeto[:self.filas]
                self.precio = None
                if filas == 6:
                    self.precio = {
                        "bajo": 6000,
                        "medio": 8000,
                        "alto": 10000
                    }
                elif filas == 8:
                    self.precio = {
                        "bajo": 8000,
                        "medio": 16000,
                        "alto": 24000,
                        "muy alto": 32000
                    }
                elif filas == 10:
                    self.precio = {
                        "muy bajo": 10000 ,
                        "bajo": 20000,
                        "medio": 30000,
                        "alto": 40000,
                        "muy alto": 50000
                    }       
            else:
                ValueError("Ingrese un valor dentro del rango")
        else:
            ValueError("Dimensiones no existentes en los parqueaderos")
    
    def asignar_puesto(self, preferencia:str):
        pass

    def consultar_puesto(self):
        pass

    def monto_pagar(self):
        pass

    def liberar_puesto(self, letra_fila: str, numero_columna: int):
        pass

    def reporte_general(self):
        pass
    
    def porcentaje_ocupacion(self):
        pass
    
    def porcentaje_sexo(self):
        pass
    
    def porcentaje_marca_año(self):
        pass
    
