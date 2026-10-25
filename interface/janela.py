import tkinter
from tkinter import *
from tkinter import ttk
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from core.jogo import iniciar_jogo
from config.sons import botoes_music, musica
from config.cores import CO0,CO4, CO1, CO7




def windonw(up_frame, down_frame):

    musica()

    # Placar do Jogo -------------------------------------------------------------------------------------------------
    app_x = Label(up_frame, text="X", height=1, relief="flat", anchor="center", font=("Ivy 40 bold"), bg=CO1, fg=CO7)
    app_x.place(x=25, y=10)

    label_app_x = Label(up_frame, text="Player 1", height=1, relief="flat", anchor="center", font=("Ivy 40 bold", 9, "bold"), bg=CO1, fg=CO0)
    label_app_x.place(x=18, y=70)

    label_x_placar = Label(up_frame, text="0", height=1, relief="flat", anchor="center", font=("Ivy 30 bold"), bg=CO1, fg=CO0)
    label_x_placar.place(x=80, y=20)

    divisao = Label(up_frame, text=":", height=1, relief="flat", anchor="center", font=("Ivy 40 bold"), bg=CO1, fg=CO0)
    divisao.place(x=108, y=10)


    app_o = Label(up_frame, text="O", height=1, relief="flat", anchor="center", font=("Ivy 40 bold"), bg=CO1, fg=CO4)
    app_o.place(x=170, y=10)

    label_app_o = Label(up_frame, text="Player 2", height=1, relief="flat", anchor="center", font=("Ivy 40 bold", 9, "bold"), bg=CO1, fg=CO0)
    label_app_o.place(x=168, y=70)

    label_o_placar = Label(up_frame, text="0", height=1, relief="flat", anchor="center", font=("Ivy 30 bold"), bg=CO1, fg=CO0)
    label_o_placar.place(x=130, y=20)

    label_jogar = Button(down_frame, command=lambda:[botoes_music(), iniciar_jogo(down_frame, label_o_placar,label_x_placar)],text="JOGAR", relief="flat", anchor="center", font=("Ivy 10 bold"), overrelief=RIDGE ,bg=CO1, fg=CO0)
    label_jogar.place(x=98, y=210)

