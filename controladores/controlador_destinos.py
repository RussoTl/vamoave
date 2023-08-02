from PIL import Image, ImageTk

class ControladorDestinos:
    def __init__(self, app):
        self.app = app
        
    def buscar_destino_por_id(self, id):
        for destino in self.app.vista_destinos.destinos:
            if destino.id == id:
                return destino
        raise ValueError(f"No se encontró ningún destino con el ID {id}")  

        
    def regresar_inicio(self):
        self.app.cambiar_frame(self.app.vista_inicio)