import tkinter as tk
from tkinter import messagebox as tmsg
import time


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

    # time display
    def display(self):
        self.var = tk.StringVar()
        self.var.set("00:00:00")
        frm = tk.Frame(self, relief="sunken", border=2, bg="white")
        frm.pack(fill="x", padx=10, pady=10, ipadx=5, ipady=5)
        a = tk.Label(frm, textvariable=self.var,
                     font="serif 18 bold", bg="white", fg="black")
        a.pack()

    # display buttons
    def start_stop(self):
        frm = tk.Frame(self)
        frm.pack(fill="x")
        bstart = tk.Button(frm, text="start", bg="grey", fg="white",
                           relief="sunken", borderwidth=2,
                           font="lucida 15 bold")
        bstart.pack(side="left", anchor="n", padx=10, pady=10)
        bstop = tk.Button(frm, text="stop", bg="grey", fg="white",
                          relief="sunken", borderwidth=2,
                          font="lucida 15 bold")
        bstop.pack(side="right", anchor="n", padx=10, pady=10)

    def statusbar(self):
        self.var = tk.StringVar()
        self.var.set("Welcome")
        # add sperator
        tk.Frame(self).pack(fill="x")
        frm = tk.Frame(self)
        frm.pack(side="bottom", fill="x")
        sbar = tk.Label(self, textvariable=self.var,
                        relief="sunken", anchor="w")
        sbar.pack(side="bottom", fill="x")


if __name__ == "__main__":
    app = gui()
    app.menubar()
    app.display()
    app.start_stop()
    app.statusbar()
    app.mainloop()
