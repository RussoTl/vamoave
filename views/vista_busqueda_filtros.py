from tkinter import *
class VistaBusquedaFiltro(Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.config(bg="Orangered")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        """LABEL BUSQUEDA"""
        self.busqueda = Label(self, text="Busqueda",  bg="Orangered", font=("Comic Sans MS", 24, "bold"))
        self.busqueda.grid()
        
        """ BARRA DE BUSQUEDA """
        self.barraBusqueda = Entry(self)
        self.barraBusqueda.grid(row=1, column=0, padx=10, pady=10)
        self.botonBusqueda = Button(self, text="Buscar", bg="SpringGreen4",  fg="gray7", font=("Comic Sans MS", 12 ,"bold"))
        self.botonBusqueda.grid(row=1, column=1, padx=5)
        
        """LABEL FILTROS"""
        self.filtros = Label(self, text="Filtros",  bg="Orangered", font=("Comic Sans MS", 24, "bold"))
        self.filtros.grid()
        
        """LISTBOX DE FILTROS"""
        
        self.lista= Listbox(self,  bg="Orange", font=("OpenSans",12))
        elementos=["Tipo de Cocina", "Ingredientes", "Rango de precios", "Popularidad de platos", "Eventos"]
        for elemento in elementos:
            self.lista.insert(END, f"{elemento}>")
        self.lista.grid()
        

        
        self.boton_inicio = Button(self, text="Inicio", command=self.controlador.regresar_inicio, bg="SpringGreen4",  fg="gray7", font=("Comic Sans MS", 12 ,"bold"))
        self.boton_inicio.grid(padx= 10, pady=10, sticky="nsew")
        self.boton_inicio.place()

