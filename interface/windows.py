import tkinter
from tkinter import *
from tkinter import ttk

co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black


def windonw():
    win = Tk()
    win.title('')
    win.geometry('260x340')
    win.configure(bg=fundo)

    frame_result = Frame(win,width=240, height=100, bg=co1,relief="raised" )#PROCURAR SABER O QYUE EH REIEF
    frame_result.grid(row=1, column=0,sticky=NW, padx=10, pady=10)

    win.mainloop()

windonw()