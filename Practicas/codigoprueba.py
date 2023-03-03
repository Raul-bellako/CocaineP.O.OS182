from tkinter import Tk, Frame, Button, Entry, Label, messagebox
from Validacion import Validador

# 1 Generar una ventana
ventana = Tk()
ventana.title("Bienvenido Humano")
ventana.geometry("600x400")

# 2 Agregamos Frames y Entrys
seccion1 = Frame(ventana, bg="red")
seccion1.pack(expand=True, fill='both')

corr = Label(seccion1, text=" Ingresa el Correo:")
corr.place(x=150, y=30)

seccion2 = Frame(ventana, bg="gray")
seccion2.pack(expand=True, fill='both')

contrase = Label(seccion2, text=" Ingresa la Contraseña: ")
contrase.place(x=150, y=40)

seccion3 = Frame(ventana, bg="purple")
seccion3.pack(expand=True, fill='both')

corr1 = Entry(seccion1)
corr1.place(x=300, y=30)

contrase1 = Entry(seccion2, show="*")
contrase1.place(x=300, y=40)

#CorreoEntry= corr1.get()

# 3 Creamos los valores para loguearse.
correo = "121038661@upq.edu.mx"
contra = "Zeusyt900000000000000000000000000000000000000"

# 4 Creamos una instancia de la clase Validador
validador = Validador(correo, contra, corr1, contrase1)

# 5 Agregamos botones
botonlogeo = Button(seccion3, text=" Login", bg="#4298f5", command=validador.validar)
botonlogeo.place(x=500, y=60, width=100, height=30)

# 6 Mentono Main para la ejecucion del ventama
ventana.mainloop()