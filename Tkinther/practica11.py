from tkinter import Tk, Button, Frame

#1 Generar una ventana 
ventana = Tk ()
ventana.title("JIJIJIJIIJI")
ventana.geometry("600x400")

#2 Agregamos Frames
seccion1 = Frame(ventana, bg="red")
seccion1.pack(expand = True, fill = 'both')

seccion2 = Frame(ventana, bg="gray")
seccion2.pack(expand = True, fill = 'both')

seccion3 = Frame(ventana, bg="purple")
seccion3.pack(expand = True, fill = 'both')

#Agregamos botones

botonAzul = Button(seccion1, text="Soy el azul", bg = "blue")
botonAzul.place(x=60,y=60, width=100, height=30)

botonamarillo = Button(seccion2, text="Soy el amarillo", bg = "yellow")
botonamarillo.grid(row=1, column=1)

botonnegro = Button(seccion2, text= "soy el negro", bg = "black")
botonnegro.grid(row=0,column=0)

botonverde = Button(seccion3, text= "soy el verde", bg = "green")
botonverde.pack()

#Mentono Main para la ejecucion del ventama
ventana.mainloop()