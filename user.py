#Clase para los usuarios
class User(object):
    nombre = "" #Nombre del usuario
    apellido = "" #Apellido del usuario
    usuario = "" #Username o nick del usuario
    password = "" #Contraseña de acceso
    tipo = 0 #Nivel de acceso del usuario

    #Constructor
    def __init__(self, nombre, apellido, usuario, password, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.password = password
        self.tipo = tipo
    
    #Funcion para guardar los datos en el archivo de permanencia
    def write(self):
        with open('usuarios.txt', 'a+') as archivo:
            linea = "\n{0}-{1}-{2}-{3}-{4}".format(self.nombre, self.apellido, self.usuario, self.password, self.tipo)
            archivo.write(linea)
    
