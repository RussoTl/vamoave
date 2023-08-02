import json


class Ubicacion:
    def __init__(self, id, direccion, coordenadas=None):
        self.id = id
        self.direccion = direccion
        if coordenadas is None:
            self.coordenadas = []
        else:
            self.coordenadas = coordenadas

    def __str__(self):
        return f"""\
            ID: {self.id}
            Dirección: {self.direccion}
            Coordenadas: {', '.join(self.coordenadas)}
        """

    def to_json(self):
        coordenadas_json = []
        for coordenada in self.coordenadas:
            coordenadas_json.append(coordenada)

        return {
            "id": self.id,
            "direccion": self.direccion,
            "coordenadas": coordenadas_json
        }

    @classmethod
    def from_json(cls, json_datos):
        id = json_datos["id"]
        direccion = json_datos["direccion"]
        coordenadas = json_datos["coordenadas"]
        return cls(id, direccion, coordenadas)

    @staticmethod
    def guardar_ubicaciones_a_json(ubicaciones, nombre_archivo="data/ubicaciones_json"):
        ubicaciones_json = []
        for ubicacion in ubicaciones:
            ubicaciones_json.append(ubicacion.to_json())

        with open(nombre_archivo, "w", encoding='utf-8') as archivo:
            json.dump(ubicaciones_json, archivo, indent=4, ensure_ascii=False)

    @staticmethod
    def cargar_ubicaciones_desde_json(nombre_archivo="data/ubicaciones_json"):
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            ubicaciones_leidas_json = json.load(archivo)
        ubicaciones_leidas = []
        for ubicacion_json in ubicaciones_leidas_json:
            ubicacion_leida = Ubicacion.from_json(ubicacion_json)
            ubicaciones_leidas.append(ubicacion_leida)
        return ubicaciones_leidas

    @staticmethod
    def mostrar_ubicaciones_cargadas(ubicaciones_cargadas):
        for ubicacion_cargada in ubicaciones_cargadas:
            print("id: ", ubicacion_cargada.id)
            print("Dirccion: ", ubicacion_cargada.direccion)
            print("Coordenadas: ", ubicacion_cargada.coordenadas)


# PRUEBAS
ubi1 = Ubicacion(1, "Catamarca 562, A4400 Salta",
                 [-24.79713218569837, -65.40623003385596])
ubi2 = Ubicacion(2, "Deán Funes 398, A4400 Salta",
                 [-24.78517781021208, -65.40776759152692])
ubi3 = Ubicacion(3, "Pueyrredón 350, Salta",
                 [-24.785503373748025, -65.40651857754554])
ubi4 = Ubicacion(4, "Catamarca 370, A4400 Salta",
                 [-24.79434675819614, -65.40617525982043])
ubi5 = Ubicacion(5, "Av. Paraguay 1275, A4400 Salta",
                 [-24.80601111093018, -65.41960729152595])
ubi6 = Ubicacion(6, "Av. Belgrano 770, A4400 Salta",
                 [-24.78637982863709, -65.41286627923948])

lista_ubicaciones = [ubi1, ubi2, ubi3, ubi4, ubi5, ubi6]

Ubicacion.guardar_ubicaciones_a_json(
    lista_ubicaciones, "data/ubicaciones_json")

ubicaciones_leidas = Ubicacion.cargar_ubicaciones_desde_json(
    "data/ubicaciones_json")

# Ubicacion.mostrar_ubicaciones_cargadas(ubicaciones_leidas)
