import pygame
from pygame.locals import *
from tkinter import *
from tkinter import messagebox
import webbrowser
from PIL import Image, ImageTk


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'


class UI():

    def __init__(self, data=[]):
        self.data = data
        while len(self.data) != 0:
            self.data.pop(0)
        self.root = Tk()
        self.root.geometry('480x570+720+255')
        self.root.title("ElementalDungeon")
        self.root.resizable(0, 0)
        self.sprites = []
        self.dontclick = 0
        self.soundstatus = 1
        self.screensize = 1

        iconphoto = ImageTk.PhotoImage(Image.open(
            "src/photo/monster2.png").resize((50, 50), Image.LANCZOS))
        self.root.iconphoto(False, iconphoto)

        self.soundimg = []
        soundoff = Image.open("src/photo/soundoff.png")
        self.soundimg.append(ImageTk.PhotoImage(
            soundoff.resize((40, 40), Image.LANCZOS)))
        soundon = Image.open("src/photo/soundon.png")
        self.soundimg.append(ImageTk.PhotoImage(
            soundon.resize((40, 40), Image.LANCZOS)))

        self.checkboximg = ImageTk.PhotoImage(Image.open(
            "src/photo/checkbox.png").copy().resize((50, 50), Image.LANCZOS))
        self.checkimg = ImageTk.PhotoImage(Image.open(
            "src/photo/check.png").copy().resize((30, 30), Image.LANCZOS))

        self.bgimg = ImageTk.PhotoImage(Image.open(
            "src/map/bgui2.png").resize((480, 720), Image.LANCZOS))
        self.monsterimg = ImageTk.PhotoImage(Image.open(
            "src/photo/monster1.png").resize((158, 100), Image.LANCZOS))
        self.root.bind("<Key>", self.key_pressed)

    def menu(self):
        Label(self.root, image=self.bgimg).place(
            x=-2, y=-2)
        self.BSound = Button(self.root, image=self.soundimg[self.soundstatus], bg=_from_rgb((76, 63, 59)), font=(
            "bold", 10), command=self.changeSoundStatus, borderwidth=0, activebackground=_from_rgb((76, 63, 59)))
        self.BSound.place(x=425, y=510)
        self.BDoNot = Button(self.root, text="Don't Click!", width=14, height=2, bg=_from_rgb((165, 121, 103)), font=(
            "", 20), command=self.dont)
        self.BDoNot.place(x=120, y=80)
        self.BPlay = Button(self.root, text="play", width=25, height=3, bg=_from_rgb((165, 121, 103)), font=(
            "", 10), command=self.play)
        self.BPlay.place(x=130, y=240)
        self.BSetting = Button(self.root, text="setting", width=25, height=3, bg=_from_rgb((165, 121, 103)), font=(
            "", 10), command=self.setting)
        self.BSetting.place(x=130, y=320)
        self.BCredit = Button(self.root, text="credit", width=25, height=3, bg=_from_rgb((165, 121, 103)), font=(
            "", 10), command=self.open_browser)
        self.BCredit.place(x=130, y=400)
        self.BQuit = Button(self.root, text="quit", width=25, height=3, bg=_from_rgb((165, 121, 103)), font=(
            "", 10), command=self.root.quit)
        self.BQuit.place(x=130, y=480)

    def setting(self):
        canvas = Canvas(self.root, height=600, width=1000,
                        bg=_from_rgb((76, 63, 59)))
        canvas.place(x=-2, y=-2)

        Bback = Button(self.root, text=" <- back ", bg=_from_rgb((76, 63, 59)), font=(
            "bold", 10), fg=_from_rgb((165, 121, 103)), command=self.menu, borderwidth=0)
        Bback.place(x=10, y=10)
        self.screentext = Label(self.root, text="Screen Size", font=(
            "bold", 35), fg=_from_rgb((165, 121, 103)), bg=_from_rgb((76, 63, 59)))
        self.screentext.place(x=110, y=50)
        self.small = Label(self.root, text="1280 x  720", font=(
            "bold", 30), fg=_from_rgb((165, 121, 103)), bg=_from_rgb((76, 63, 59)))
        self.small.place(x=180, y=150)
        self.Bsmall = Button(self.root, image=self.checkboximg, bg=_from_rgb((76, 63, 59)),
                             borderwidth=0, activebackground=_from_rgb((76, 63, 59)), command=lambda: self.change_screensize(0))
        self.Bsmall.place(x=100, y=150)

        self.normal = Label(self.root, text="1536 x  864", font=(
            "bold", 30), fg=_from_rgb((165, 121, 103)), bg=_from_rgb((76, 63, 59)))
        self.normal.place(x=180, y=230)
        self.Bnormal = Button(self.root, image=self.checkboximg, bg=_from_rgb((76, 63, 59)),
                              borderwidth=0, activebackground=_from_rgb((76, 63, 59)), command=lambda: self.change_screensize(1))
        self.Bnormal.place(x=100, y=230)

        self.big = Label(self.root, text="1920 x 1080", font=(
            "bold", 30), fg=_from_rgb((165, 121, 103)), bg=_from_rgb((76, 63, 59)))
        self.big.place(x=180, y=310)
        self.Bbig = Button(self.root, image=self.checkboximg, bg=_from_rgb((76, 63, 59)),
                           borderwidth=0, activebackground=_from_rgb((76, 63, 59)), command=lambda: self.change_screensize(2))
        self.Bbig.place(x=100, y=310)

        self.big2k = Label(self.root, text="2560 x 1440", font=(
            "bold", 30), fg=_from_rgb((165, 121, 103)), bg=_from_rgb((76, 63, 59)))
        self.big2k.place(x=180, y=390)
        self.Bbig2k = Button(self.root, image=self.checkboximg, bg=_from_rgb((76, 63, 59)),
                             borderwidth=0, activebackground=_from_rgb((76, 63, 59)), command=lambda: self.change_screensize(3))
        self.Bbig2k.place(x=100, y=390)

        self.check = Label(self.root, image=self.checkimg,
                           bg=_from_rgb((76, 63, 59)))
        self.check.place(x=110, y=160+80*self.screensize)

        self.monster = Label(self.root, image=self.monsterimg,
                             bg=_from_rgb((76, 63, 59)))
        self.monster.place(x=170, y=450)

    def play(self, fail=False):
        canvas = Canvas(self.root, height=600, width=1000,
                        bg=_from_rgb((76, 63, 59)))
        canvas.place(x=-2, y=-2)

        Bback = Button(self.root, text=" <- back ", bg=_from_rgb((76, 63, 59)), font=(
            "bold", 10), fg=_from_rgb((165, 121, 103)), command=self.menu, borderwidth=0)
        Bback.place(x=10, y=10)

        self.inputusername = Label(self.root, text="Username:", font=(
            "bold", 12), fg=_from_rgb((165, 121, 103)), bg=_from_rgb((76, 63, 59)))
        self.inputusername.place(x=100, y=100)
        self.entry_username = Entry(self.root, width=45)
        self.entry_username.place(x=100, y=130)
        self.inputusername = Label(self.root, text="Password:", font=(
            "bold", 12), fg=_from_rgb((165, 121, 103)), bg=_from_rgb((76, 63, 59)))
        self.inputusername.place(x=100, y=180)
        self.entry_password = Entry(self.root, width=45, show="*")
        self.entry_password.place(x=100, y=210)

        if not fail:
            self.warning1 = Label(
                self.root, text="the length of username must less than eight", font=("", 10), fg='red', bg=_from_rgb((76, 63, 59)))
            self.warning1.place(x=100, y=260)
            self.warning2 = Label(
                self.root, text="and username can't be empty.", font=("", 10), fg='red', bg=_from_rgb((76, 63, 59)))
            self.warning2.place(x=100, y=280)
        else:
            self.warning1 = Label(
                self.root, text="username or password is incorrect, please try", font=("", 10), fg='red', bg=_from_rgb((76, 63, 59)))
            self.warning1.place(x=100, y=260)
            self.warning2 = Label(
                self.root, text="again with another password.", font=("", 10), fg='red', bg=_from_rgb((76, 63, 59)))
            self.warning2.place(x=100, y=280)

        self.BCheck = Button(self.root, text="Login To Game",
                             command=self.get, width=39, height=3, bg=_from_rgb((165, 121, 103)))
        self.BCheck.place(x=100, y=360)

    def get(self):
        self.data.append(self.entry_username.get())
        self.data.append(self.entry_password.get())
        self.data.append(self.soundstatus)
        self.entry_password.delete(0, END)
        if self.data[0] == "" or len(self.data[0]) >= 8:
            self.warning1.config(
                text="the length of username must less than eight")
            self.warning2.config(text="and username can't be empty.")
            while len(self.data) != 0:
                self.data.pop(0)
            return

        self.root.withdraw()
        self.root.quit()

    def show(self, login):
        self.root.deiconify()
        pygame.mixer.init()
        pygame.mixer.music.load('sound.mp3')
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.2)
        while len(self.data) != 0:
            self.data.pop(0)
        if login:
            self.menu()
        else:
            self.play(True)
        self.root.mainloop()

    def key_pressed(self, event):
        if event.keysym == "Escape":
            self.menu()

    def change_screensize(self, val):
        messagebox.showerror(
            "warning", "Sorry changing screen size is not supported yet")

    def open_browser(self):
        webbrowser.open("https://github.com/jiratQ/ElementalDungeon")

    def changeSoundStatus(self):
        self.soundstatus = 1 - self.soundstatus
        self.BSound.configure(image=self.soundimg[self.soundstatus])
        if self.soundstatus == 0:
            pygame.mixer.music.set_volume(0)
        else:
            pygame.mixer.music.set_volume(0.2)

    def dont(self):
        self.dontclick += 1
        if messagebox.askquestion(title="Don't Click!", message="Sure?") == "yes":
            if self.dontclick >= 30:
                webbrowser.open("https://www.youtube.com/watch?v=q3TdXGFI3wc")
                self.dontclick = 0
            else:
                self.dont()
