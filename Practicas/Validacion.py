from tkinter import messagebox

class Validador:
    def __init__(self, correo, contra, corr1, contrase1):
        self.correo = correo
        self.contra = contra
        self.corr1 = corr1
        self.contrase1 = contrase1

    def validar(self):
        if self.correo == self.corr1.get() and self.contra == self.contrase1.get():
            messagebox.showinfo("Login", "Hola Has ingresado excelentemente bien")
        else:
            messagebox.showerror("Error", "Tus datos no jalan bro")
