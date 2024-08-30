# excepciones.py
from tkinter import messagebox

class ErrorAplicacion(Exception):
    def __init__(self, nombre_campo=None):
        self.nombre_campo = nombre_campo
    def __str__(self):
        return "Manejo de errores de la Aplicación:"

class ErroresEntry(ErrorAplicacion):
    pass

class ErroresTipo(ErrorAplicacion):
    pass

class SoloLetrasNumerosSimbolos(ErrorAplicacion):
    def __init__(self, campo):
        super().__init__(f"El campo '{campo}' solo permite letras, números, y los símbolos #, -.")

class SoloNumerosSimboloMas(ErrorAplicacion):
    def __init__(self, campo):
        super().__init__(f"El campo '{campo}' solo permite números y el símbolo +.")

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

def validar_num(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio(nombre_campo)

        if ' ' in entry_text:
            raise SinEspacios(nombre_campo)

        if '.' in entry_text:
            raise NoUsarDecimales(nombre_campo)

        if any(c in "!@#$%^&*()_+=-{}[]|\:;<>,?/'\"" for c in entry_text):
            raise NoUsarSimbolos(nombre_campo)

        numero = int(entry_text)

        if numero < 0:
            raise NoUsarNegativos(nombre_campo)

        return True
    except ValueError:
        messagebox.showerror("Error", f"Manejo de errores de la Aplicación:\nEl dato en el campo '{nombre_campo}' debe ser un número.")
        return False
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False

def validar_string(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio(nombre_campo)

        if ' ' in entry_text:
            raise SinEspacios(nombre_campo)

        if not entry_text.isalpha():
            raise SoloLetras(nombre_campo)

        return True
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False

def validar_nombre(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio(nombre_campo)

        if not entry_text.isalpha():
            raise SoloLetras(nombre_campo)
        
        if any(c in "!@#$%^&*()_+=-{}[]|\:;<>,?/'\"" for c in entry_text):
            raise NoUsarSimbolos(nombre_campo)

        return True
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False

def validar_producto(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio(nombre_campo)
        
        if any(c in "!@#$%^&*()_+=-{}[]|\:;<>,?/'\"" for c in entry_text):
            raise NoUsarSimbolos(nombre_campo)

        return True
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False
    
def validar_dir(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio(nombre_campo)

        if not all(c.isalnum() or c in "#- " for c in entry_text):
            raise SoloLetrasNumerosSimbolos(nombre_campo)

        return True
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False

# Función para validar teléfono: números y símbolo +
def validar_tel(entry_text, nombre_campo):
    try:
        entry_text = entry_text.strip()
        if not entry_text:
            raise CampoVacio(nombre_campo)

        if not all(c.isdigit() or c == "+ " for c in entry_text):
            raise SoloNumerosSimboloMas(nombre_campo)

        return True
    except ErrorAplicacion as e:
        messagebox.showerror("Error", str(e))
        return False
