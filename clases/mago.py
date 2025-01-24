class Mago:
    #Meto especial CONsRTUCTOR
    def __init__(self, nombre, hechizos=None):
        self.nombre = nombre
        self.hechizos = hechizos if hechizos else[]
    
    #Metodo Especial TO STRING ( se identifica con una caen aed caracteres la instancia)

    def __str__(self):
        return f"!Hola mi nombre es {self.nombre}, el mago"
    
    def __len__(self):
        return len(self.hechizos)
    
    def __eq__(self, otro):
        return self.nombre == otro.nombre and self.hechizos == otro.hechizos