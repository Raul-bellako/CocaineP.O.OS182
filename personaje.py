class Personaje:
    
    #Agregamos el constructor del personaje
    def __init__(self,esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    #Metodos
    
    def correr(self, status):
        if (status):
            print ("El personaje " + self.__nombre + "Esta corriendo")
        else :
            print ("El personaje " + self.__nombre + "Se detuvo")
    
    def lanzarGranadas (self):
        print("El personaje" + self.__nombre + "lanzo granada")
        
    def recargarArma(self, municiones):
        cargador=10
        cargador += municiones
        
        print ("El arma recargada tiene" + str(cargador) + "balas")
        
    def pensar (self):
        print("toy pensandooooooooo........")
        
    #Agregamos get y set
    def getEspecie(self):
      return self.__especie
    
    def setEspecie(self,esp):
        self.__especie = esp
        
        
    def getNombre(self):
      return self.__nombre
    
    def setNombre(self,nom):
        self.__nombre = nom
        
    def getAltura(self):
      return self.__altura
    
    def setAltura(self,alt):
        self.__altura = alt
    