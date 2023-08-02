from tkinter import *
from views.vista_rutas import VistaRutas
from views.vista_destinos import VistaDestinos
from views.vista_busqueda_filtros import VistaBusquedaFiltro
from views.vista_inicio import VistaInicio
from views.vista_reviews import VistaReviews
from controladores.controlador_inicio import ControladorInicio
from controladores.controlador_busqueda_filtro import ControladorBusquedaFiltro
from controladores.controlador_destinos import ControladorDestinos
from controladores.controlador_rutas import ControladorRutas
from controladores.controlador_reviews import ControladorReviews


"""VENTANA PRINCIPAL"""
class Aplicacion(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Foodie Tour")
        self.config(bg="Orangered")
        self.geometry("500x500")
        self.resizable(False, False)
        self.iniciar()
        self.cambiar_frame(self.vista_inicio)
        
        
    def iniciar(self):
        controlador_inicio= ControladorInicio(self)
        controlador_actividades= ControladorBusquedaFiltro(self)
        controlador_destinos= ControladorDestinos(self)
        controlador_rutas=ControladorRutas(self)
        controlador_reviews= ControladorReviews(self)
        
        self.vista_inicio= VistaInicio(self, controlador_inicio)
        self.vista_actividades= VistaBusquedaFiltro(self, controlador_actividades)
        self.vista_destinos = VistaDestinos(self, controlador_destinos, self.seleccionar_destino)
        self.vista_rutas= VistaRutas(self, controlador_rutas)
        self.vista_reviews= VistaReviews(self, controlador_reviews)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_actividades)
        self.ajustar_frame(self.vista_destinos)
        self.ajustar_frame(self.vista_rutas)
        self.ajustar_frame(self.vista_reviews)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
    def ajustar_frame(self, frame):
        frame.grid(row=0, column= 0, sticky="nsew")
    
    def cambiar_frame(self, frame_destino):
        frame_destino.tkraise()
        
    def seleccionar_destino(self, id):
        # Acceder a la instancia de VistaDestinos y obtener el atributo lista_destinos
        lista_destinos = self.vista_destinos.lista_destinos
        # Obtiene el índice del elemento seleccionado
        indice_seleccionado = lista_destinos.curselection()
        if indice_seleccionado:
            # Obtiene el local seleccionado
            destino_seleccionado = self.vista_destinos.controladorDestino.buscar_destino_por_id(id)
        
            ubicacion_seleccionada = None
            print("Destino seleccionado:", destino_seleccionado.nombre)
            # Busca la ubicación correspondiente al local seleccionado
            for ubicacion in self.vista_destinos.ubicaciones:
                if ubicacion.id == destino_seleccionado.id_ubicacion:
                    ubicacion_seleccionada = ubicacion
                    break
                
            if ubicacion_seleccionada:
                # Centra el mapa en la ubicación seleccionada
                self.vista_destinos.mapa.set_position(ubicacion_seleccionada.coordenadas[0], ubicacion_seleccionada.coordenadas[1])
                print(f"Latitud: {ubicacion_seleccionada.coordenadas[0]}, Longitud: {ubicacion_seleccionada.coordenadas[1]}")
                
                
    def seleccionar_ubicacion(self, marcador, ubicacion_id):
        if marcador.image_hidden:
            marcador.hide_image(False)
        else:
            marcador.hide_image(True)
        print("Ubicación seleccionada: ", marcador.text)  

if __name__== "__main__":
    app = Aplicacion()
    app.mainloop()