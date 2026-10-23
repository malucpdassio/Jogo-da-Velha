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
    win.geometry('260x370')
    win.configure(bg=fundo)


    # Dividindo os Frames: 1_frame = Placar e 2_frame= jogo-----------------------------------
    up_frame = Frame(win,width=240, height=100, bg=co1,relief="raised" )#PROCURAR SABER O QYUE EH REIEF
    up_frame.grid(row=0, column=0,sticky=NW, padx=10, pady=10)

    down_frame = Frame(win, width=240, height=300, bg=fundo, relief="flat")
    down_frame.grid(row=1, column=0, sticky=NW)


    # Placar do Jogo -------------------------------------------------------------------------------------------------
    app_x = Label(up_frame, text="X", height=1, relief="flat", anchor="center", font=("Ivy 40 bold"), bg=co1, fg=co7)
    app_x.place(x=25, y=10)

    label_app_x = Label(up_frame, text="Player 1", height=1, relief="flat", anchor="center", font=("Ivy 40 bold", 9, "bold"), bg=co1, fg=co0)
    label_app_x.place(x=18, y=70)

    label_x_placar = Label(up_frame, text="0", height=1, relief="flat", anchor="center", font=("Ivy 30 bold"), bg=co1, fg=co0)
    label_x_placar.place(x=80, y=20)

    divisao = Label(up_frame, text=":", height=1, relief="flat", anchor="center", font=("Ivy 40 bold"), bg=co1, fg=co0)
    divisao.place(x=108, y=10)


    app_o = Label(up_frame, text="O", height=1, relief="flat", anchor="center", font=("Ivy 40 bold"), bg=co1, fg=co4)
    app_o.place(x=170, y=10)

    label_app_o = Label(up_frame, text="Player 2", height=1, relief="flat", anchor="center", font=("Ivy 40 bold", 9, "bold"), bg=co1, fg=co0)
    label_app_o.place(x=168, y=70)

    label_o_placar = Label(up_frame, text="0", height=1, relief="flat", anchor="center", font=("Ivy 30 bold"), bg=co1, fg=co0)
    label_o_placar.place(x=130, y=20)

    # Tabuleiro do Jogo -------------------------------------------------------------------------------------------------

    # Colunas

    label_col = Label(down_frame, text="", height=23, relief='flat', pady=5, anchor="center", font=("Ivy 5 bold"), bg=co0, fg=co7)
    label_col.place(x=90, y=15)
    label_col = Label(down_frame, text="", height=23, relief='flat', pady=5, anchor="center", font=("Ivy 5 bold"), bg=co0, fg=co7)
    label_col.place(x=160, y=15)

    # Linhas

    label_rows = Label(down_frame, text=" ", width=190, relief='flat', padx=2, pady=1, anchor="center", font=("Ivy 1 bold"), bg=co0, fg=co7)
    label_rows.place(x=30, y=63)
    label_rows = Label(down_frame, text=" ", width=190, relief='flat', padx=2, pady=1, anchor="center", font=("Ivy 1 bold"), bg=co0, fg=co7)
    label_rows.place(x=30, y=123)

    #Criar BOTOES
    win.mainloop()

windonw()