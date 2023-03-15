import tkinter as tk
from tkinter import messagebox, Frame
from  generadorr import Estudiante

## 1Funcion 
def generar_matri():
    nombre = entnombre.get()
    apellido_paterno = entapellido_paterno.get()
    apellido_materno = entapellido_materno.get()
    anio_nacimiento = int(entañoo_nacimiento.get())
    carrera = entcarrera.get()

    estudiante = Estudiante(nombre, apellido_paterno, apellido_materno, anio_nacimiento, carrera)
    matricula = estudiante.generar_matri()

    messagebox.showinfo("Matrícula Generada", matricula)

# # 2 Ventana
ventana = tk.Tk()
ventana.title("Generador de Matrículas UPQ JIJI")


# 3 Etiquetas
etinombre = tk.Label(ventana, text="Add Nombre:")
etinombre.grid(row=0, column=0, padx=5, pady=5)

etiapellido_paterno = tk.Label(ventana, text="Add Apellido Paterno:")
etiapellido_paterno.grid(row=1, column=0, padx=5, pady=5)

etiapellido_materno = tk.Label(ventana, text="Add Apellido Materno:")
etiapellido_materno.grid(row=2, column=0, padx=5, pady=5)

etiañoo_nacimiento = tk.Label(ventana, text="Add Año de Nacimiento:")
etiañoo_nacimiento.grid(row=3, column=0, padx=5, pady=5)

eticarrera = tk.Label(ventana, text="Add Carrera:")
eticarrera.grid(row=4, column=0, padx=5, pady=5)

# 4 Entradas
entnombre = tk.Entry(ventana)
entnombre.grid(row=0, column=1, padx=5, pady=5)

entapellido_paterno = tk.Entry(ventana)
entapellido_paterno.grid(row=1, column=1,padx=5, pady=5)

entapellido_materno = tk.Entry(ventana)
entapellido_materno.grid(row=2, column=1, padx=5, pady=5)

entañoo_nacimiento = tk.Entry(ventana)
entañoo_nacimiento.grid(row=3, column=1, padx=5, pady=5)

entcarrera = tk.Entry(ventana)
entcarrera.grid(row=4, column=1, padx=5, pady=5)

# 5 Boton

boton_genematricula = tk.Button(ventana, text="Generar Matrícula", command=generar_matri)
boton_genematricula.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()