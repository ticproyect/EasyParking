from datetime import datetime
class Usuario:
    def __init__(self, nombre:str, año_de_nacimiento: int, mes_de_nacimiento: int, dia_de_nacimiento: int, sexo:str ):
        self.nombre = nombre
        self.año_de_nacimiendo = año_de_nacimiento
        self.mes_de_nacimiento = mes_de_nacimiento
        self.dia_de_nacimiento = dia_de_nacimiento
        self.sexo = sexo
        
    
    def Calcular_edad(self):
        año_actual = datetime.now().year
        mes_actual = datetime.now().month
        dia_actual = datetime.now().day
        edad_años = self.año_de_nacimiendo - año_actual
        if mes_actual < self.mes_de_nacimiento or (mes_actual == self.mes_de_nacimiento and dia_actual < self.dia_de_nacimiento):
            edad_años -= 1
            return edad_años
        