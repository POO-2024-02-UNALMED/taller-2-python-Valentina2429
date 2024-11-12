class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if (color == "rojo" or color == "negro" or color=="verde" or color=="amrillo" or color == "blanco"):

            self.color = color

class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,motor,marca,registro):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.asientos = asientos
        Auto.cantidadCreados += 1

    def cantidadAsientos(self):

        num_asientos = 0

        for asiento in self.asientos:

            if asiento is not None:
                num_asientos += 1
                
        return num_asientos
    
    def verificarIntegridad(self):

        if self.registro == self.motor.registro:

            for asiento in self.asientos:

                if asiento is not None and asiento.registro != self.registro:

                    return "Las piezas no son originales"
                
            return"Auto original"
        else:
            return "Las piezas no son originales"
        
class Motor:
    def __init__(self, numero_cilindros, tipo, registro):
        
        self.numero_cilindros = numero_cilindros  
        self.tipo = tipo                          
        self.registro = registro                  

    def cambiarRegistro(self, registro):
        
        self.registro = registro

    def asignarTipo(self, tipo):
        
        if tipo == "gasolina" or tipo == "electrico":
            self.tipo = tipo








