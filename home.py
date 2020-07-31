from tkinter import Frame,Menu, Label, Entry, END,FLAT, Checkbutton, Radiobutton, IntVar, Button, LEFT, W, E
from classes.Paciente import Paciente
from classes.User import User

#Pantalla principal de la aplicacion
class Home(Frame):
    def __init__(self, parent, user, login):
        self.user = user
        self.parent = parent
        self.login = login
        super(Home,self).__init__(parent)
        self.menubar = Menu(parent.master.master)
        parent.master.master.config(menu=self.menubar)
        self.menubar.add_command(label="Home", command=lambda:self.home())
        opciones1 = Menu(self.menubar, tearoff=0)
        opciones1.add_command(label="Listar pacientes", command=lambda:self.listar_pacientes())
        if self.user.tipo == "1":
            opciones1.add_command(label="Registrar pacientes", command = lambda:self.crear_paciente())
        opciones1.add_command(label="Estadisticas", command = lambda:self.estadisticas())
        self.menubar.add_cascade(label="Pacientes", menu=opciones1)

        if self.user.tipo == "1":
            opciones2 = Menu(self.menubar, tearoff=0)
            opciones2.add_command(label="Registrar usuario", command=lambda:self.registrar_usuario())
            self.menubar.add_cascade(label="Usuarios", menu=opciones2)
        self.menubar.add_command(label="Cerrar sesion", command=lambda:self.salir())
        self.home()
        
    def home(self):
        self.clear()
        self.bienvenida = Label(self, text="Bienvenido al sistema de control de COVID-19", font=("Arial Bold", 20))
        self.bienvenida.grid(row=1, pady=35)
        self.message = Label(
            self, 
            text="Sistema capaz de contabilizar y controlar la cantidad de pacientes infectados  y ayudar a la difusion  de la informacion y \n datos sobre el virus, desde control de los sintomas para mejor analisis de la enfermedad  \n hasta el numero de infectados, muertos y recuperados para la toma de decisiones demograficas",
            font=("Arial Bold", 10)
        )
        self.message.grid(row=2, pady=20)

    def clear(self):
        wid = self.grid_slaves()
        for l in wid:
            l.destroy()
    
    def listar_pacientes(self):
        self.clear()
        filas = [
            ["Nombre", "Apellido", "Fiebre", "Respiracion", "Tos", "Dolores", "Estado"],
        ]
        archivo = open('pacientes.txt', 'r')
        lineas = archivo.readlines()
        for l in lineas:
            cols = l.split('-')
            filas.append([cols[0], cols[1], cols[2], cols[3], cols[4], cols[5], cols[6].split('\n')[0]])
        archivo.close()
        i = 2
        for fila in filas :
            j = 0
            for columna in fila:
                if(i == 2):
                    self.e = Entry(self,width=15,fg="blue", font=("Arial", 10, "bold"))
                    self.e.grid(row=i,column=j)
                    self.e.insert(END, columna)
                else:
                    self.e = Entry(self,width=15, font=("Arial", 10, "bold"))
                    self.e.grid(row=i,column=j)
                    if j == 3 and  columna=="1":
                        self.e.insert(END, "Forzada")
                    elif j ==3 and columna!="1":
                        self.e.insert(END, "Normal")
                    elif j == 6 and columna == "0":
                        self.e.insert(END, "Infectado")
                    elif j == 6 and columna == "1":
                        self.e.insert(END, "Recuperado")
                    elif j == 6 and columna == "2":
                        self.e.insert(END, "Fallecido")
                    elif j > 1 and columna == "0":
                        self.e.insert(END, "No")
                    elif j > 1 and columna == "1":
                        self.e.insert(END, "Si")
                    else:
                        self.e.insert(END, columna)
                self.e["state"] = "readonly"
                j += 1
            i += 1

    def crear_paciente(self):
        self.clear()
        self.label_nombre = Label(self, text="Nombre: ", font=("Arial", 20, "bold"), anchor="w")
        self.label_nombre.grid(row=3, column=1, rowspan=2)
        self.entry_nombre = Entry(self)
        self.entry_nombre.grid(row=3, column=2, rowspan=2)
        self.label_apellido = Label(self, text="Apellido: ", font=("Arial", 20, "bold"))
        self.label_apellido.grid(row=3, column=3, rowspan=2)
        self.entry_apellido = Entry(self)
        self.entry_apellido.grid(row=3, column=4, rowspan=2)
        self.label_sintomas = Label(self, text="Sintomas: ", font=("Arial", 20, "bold"), anchor="w")
        self.fiebre = IntVar()
        self.resp = IntVar()
        self.tos= IntVar()
        self.dolor = IntVar()
        self.label_sintomas.grid(row=5, column=1, pady=15)
        self.check_fiebre = Checkbutton(self, text="Fiebre", variable=self.fiebre, onvalue=1, offvalue=0)
        self.check_fiebre.grid(row=6,column=1)
        self.check_resp = Checkbutton(self, text="Dificultad para respirar", variable=self.resp, onvalue=1, offvalue=0)
        self.check_resp.grid(row=6,column=2, columnspan=2)
        self.check_tos = Checkbutton(self, text="Tos", variable=self.tos, onvalue=1, offvalue=0)
        self.check_tos.grid(row=6,column=4)
        self.check_dolor = Checkbutton(self, text="Dolor", variable=self.dolor, onvalue=1, offvalue=0)
        self.check_dolor.grid(row=6,column=5)
        self.label_estado = Label(self, text="Estado: ", font=("Arial", 20, "bold"), anchor="w")
        self.label_estado.grid(row=7, column=1, pady=15)
        self.estado = IntVar()
        self.radio_vivo= Radiobutton(self, text="Infectado", variable=self.estado, value = 0)
        self.radio_vivo.grid(row=8, column=1)
        self.radio_recuperado= Radiobutton(self, text="Recuperado", variable=self.estado, value = 1)
        self.radio_recuperado.grid(row=8, column=2)
        self.radio_fallecido= Radiobutton(self, text="Fallecido", variable=self.estado, value = 2)
        self.radio_fallecido.grid(row=8, column=3)
        self.login_button = Button(
            self, 
            text="Registrar",
            width=13,
            pady=5,
            font=("Arial bold", 15), 
            bg="deep sky blue", 
            fg="white",
            relief = FLAT,
            cursor = "hand2",
            command=lambda:self.guardar()
        )
        self.login_button.grid(row=9, column=5, columnspan=2)
        self.label_warning = Label(self, text="",fg="red", font=("Arial", 9, "bold"), anchor="w")
        self.label_warning.grid(row=10, column=1, pady=15)

    def guardar(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()

        if(nombre == "" or apellido == ""):
            self.label_warning.configure(text="Introduzca el nombre y el apellido del paciente")
            return
        
        newPaciente = Paciente(nombre, apellido,self.fiebre.get(),self.resp.get(),self.tos.get(),self.dolor.get(),self.estado.get())
        newPaciente.write()
        self.home()

    def estadisticas(self):
        self.clear()

        cont_fiebre = 0
        cont_resp = 0
        cont_tos = 0
        cont_dolor = 0
        cont_rec = 0
        cont_fa = 0
        archivo = open('pacientes.txt','r')
        lineas = archivo.readlines()
        for linea in lineas:
            columnas = linea.split('-')
            if int(columnas[2]) == 1:
                cont_fiebre +=1
            if int(columnas[3]) == 1:
                cont_resp+=1
            if int(columnas[4]) == 1:
                cont_tos += 1
            if int(columnas[5]) == 1:
                cont_dolor +=1
            if int(columnas[6].split('\n')[0]) == 1:
                cont_rec +=1
            if int(columnas[6].split('\n')[0]) == 2:
                cont_fa +=1

        archivo.close()

        self.label_inf = Label(self, text="Infectados: "+ str(len(lineas)), font=("Arial", 20, "bold"), anchor=W)
        self.label_inf.grid(row=1, column=1, sticky=W+E)
        self.label_rec = Label(self, text="Recuperados: "+ str(cont_rec), font=("Arial", 20, "bold"), anchor=W)
        self.label_rec.grid(row=2, column=1, sticky=W+E)
        self.label_fa = Label(self, text="Fallecidos: "+ str(cont_fa), font=("Arial", 20, "bold"), anchor=W)
        self.label_fa.grid(row=3, column=1, sticky=W+E)
        self.label_fie = Label(self, text="Pacientes con fiebre: "+ str(cont_fiebre), font=("Arial", 20, "bold"),anchor=W)
        self.label_fie.grid(row=4, column=1, sticky=W+E)
        self.label_resp = Label(self, text="Pacientes con respiracion afectada: "+ str(cont_resp), font=("Arial", 20, "bold"),anchor=W)
        self.label_resp.grid(row=5, column=1, sticky=W+E)
        self.label_tos = Label(self, text="Pacientes con tos: "+ str(cont_tos), font=("Arial", 20, "bold"),anchor=W)
        self.label_tos.grid(row=6, column=1, sticky=W+E)
        self.label_dolor = Label(self, text="Pacientes con dolor: "+ str(cont_dolor), font=("Arial", 20, "bold"),anchor=W)
        self.label_dolor.grid(row=7, column=1, sticky=W+E)

    def registrar_usuario(self):
        self.clear()
        self.label_nombre = Label(self, text="Nombre: ", font=("Arial", 20, "bold"), anchor="w")
        self.label_nombre.grid(row=1, column=1, rowspan=2, sticky=W+E)
        self.entry_nombre_user = Entry(self)
        self.entry_nombre_user.grid(row=1, column=2, rowspan=2)
        self.label_apellido = Label(self, text="Apellido: ", font=("Arial", 20, "bold"), anchor="w", pady=10)
        self.label_apellido.grid(row=1, column=3, rowspan=2, sticky=W+E)
        self.entry_apellido_user = Entry(self)
        self.entry_apellido_user.grid(row=1, column=4, rowspan=2)
        self.label_usuario = Label(self, text="Usuario: ", font=("Arial", 20, "bold"), anchor="w")
        self.label_usuario.grid(row=3, column=1, rowspan=2, sticky=W+E)
        self.entry_usuario = Entry(self)
        self.entry_usuario.grid(row=3, column=2, rowspan=2)
        self.label_password = Label(self, text="Contraseña: ", font=("Arial", 20, "bold"), anchor="w", pady=10)
        self.label_password.grid(row=3, column=3, rowspan=2, sticky=W+E)
        self.entry_password = Entry(self)
        self.entry_password.grid(row=3, column=4, rowspan=2)
        self.super_user = IntVar()
        self.check_super = Checkbutton(self, text="Super usuario", variable=self.super_user, onvalue=1, offvalue=2)
        self.check_super.grid(row=5,column=1)
        self.regist_button = Button(
            self, 
            text="Registrar",
            width=13,
            pady=5,
            font=("Arial bold", 15), 
            bg="deep sky blue", 
            fg="white",
            relief = FLAT,
            cursor = "hand2",
            command=lambda:self.guardar_user()
        )
        self.regist_button.grid(row=5, column=5, columnspan=2)

    def guardar_user(self):
        nombre = self.entry_nombre_user.get()
        apellido = self.entry_apellido_user.get()
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()
        if nombre == "" or apellido == "" or usuario == "" or password == "":
            return
        newUser = User(nombre, apellido, usuario, password, self.super_user.get())
        newUser.write()
        self.home()

    def salir(self):
        self.parent.create_window((0, 0), window=self.login, anchor="nw")
        self.parent.configure(yscrollcommand=self.parent.scroll.set)
        self.login.bind(
            "<Configure>",
            lambda e: self.parent.configure(
                scrollregion=self.parent.bbox("all")
            )
        )
        self.menubar.destroy()
        self.destroy()
