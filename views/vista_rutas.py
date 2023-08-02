from tkinter import *

class VistaRutas(Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        #self.configure(bg="Orangered")
        self.titulo = Label(self, text="Rutas",  bg="Orangered", font=("Comic Sans MS", 24, "bold"))
        self.titulo.grid(pady=10)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        self.boton_inicio = Button(self, text="Inicio", command=self.controlador.regresar_inicio, bg="SpringGreen4",  fg="gray7", font=("Comic Sans MS", 12 ,"bold"))
        self.boton_inicio.grid(padx= 10, pady=10, sticky="nsew")
        self.boton_inicio.place()
