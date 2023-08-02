import json


class RutaVisita:
    def __init__(self, id, nombre, destinos):
        self.id = id
        self.nombre = nombre
        self.destinos = destinos

    def to_json(self):
        destinos_json = []
        for destino in self.destinos:
            destinos_json.append(destino)
        return {
            "id": self.id,
            "nombre": self.nombre,
            "destinos": destinos_json
        }

    def __str__(self):
        return f"""\
            ID: {self.id}
            Nombre: {self.nombre}
            Destinos: {', '.join(self.destinos)}
        """

    @classmethod
    def from_json(cls, json_datos):
        id = json_datos["id"]
        nombre = json_datos["nombre"]
        destinos = json_datos["destinos"]
        return cls(id, nombre, destinos)

    @staticmethod
    def guardar_rutas_a_json(rutas, nombre_archivo="data/rutas_json"):
        rutas_json = []
        for ruta in rutas:
            rutas_json.append(ruta.to_json())

        with open(nombre_archivo, "w", encoding='utf-8') as archivo:
            json.dump(rutas_json, archivo, indent=4, ensure_ascii=False)

    @staticmethod
    def cargar_rutas_desde_json(nombre_archivo="data/rutas_json"):
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            rutas_leidas_json = json.load(archivo)
        rutas_leidas = []
        for ruta_json in rutas_leidas_json:
            ruta_leida = RutaVisita.from_json(ruta_json)
            rutas_leidas.append(ruta_leida)
        return rutas_leidas

    @staticmethod
    def mostrar_rutas_cargadas(rutas_cargadas):
        for ruta_cargada in rutas_cargadas:
            print("ID: ", ruta_cargada.id)
            print("Nombre: ", ruta_cargada.nombre)
            print("Destinos: ", ruta_cargada.destinos)
            print("--------------------")


# PRUEBAS JSON
ruta1 = RutaVisita(1, "Ruta Javi", [1, 2, 5])
ruta2 = RutaVisita(2, "Ruta Agustin", [1, 4, 5])
ruta3 = RutaVisita(3, "Ruta Mateo", [1, 3, 4])
ruta4 = RutaVisita(4, "Ruta Nacho", [4, 5, 6])
ruta5 = RutaVisita(5, "Ruta Andres", [4, 5])
ruta6 = RutaVisita(6, "Ruta David", [6])

rutas = [ruta1, ruta2, ruta3, ruta4, ruta5, ruta6]

# Guardar rutas visitadas en un archivo JSON
RutaVisita.guardar_rutas_a_json(rutas, "data/rutas_json")

# Cargar rutas visitadas desde el archivo JSON
rutas_leidas = RutaVisita.cargar_rutas_desde_json("data/rutas_json")

# Mostrar los datos recuperados
RutaVisita.mostrar_rutas_cargadas(rutas_leidas)
