from tkinter import Tk, Canvas, Menu,Scrollbar, RIGHT, Y, Frame
from frames.Login import Login

def center(toplevel):
       toplevel.update_idletasks()
       w = toplevel.winfo_screenwidth()
       h = toplevel.winfo_screenheight()
       size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
       x = w/2 - size[0]/2
       y = h/2 - size[1]/2
       toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

def main():
    root = Tk()
    root.title("COVID-19")
    root.geometry('820x500')
    center(root)
    

    container = Frame(root)
    canvas = Canvas(container, height = 500, width=800)
    scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
    login = Login(canvas)

    login.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.scroll = scrollbar
    canvas.create_window((0, 0), window=login, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    container.pack()
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    root.mainloop()

if __name__ == "__main__":
    main()
