from tkinter import *
from tkinter import ttk
import tkinter as tk 

v = Tk()
v. title ("CRUDE de usuarios")
v.geometry ("500x300")


panel=ttk.Notebook(v)
panel.pack(fill="both", expand='yes')

pestana1=ttk.Frame(panel)
pestana2=ttk.Frame(panel)
pestana3=ttk.Frame(panel)
pestana4=ttk.Frame(panel)

#Pestana 1 formulario de registro

titulo=Label(pestana1, text="Registro usuarios", fg="blue", font=("Modern",18)).pack()

varNom=tk.StringVar()
lblNom=Label(pestana1, text="Nombre: ").pack()
txtNom= Entry(pestana1, textvariable=varNom).pack()

varCorr=tk.StringVar()
lblNom=Label(pestana1, text="Correo: ").pack()
txtNom= Entry(pestana1, textvariable=varCorr).pack()

varCont=tk.StringVar()
lblNom=Label(pestana1, text="Contrasena: ").pack()
txtNom= Entry(pestana1, textvariable=varCont).pack()

btnGaurdar=Button(pestana1, text='Guardar usuario').pack()



panel.add(pestana1, text="Formulario de ususarios")
panel.add(pestana2, text="Buscar usuario")
panel.add(pestana3, text="Consultar ususarios")
panel.add(pestana4, text="Actualizar ususarios")

v.mainloop()

