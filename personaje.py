class Personaje:
    #atributos
    especie="Humanos"
    nombre="MasterChief"
    altura=2.70
    
    #Metodos
    
    def correr(self, status):
        if (status):
            print ("El personaje " + self.nombre + "Esta corriendo")
        else :
            print ("El personaje " + self.nombre + "Se detuvo")