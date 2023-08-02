import json


class Actividad:
    def __init__(self, id, nombre, destino_id, hora_inicio):
        self.id = id
        self.nombre = nombre
        self.destino_id = destino_id
        self.hora_inicio = hora_inicio

    def __str__(self):
        return f"""\
            ID: {self.id}
            Nombre: {self.nombre}
            ID de Destino: {self.destino_id}
            Hora de Inicio: {self.hora_inicio}
        """

    def to_json(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "destino_id": self.destino_id,
            "hora_inicio": self.hora_inicio
        }

    @classmethod
    def from_json(cls, json_datos):
        id = json_datos["id"]
        nombre = json_datos["nombre"]
        destino_id = json_datos["destino_id"]
        hora_inicio = json_datos["hora_inicio"]
        return cls(id, nombre, destino_id, hora_inicio)

    @staticmethod
    def guardar_actividades_a_json(actividades, nombre_archivo="data/actividades_json"):
        actividades_json = []
        for actividad in actividades:
            actividades_json.append(actividad.to_json())

        with open(nombre_archivo, "w", encoding='utf-8') as archivo:
            json.dump(actividades_json, archivo, indent=4, ensure_ascii=False)

    @staticmethod
    def cargar_actividades_desde_json(nombre_archivo="data/actividades_json"):
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            actividades_leidas_json = json.load(archivo)
        actividades_leidas = []
        for actividad_json in actividades_leidas_json:
            actividad_leida = Actividad.from_json(actividad_json)
            actividades_leidas.append(actividad_leida)
        return actividades_leidas

    @staticmethod
    def mostrar_actividades_cargadas(actividades_cargadas):
        for actividad_cargada in actividades_cargadas:
            print("ID: ", actividad_cargada.id)
            print("Nombre: ", actividad_cargada.nombre)
            print("ID de Destino: ", actividad_cargada.destino_id)
            print("Hora de Inicio: ", actividad_cargada.hora_inicio)
            print("--------------------")


# PRUEBAS JSON
actividad1 = Actividad(1, "Actividad 1", 2, "2023-07-04T09:00:00")
actividad2 = Actividad(2, "Actividad 2", 5, "2023-07-04T11:00:00")
actividad3 = Actividad(3, "Actividad 3", 3, "2023-07-04T08:10:00")
actividad4 = Actividad(4, "Actividad 4", 1, "2023-07-04T09:05:00")

actividades = [actividad1, actividad2, actividad3, actividad4]

# Guardar actividades en un archivo JSON
Actividad.guardar_actividades_a_json(actividades, "data/actividades_json")

# Cargar actividades desde el archivo JSON
actividades_leidas = Actividad.cargar_actividades_desde_json(
    "data/actividades_json")

# Mostrar los datos recuperados
Actividad.mostrar_actividades_cargadas(actividades_leidas)
