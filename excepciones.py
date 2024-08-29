# excepciones.py

class ErrorAplicacion(Exception):
    def __init__(self, nombre_campo=None):
        self.nombre_campo = nombre_campo
    def __str__(self):
        return "Manejo de errores de la Aplicación:"

class ErroresEntry(ErrorAplicacion):
    pass

class ErroresTipo(ErrorAplicacion):
    pass

class CampoVacio(ErroresEntry):
    def __str__(self):
        return f"{super().__str__()} CampoVacio: El campo '{self.nombre_campo}' no puede estar vacío."

class SinEspacios(ErroresEntry):
    def __str__(self):
        return f"{super().__str__()} SinEspacios: No se permiten espacios en blanco en el campo '{self.nombre_campo}'."

class SoloLetras(ErroresTipo):
    def __str__(self):
        return f"{super().__str__()} SoloLetras: Solo se permiten letras en el campo '{self.nombre_campo}'."

class SoloNumeros(ErroresTipo):
    def __str__(self):
        return f"{super().__str__()} SoloNumeros: Solo se permiten números en el campo '{self.nombre_campo}'."

class NoUsarSimbolos(ErroresTipo):
    def __str__(self):
        return f"{super().__str__()} NoUsarSimbolos: No se permiten símbolos en el campo '{self.nombre_campo}'."

class NoUsarDecimales(ErroresTipo):
    def __str__(self):
        return f"{super().__str__()} NoUsarDecimales: No se permiten decimales en el campo '{self.nombre_campo}'."

class NoUsarNegativos(ErroresTipo):
    def __str__(self):
        return f"{super().__str__()} NoUsarNegativos: No se permiten números negativos en el campo '{self.nombre_campo}'."

class NoExisteObjeto(ErroresEntry):
    def __init__(self, indice, max_indice):
        self.indice = indice
        self.max_indice = max_indice

    def __str__(self):
        return f"{super().__str__()} NoExisteObjeto: El valor '{self.indice}' no es válido. Ingrese un número entre 0 y {self.max_indice}."

class NoFormatoFecha(ErroresTipo):
    def __str__(self):
        return f"{super().__str__()} NoFormatoFecha: El formato de fecha no es válido en el campo '{self.nombre_campo}'. Utilice DD-MM-AAAA."
