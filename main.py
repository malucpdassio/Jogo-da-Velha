import tkinter
from tkinter import *
from tkinter import ttk
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from interface.janela import windonw
from config.sons import musica

def main():
    co1 = "#333333"
    fundo = "#3b3b3b" # preta / black

    win = Tk()
    win.title('')
    win.geometry('260x370')
    win.configure(bg=fundo)

    musica()

    # Dividindo os Frames: 1_frame = Placar e 2_frame= jogo-----------------------------------
    up_frame = Frame(win,width=240, height=100, bg=co1,relief="raised" )#PROCURAR SABER O QYUE EH REIEF
    up_frame.grid(row=0, column=0,sticky=NW, padx=10, pady=10)

    down_frame = Frame(win, width=240, height=300, bg=fundo, relief="flat")
    down_frame.grid(row=1, column=0, sticky=NW)

    windonw(up_frame, down_frame)

    #Criar BOTOES   
    win.mainloop()

if __name__ == '__main__':
    main()