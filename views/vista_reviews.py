from tkinter import *

class VistaReviews(Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master = master
        self.controlador = controlador
        self.configure(bg="Orangered")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        
        """ESCRIBE UNA REVIEW"""
        self.review= Label(self, text="Escribe una Review",  bg="Orangered", font=("Comic Sans MS", 24, "bold"))
        self.review.grid()
        self.escribirReview = Entry(self)
        self.escribirReview.grid(padx=1, pady=1)
        
        self.boton_review= Button(self, text="Enviar Review", bg="SpringGreen4",  fg="gray7", font=("Comic Sans MS", 12 ,"bold"))
        self.boton_review.grid()
        
        """VER REVIEWS"""
        self.busqueda = Label(self, text="Reviews",  bg="Orangered", font=("Comic Sans MS", 24, "bold"))
        self.busqueda.grid(padx=0, pady=0)
        self.verReviews= Listbox(self, selectmode=SINGLE, font=("OpenSans"), fg="Orange", height=5, width=10)
        elementos=["Review 1", "Review 2", "Review 2", "Review 3", "Review 4"]
        for elemento in elementos:
            self.verReviews.insert(END, f"{elemento}")
        self.verReviews.grid()
        
        
        self.boton_inicio = Button(self, text="Inicio", command=self.controlador.regresar_inicio, bg="SpringGreen4",  fg="gray7", font=("Comic Sans MS", 12 ,"bold"))
        self.boton_inicio.grid(padx= 10, pady=10, sticky="nsew")
        self.boton_inicio.place()
