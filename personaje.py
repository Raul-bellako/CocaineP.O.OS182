class Personaje:
    
    #Agregamos el constructor del personaje
    def __init__(self,esp,nom,alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt
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
        cargador += municiones
        
        print ("El arma recargada tiene" + str(cargador) + "balas")
    
    