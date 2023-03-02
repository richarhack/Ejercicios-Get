class Persona:
    def __init__(self):
        self.__edad = 0
        self.__nombre = ''
        self.__telefono = ''
    
    def get_edad(self):
        return self.__edad
    
    def set_edad(self, edad):
        self.__edad = edad
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_telefono(self):
        return self.__telefono
    
    def set_telefono(self, telefono):
        self.__telefono = telefono

# Crear objeto persona
mi_persona = Persona()

# Pedir al usuario que ingrese los valores de las propiedades
mi_persona.set_edad(int(input("Ingresa la edad de la persona: ")))
mi_persona.set_nombre(input("Ingresa el nombre de la persona: "))
mi_persona.set_telefono(input("Ingresa el teléfono de la persona: "))

# Mostrar los valores de las propiedades
print("La edad de la persona es:", mi_persona.get_edad())
print("El nombre de la persona es:", mi_persona.get_nombre())
print("El teléfono de la persona es:", mi_persona.get_telefono())