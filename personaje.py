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
    
    def lanzarGranadas (self):
        print("El personaje" + self.nombre + "lanzo granada")
        
    def recargarArma(self, municiones):
        cargador=10
        cargador = cargador + municiones
        print ("El arma recargada tiene" + cargador + "balas")
        