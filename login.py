from tkinter import Frame, Label, Entry, Button, W,E, FLAT
from frames.Home import Home
from classes.User import User

#Ventana de inicio de sesion
class Login(Frame):
    def __init__(self, parent):
        self.parent = parent
        super(Login,self).__init__(parent, pady=100)
        
        self.label_title = Label(self, text="Login", font= ("Arial Bold", 30), pady=20)
        self.label_title.grid(row=1, column=3, columnspan=2)

        self.label1 = Label(self, text="Username:", font= ("Arial Bold", 15), anchor=W)
        self.label1.grid(row=2, column=3)

        self.entry_username = Entry(self)
        self.entry_username.grid(row=2, column=4)

        self.label2 = Label(self, text="Contraseña:", font= ("Arial Bold", 15), anchor=W)
        self.label2.grid(row=4, column=3)

        self.entry_password = Entry(self)
        self.entry_password.grid(row=4, column=4)
        self.bienvenida = Label(self, text="COVID-19", font=("Arial Bold", 20), anchor="center")
        self.bienvenida.grid(row=4, column=7, columnspan=3, pady=20, padx=50)
        self.sep_label = Label(self,text="")
        self.sep_label.grid(row=5, rowspan=3)
        self.login_button = Button(
            self, 
            text="Iniciar Sesion", 
            height=2, 
            width=13, 
            font=("Arial bold", 15), 
            bg="deep sky blue", 
            fg="white",
            relief = FLAT,
            cursor = "hand2",
            command=lambda:self.login()
        )
        self.login_button.grid(row=9, column=3, columnspan=2)
        self.message_label = Label(self,text="", fg="red")
        self.message_label.grid(row=10,column=3, columnspan=2)
        
    
    def login(self):
        existe = False
        passw = ""
        user = None
        with open('usuarios.txt', 'r') as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                columnas = linea.split('-')
                if(self.entry_username.get() == columnas[2]):
                    existe = True
                    passw = columnas[3]
                    user = User(columnas[0],columnas[1],columnas[2],columnas[3],columnas[4].split('\n')[0])
        if(existe):
            if passw == self.entry_password.get():
                home = Home(self.parent, user, Login(self.parent))
                self.parent.create_window((0, 0), window=home, anchor="nw")
                self.parent.configure(yscrollcommand=self.parent.scroll.set)
                home.bind(
                    "<Configure>",
                    lambda e: self.parent.configure(
                        scrollregion=self.parent.bbox("all")
                    )
                )
                self.destroy()
            else:
                self.message_label.configure(text= "Contraseña incorrecta")
        else:
            self.message_label.configure(text= "Usuario no existente")
