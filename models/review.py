import json

class Review:
    def __init__(self, id, id_destino, id_usuario, calificacion, comentario, animo):
        self.id= id
        self.id_destino= id_destino
        self.id_usuario= id_usuario
        self.calificacion= calificacion
        self.comentario= comentario
        self.animo= animo

    def to_json(self):
        return {"id": self.id,
                "id_destino": self.id_destino,
                "id_usuario": self.id_usuario,
                "calificacion": self.calificacion,
                "comentario": self.comentario,
                "animo": self.animo}

    @classmethod
    def from_json(cls, json_datos):
        id= json_datos["id"]
        id_destino= json_datos["id_destino"]
        id_usuario= json_datos["id_usuario"]
        calificacion= json_datos["calificacion"]
        comentario= json_datos["comentario"]
        animo= json_datos["animo"]
        return cls(id, id_destino, id_usuario, calificacion, comentario, animo)

    @staticmethod
    def guardar_review_a_json(review, nombre_archivo= "review_json"):
        with open(nombre_archivo, "w", encoding='utf-8') as archivo:
         json.dump(review.to_json(), archivo, indent=4, ensure_ascii=False)

    @staticmethod
    def cargar_review_desde_json(nombre_archivo= "review_json"):
        with open(nombre_archivo, "r", encoding='utf-8') as archivo:
            review_leida_json= json.load(archivo)
            review_leida= Review.from_json(review_leida_json)
        return review_leida

    @staticmethod
    def mostrar_review_cargada(review_leida):
        print("id: ", review_leida.id)
        print("id_desino: ", review_leida.id_destino)
        print("id_usuario: ", review_leida.id_usuario)
        print("Calificacion: ", review_leida.calificacion)
        print("Comentario: ", review_leida.comentario)
        print("Animo: ", review_leida.animo)

review= Review(1, 1, 1, 5, "Bueno, bonito y brato", "Positivo")

Review.guardar_review_a_json(review, "review_json")
review_leida= Review.cargar_review_desde_json("review_json")
Review.mostrar_review_cargada(review_leida)