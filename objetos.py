from personaje import *

print("Datos para el objeto")

print("")
print("Solitcitud datos del heroe")
especieH =input ("Escribe la especie del heroee")
nombreH = input ("Escribe el nombre del heroe")
alturaH = float(input( "Escribe la altura del heroe"))
recargaH =int(input("Ingresa las balas para el heroe"))

print("")
print("Solicitud datos del villano")
especieV = input("Escribe la especie del villano")
nombreV = input ("Escribe el nombre del vilano")
alturaV = float(input("Escribe la altura del villano"))

recargaV = int(input("Ingresa las balas para el villano"))


#Creamos los objetos
Heroe =Personaje(especieH,nombreH,alturaH)
Villano =Personaje(especieV, nombreV, alturaV)


#Usamos los atributosdel heroe y villano
print("")
print ("El persobaje se llama" + Heroe.getNombre())
print ("Pertenece a la especie" + Heroe.getEspecie())
print ("Y una altura de " + str(Heroe.getAltura()))
print("")
Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(recargaH)
print("")

print ("El persobaje se llama" + Villano.getNombre())
print ("Pertenece a la especie" + Villano.getEspecie())
print ("Y una altura de " + str(Villano.getAltura()))
print("")
Villano.correr(True)
Villano.lanzarGranadas()
Villano.recargarArma(recargaV)
Villano.__pensar()





