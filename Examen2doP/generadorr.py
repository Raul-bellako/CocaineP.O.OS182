import random

class Estudiante:
    def __init__(self, nombre, apellido_paterno, apellido_materno, anio_nacimiento, carrera):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.anio_nacimiento = anio_nacimiento
        self.carrera = carrera

    def generar_matri(self):
        añooo_actual = str(2023)[-2:]
        anio_nacimiento = str(self.anio_nacimiento)[-2:]
        primera_letra_nombre = self.nombre[0]
        primera_letra_apellido_paterno = self.apellido_paterno[0]
        primera_letra_apellido_materno = self.apellido_materno[0]
        digitos_aleatorios = str(random.randint(100, 999))
        primeras_tres_letras_carrera = self.carrera[:3].upper()

        matricula = añooo_actual + anio_nacimiento + primera_letra_nombre + \
                    primera_letra_apellido_paterno + primera_letra_apellido_materno + \
                    digitos_aleatorios + primeras_tres_letras_carrera

        return matricula
