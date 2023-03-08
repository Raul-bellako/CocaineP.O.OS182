import random
import string
from tkinter import Tk, Frame, Button, Checkbutton, Label, IntVar

# Función para generar una contraseña aleatoria
def generar_contrasena(mayusculas=False):
    longitud = 12  # Longitud de la contraseña
    caracteres = string.ascii_lowercase + string.digits + string.punctuation  # Caracteres permitidos
    if mayusculas:
        caracteres += string.ascii_uppercase  # Agregar letras mayúsculas si se solicita
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))  # Generar contraseña aleatoria
    return contrasena

# 1 Generar una ventana
ventana = Tk()
ventana.title("Generador de Contraseñas")
ventana.geometry("600x500")

# 2 Agregamos Frames, Entrys, etiquetas y un checkbutton
seccion1 = Frame(ventana, bg="white")
seccion1.pack(expand=True, fill='both')

contrasena = Label(seccion1, text="Presiona el botón para generar una contraseña aleatoria", font=("Arial", 16))
contrasena.place(relx=0.5, rely=0.3, anchor='center')

seccion2 = Frame(ventana, bg="white")
seccion2.pack(expand=True, fill='both')

mayusculas_var = IntVar()
mayusculas_check = Checkbutton(seccion2, text="Incluir mayúsculas", variable=mayusculas_var, font=("Arial", 12))
mayusculas_check.pack(pady=10)

# 3 Agregamos un botón para generar contraseñas
def generar():
    nueva_contrasena = generar_contrasena(mayusculas=mayusculas_var.get())
    contrasena.config(text=nueva_contrasena)

boton_generar = Button(ventana, text="Generar Contraseña", bg="#4298f5", fg="white", font=("Arial", 12), command=generar)
boton_generar.place(relx=0.5, rely=0.6, anchor='center', width=200, height=50)

# 4 Mentono Main para la ejecucion del ventama
ventana.mainloop()
