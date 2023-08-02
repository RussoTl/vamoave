class ControladorInicio:
    def __init__(self, app):
        self.app = app

    def mostrar_busqueda_filtro(self):
        self.app.cambiar_frame(self.app.vista_actividades)

    def mostrar_destinos(self):
        self.app.cambiar_frame(self.app.vista_destinos)

    def mostrar_rutas(self):
        self.app.cambiar_frame(self.app.vista_rutas)

    def mostrar_reviews(self):
        self.app.cambiar_frame(self.app.vista_reviews)

    def salir(self):
        self.app.cambiar_frame(self.app.cerrar_app)