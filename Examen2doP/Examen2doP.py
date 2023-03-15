from tkinter import Tk, Frame, Button, messagebox,  Entry, Label

#1 Generar una ventana 
ventana = Tk ()
ventana.title("Bienvenido Humano, Generador de matriculas")
ventana.geometry("600x400")

################################################################################
#2 Agregamos Frames 
seccion1 = Frame(ventana, bg="red")
seccion1.pack(expand = True, fill = 'both')

nom = Label(seccion1, text=" Ingresa tu nombre:")
nom.place(x=150, y=30)

seccion2 = Frame(ventana, bg="gray")
seccion2.pack(expand = True, fill = 'both')

ap = Label(seccion1, text=" Ingresa tu apellido paterno: ")
ap.place(x=150, y=70)

am = Label(seccion2, text="Ingrese su apellido materno: ")
am.place(x=150, y=20)

nac = Label(seccion2, text = "Ingrese su año de nacimiento")
nac.place (x=150, y=50)

seccion3 = Frame(ventana, bg="purple")
seccion3.pack(expand = True, fill = 'both')

carr = Label(seccion3, text= "Ingrese su carrera")
carr.place(x=150, y=30)

#######################################################################

#3 Agregamos Entrys
nom1 = Entry (seccion1)
nom1.place (x=300, y=30)

ap1 = Entry(seccion1)
ap1.place(x=310, y=70)

am1 = Entry(seccion2)
am1.place(x=310, y=20)

nac1 = Entry(seccion2)
nac1.place(x=310, y=50)

carr1 = Entry(seccion3)
carr1.place(x=300, y=30)

###############################################################################

#4 Agregamos botones
BotonGenerar = Button(seccion3, text=" Generar matricula  ", bg = "#4298f5")
BotonGenerar.place(x=400,y=60, width=100, height=30)



# 5 Mentono Main para la ejecucion del ventama
ventana.mainloop()