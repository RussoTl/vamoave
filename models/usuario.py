from tkinter import messagebox as MessageBox

class usuario():
    numUsuarios = 0
    def __init__(self, nombre, contra):#, id, historial_rutas):
        self.nombre = nombre
        self.contra = contra
        #self.id = id
        #self.historial_rutas = historial_rutas
        self.conectado = False
        self.intentos = 3

        usuario.numUsuarios += 1

    def conectar(self, contra = None):
        if contra==None:
            myContra = input("Ingrese su contraseña: ")
        else:
               myContra = contra
        if myContra == self.contra:
            print("Inicio de sesion exitoso")
            self.conectado = True
            return True
        else:
            self.intentos -= 1
            if self.intentos > 0:
                MessageBox.showinfo("Error","Usuario o contraseña incorrecta, intentelo de nuevo." f"Intentos restantes: {self.intentos}")
                if contra != None:
                    return False
                MessageBox.showinfo("Error", f"Intentos restantes: {self.intentos}")    
                self.conectar()
            else:
                print("A alcanzado el numero de intentos permitidos")
                print("Intente de nuevo mas tarde.")    

    def desconectar (self):
        if self.conectado:
            print("Se ha cerrado sesion.")
            self.conectado= False
        else:
            print("No inicio sesion")
        
    def __str__(self):
        if self.conectado:
            connect = "Conectado"
        else:
            connect = "Desconectado"
        return f"Mi nombre de usuario es {self.nombre} y estoy {connect}"
