import json


class DestinoCulinario:
    def __init__(self, id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad,
                 disponibilidad, id_ubicacion, imagen):
        self.id = id
        self.nombre = nombre
        self.tipo_cocina = tipo_cocina
        self.ingredientes = ingredientes
        self.precio_minimo = precio_minimo
        self.precio_maximo = precio_maximo
        self.popularidad = popularidad
        self.disponibilidad = disponibilidad
        self.id_ubicacion = id_ubicacion
        self.imagen = imagen

    def __str__(self):
        disponibilidad_str = 'Disponible' if self.disponibilidad else 'No disponible'
        return f"""\
            ID: {self.id}
            Nombre: {self.nombre}
            Tipo de cocina: {self.tipo_cocina}
            Ingredientes: {', '.join(self.ingredientes)}
            Precio mínimo: 💲{self.precio_minimo}
            Precio máximo: 💲{self.precio_maximo}
            Popularidad: ⭐️{self.popularidad}
            Disponibilidad: {disponibilidad_str}
            ID de ubicación: {self.id_ubicacion}
            Imagen: {self.imagen}
        """

    def to_json(self):
        ingredientes_json = []
        for ingrediente in self.ingredientes:
            ingredientes_json.append(ingrediente)
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo_cocina": self.tipo_cocina,
            "ingredientes": ingredientes_json,
            "precio_minimo": self.precio_minimo,
            "precio_maximo": self.precio_maximo,
            "popularidad": self.popularidad,
            "disponibilidad": self.disponibilidad,
            "id_ubicacion": self.id_ubicacion,
            "imagen": self.imagen
        }

    @classmethod
    def from_json(cls, json_datos):
        id = json_datos["id"]
        nombre = json_datos["nombre"]
        tipo_cocina = json_datos["tipo_cocina"]
        ingredientes = json_datos["ingredientes"]
        precio_minimo = json_datos["precio_minimo"]
        precio_maximo = json_datos["precio_maximo"]
        popularidad = json_datos["popularidad"]
        disponibilidad = json_datos["disponibilidad"]
        id_ubicacion = json_datos["id_ubicacion"]
        imagen = json_datos["imagen"]
        return cls(id, nombre, tipo_cocina, ingredientes, precio_minimo, precio_maximo, popularidad, disponibilidad,
                   id_ubicacion, imagen)

    @staticmethod
    def guardar_destinos_a_json(destinos, nombre_archivo="data/destinos_json"):
        # Método estático para guardar destinos en un archivo JSON
        destinos_json = []
        for destino in destinos:
            destinos_json.append(destino.to_json())

        with open(nombre_archivo, "w", encoding='utf-8') as archivo:
            json.dump(destinos_json, archivo, indent=4, ensure_ascii=False)

    @staticmethod
    def cargar_destinos_desde_json(nombre_archivo="data/destinos_json"):
        # Método estático para cargar destinos desde un archivo JSON
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            destinos_leidos_json = json.load(archivo)
        destinos_leidos = []
        for destino_json in destinos_leidos_json:
            destino_leido = DestinoCulinario.from_json(destino_json)
            destinos_leidos.append(destino_leido)
        return destinos_leidos

    @staticmethod
    def mostrar_destinos(destinos_cargados):
        # Muestra de datos recuperados de un archivo JSON
        for destino_leido in destinos_cargados:
            print("ID: ", destino_leido.id)
            print("Nombre: ", destino_leido.nombre)
            print("Tipo de cocina: ", destino_leido.tipo_cocina)
            print("Ingredientes: ", destino_leido.ingredientes)
            print("Precio mínimo: ", destino_leido.precio_minimo)
            print("Precio máximo: ", destino_leido.precio_maximo)
            print("Popularidad: ", destino_leido.popularidad)
            print("Disponibilidad: ", destino_leido.disponibilidad)
            print("ID de ubicación: ", destino_leido.id_ubicacion)
            print("Imagen: ", destino_leido.imagen)
            print("--------------------")


destino1 = DestinoCulinario(
    id=1,
    nombre="Sabor a Oriente",
    tipo_cocina="Mediterránea 🍝",
    ingredientes=["aceite de oliva",
                  "tomates 🍅", "ajo 🧄", "pescado 🐟"],
    precio_minimo=30.0,
    precio_maximo=50.0,
    popularidad=8.7,
    disponibilidad=True,
    id_ubicacion=1,
    imagen="image_1.png"
)
destino2 = DestinoCulinario(
    id=2,
    nombre="SUSHI GO Downtown",
    tipo_cocina="Japonesa 🍣",
    ingredientes=["arroz 🍚", "pescado fresco 🐟",
                  "alga nori 🌿", "salsa de soja 🍱"],
    precio_minimo=25.0,
    precio_maximo=60.0,
    popularidad=9.2,
    disponibilidad=True,
    id_ubicacion=2,
    imagen="image_2.png"
)

destino3 = DestinoCulinario(
    id=3,
    nombre="México Lindo",
    tipo_cocina="Mexicana 🌮",
    ingredientes=["tortillas de maíz 🌽",
                  "carne de res 🥩", "frijoles 🍛", "guacamole 🥑"],
    precio_minimo=20.0,
    precio_maximo=40.0,
    popularidad=8.5,
    disponibilidad=True,
    id_ubicacion=3,
    imagen="image_3.png"
)

destino4 = DestinoCulinario(
    id=4,
    nombre="La Fiamma",
    tipo_cocina="Italiana 🍕",
    ingredientes=["harina de trigo 🍞",
                  "salsa de tomate 🍅", "mozzarella 🧀", "albahaca 🌿"],
    precio_minimo=25.0,
    precio_maximo=45.0,
    popularidad=9.0,
    disponibilidad=True,
    id_ubicacion=4,
    imagen="image_4.png"
)

destino5 = DestinoCulinario(
    id=5,
    nombre="Agni Food",
    tipo_cocina="India 🍛",
    ingredientes=["arroz basmati 🍚", "pollo tikka masala 🍗",
                  "especias 🌶️", "lentejas 🍲"],
    precio_minimo=35.0,
    precio_maximo=55.0,
    popularidad=8.8,
    disponibilidad=True,
    id_ubicacion=5,
    imagen="image_5.png"
)

destino6 = DestinoCulinario(
    id=6,
    nombre="Design Resto",
    tipo_cocina="Francesa 🥐",
    ingredientes=["mantequilla 🧈", "harina de trigo 🍞",
                  "queso brie 🧀", "baguette 🥖"],
    precio_minimo=40.0,
    precio_maximo=70.0,
    popularidad=9.5,
    disponibilidad=True,
    id_ubicacion=6,
    imagen="image_6.png"
)

destinos = [destino1, destino2, destino3, destino4, destino5, destino6]

# Guardar destinos en un archivo JSON
DestinoCulinario.guardar_destinos_a_json(destinos, "data/destinos_json")

# Cargar destinos desde el archivo JSON
destinos_leidos = DestinoCulinario.cargar_destinos_desde_json(
    "data/destinos_json")

# Mostrar los datos recuperados
# DestinoCulinario.mostrar_destinos(destinos_leidos)
