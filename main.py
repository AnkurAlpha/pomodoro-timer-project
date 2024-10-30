import tkinter as tk
from tkinter import messagebox as tmsg


class gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.minsize(300, 300)
        self.maxsize(900, 900)

    def menubar(self):
        mainmenu = tk.Menu(self)

        # timer option
        m1 = tk.Menu(mainmenu, tearoff=0)
        m1.add_command(label="start")
        m1.add_command(label="stop")
        mainmenu.add_cascade(label="timer", menu=m1)

        # info option
        m2 = tk.Menu(mainmenu, tearoff=0)
        m2.add_command(label="about")
        mainmenu.add_cascade(label="about", menu=m2)

        # exit
        def quitapp():
            a = tmsg.askyesno("Quit", "Do you want to quit the application ?")
            if a:
                self.destroy()

        mainmenu.add_command(label="quit", command=quitapp)
        self.config(menu=mainmenu)


if __name__ == "__main__":
    app = gui()
    app.menubar()
    app.mainloop()
