from tkinter import Tk, Frame, Button, messagebox, simpledialog as simpledialog

#5 agregar funcion de mensaje

def mostrarmensaje():
    messagebox.showinfo("informacion","Te informo que")
    messagebox.showerror("error", "perdon te falle")
    print(messagebox.askokcancel("Pregunta", "Seguro que quieres guardar"))
    
    value = simpledialog.askstring("Input", "Ingrese un valor:")
    print("El valor ingresado es:", value)
    
    
#6. Funcion agregar botones
def agregarBoton ():
    botonverde.config(text="+", bg = "green")
    botonNuevo = Button (seccion3, text="Boton nuevo")
    botonNuevo.pack()

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

botonAzul = Button(seccion1, text="Soy el azul", bg = "#4298f5", command=mostrarmensaje)
botonAzul.place(x=60,y=60, width=100, height=30)

botonamarillo = Button(seccion2, text="Soy el amarillo", bg = "#e9f542")
botonamarillo.grid(row=1, column=1)

botonnegro = Button(seccion2, text= "soy el negro", bg = "#f542da")
botonnegro.grid(row=0,column=0)

botonverde = Button(seccion3, text= "soy el verde", bg = "#42f551", command=agregarBoton)
botonverde.pack()


#4 
#Mentono Main para la ejecucion del ventama
ventana.mainloop()