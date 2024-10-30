import tkinter as tk
from tkinter import messagebox as tmsg
import time


class gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.minsize(300, 300)
        self.maxsize(900, 900)
        self.title("Pomodoro app")

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
        self.dvar = tk.StringVar()
        self.dvar.set(time.strftime("%H:%M:%S", time.gmtime(0)))
        frm = tk.Frame(self, relief="sunken", border=2, bg="white")
        frm.pack(fill="x", padx=10, pady=10, ipadx=5, ipady=5)
        a = tk.Label(frm, textvariable=self.dvar,
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
        self.tvar = 0
        self.bvar = 0
        self.svar = tk.StringVar()
        self.svar.set("Welcome")
        # add sperator
        tk.Frame(self).pack(fill="x")
        frm = tk.Frame(self)
        frm.pack(side="bottom", fill="x")
        sbar = tk.Label(self, textvariable=self.svar,
                        relief="sunken", anchor="w")
        sbar.pack(side="bottom", fill="x")

    # for starting

    def changesbar(self, cond):
        if cond == "break":
            self.bvar += 1
        else:
            self.tvar += 1
        self.svar.set(f"Pomos : {self.tvar} Breaks : {self.bvar}")

    def changetime(self, secs):
        self.dvar.set(time.strftime("%H:%M:%S", time.gmtime(secs)))

    def takeinputs(self):
        self.frm1 = tk.Frame(self)
        self.frm1.pack(fill="x")
        timeslider = tk.Scale(self.frm1, from_=0, to=120,
                              orient="horizontal", tickinterval=60)
        timeslider.pack(side="right")
        timemsg = tk.Label(self.frm1, text="Pomo time : ")
        timemsg.pack(side="left")
        self.frm2 = tk.Frame(self)
        self.frm2.pack(fill="x")
        breakslider = tk.Scale(self.frm2, from_=0, to=30,
                               orient="horizontal", tickinterval=10)
        breakslider.pack(side="right")
        breakmsg = tk.Label(self.frm2, text="Break time : ")
        breakmsg.pack(side="left")


if __name__ == "__main__":
    app = gui()
    app.menubar()
    app.display()
    app.takeinputs()
    # app.start_stop()
    app.statusbar()
    # app.changesbar()
    app.mainloop()
