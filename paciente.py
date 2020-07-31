class Paciente(object):
    nombre = ""
    apellido = ""
    fiebre = 0
    resp = 0
    tos = 0
    dolor = 0
    estado = 0

    def __init__(self, nombre, apellido, fiebre, resp, tos, dolor, estado):
        self.nombre = nombre
        self.apellido = apellido
        self.fiebre = fiebre
        self.resp = resp
        self.tos = tos
        self.dolor = dolor
        self.estado = estado

    def write(self):
        with open('pacientes.txt', 'a') as archivo:
            linea = "\n{0}-{1}-{2}-{3}-{4}-{5}-{6}".format(self.nombre, self.apellido, self.fiebre, self.resp, self.tos, self.dolor, self.estado)
            archivo.write(linea)
