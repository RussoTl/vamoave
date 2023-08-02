class CerrarApp:
    def __init__(self, app):
        self.app = app
    
    def cerrar_app(self):
        self.app.cambiar_frame(self.app.destroy())