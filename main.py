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
        self.resetter = False
        self.bigfont_cond = "start"

    def resetting_process(self):
        self.resetter = True

    def menubar(self):
        mainmenu = tk.Menu(self)

        # timer option
        m1 = tk.Menu(mainmenu, tearoff=0)
        m1.add_command(label="reset", command=self.resetting_process)
        # m1.add_command(label="stop")
        mainmenu.add_cascade(label="timer", menu=m1)

        # info option
        m2 = tk.Menu(mainmenu, tearoff=0)
        m2.add_command(label="about")
        mainmenu.add_cascade(label="about", menu=m2)

        # exit
        def quitapp():
            a = tmsg.askyesno("Quit", "Do you want to quit the application ?")
            if a:
                self.resetter = True
                self.disp.destroy()
                self.destroy()

        mainmenu.add_command(label="quit", command=quitapp)
        self.config(menu=mainmenu)

    # time display
    def display(self):
        self.dvar = tk.StringVar()
        self.dvar.set(time.strftime("%H:%M:%S", time.gmtime(0)))
        frm = tk.Frame(self, relief="sunken", border=2, bg="white")
        frm.pack(fill="x", padx=10, pady=10, ipadx=5, ipady=5)
        self.disp = tk.Label(frm, textvariable=self.dvar,
                             font="serif 18 bold", bg="white", fg="black")
        self.disp.pack()

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

    def start_timer(self):
        self.svar.set(f"Pomos : {self.tvar} Breaks : {self.bvar}")
        while True:
            self.bigfont_cond = "no_break"
            self.bigfont_update()
            for i in range(self.counttime*60):
                self.dvar.set(time.strftime("%H:%M:%S", time.gmtime(i)))
                self.disp.update()
                if self.resetter is True:
                    self.dvar.set(time.strftime("%H:%M:%S", time.gmtime(0)))
                    self.disp.update()
                    break
                time.sleep(1)
            self.changesbar("time")
            if self.resetter is True:
                break
            repeater = tmsg.askyesno(
                "Time Over", "Time is over. Do you want break ?")
            if repeater is True:
                self.bigfont_cond = "break"
                self.bigfont_update()
                for i in range(self.countbreak*60):
                    self.dvar.set(time.strftime(
                        "%H:%M:%S", time.gmtime(i)))
                    self.disp.update()
                    time.sleep(1)
                    if self.resetter is True:
                        self.dvar.set(time.strftime(
                            "%H:%M:%S", time.gmtime(0)))
                        self.disp.update()
                        break
                self.changesbar("break")
            if self.resetter is True:
                break
            tmsg.askyesno(
                "Break Over", "Break is over")

    def the_main_process(self):

        def ignite():
            self.counttime = timeslider.get()
            self.countbreak = breakslider.get()
            self.frm1.destroy()
            self.frm2.destroy()
            self.frm3.destroy()
            self.bigfont_create()
            self.start_timer()

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
        self.frm3 = tk.Frame(self, bg="red")
        self.frm3.pack()
        but1 = tk.Button(self.frm3, relief="sunken", border=5,
                         text="start", command=ignite)
        but1.pack()

    def bigfont_create(self):
        self.bigfont_var = tk.StringVar()
        self.bigfntframe = tk.Frame(self)
        self.bigfntframe.pack(fill="x")
        self.bigfont_display = tk.Label(self.bigfntframe,
                                        textvariable=self.bigfont_var,
                                        font="cursive 30 bold")
        self.bigfont_display.pack(fill="x")
        self.bigfont_var.set("Keep going...")
        self.bigfntframe.update()

    def bigfont_update(self):
        if self.bigfont_cond == "break":
            self.bigfont_var.set("Break")
        else:
            self.bigfont_var.set("Keep going...")


if __name__ == "__main__":
    app = gui()
    app.menubar()
    app.display()
    app.the_main_process()
    # app.start_stop()
    app.statusbar()
    # app.changesbar()
    app.mainloop()
