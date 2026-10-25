import tkinter
from tkinter import *
from tkinter import ttk
import random
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from config.cores import CO0, CO1, CO4, CO7, FUNDO
from config.sons import music_ganhador, botoes_music,musica


def iniciar_jogo(down_frame, label_o_placar, label_x_placar):
    musica()

    player_1 = "X"
    player_2 = "O"

    point_player_1 = 0
    point_player_2 = 0

    jogando = ''
    contador = 0

    estado_tabuleiro = ['' for _ in range(9)]

    if jogando == '':
        jogando = random.choice([player_1, player_2])

    print(jogando)

    #Controle do gamer
    def controle(i, btn):
        global controlar
        nonlocal contador
        global jogar
        nonlocal jogando


 
        if btn['text'] == '' or btn['text'] == ' ':

            botoes_music()
            

            if jogando == 'X':
                cor = CO7
            if jogando == 'O':
                cor = CO4

            btn['text'] = jogando
            btn['fg'] = cor

            ind = int(i)-1
            estado_tabuleiro[ind] = jogando
            contador+=1

            if contador >=5:
                print('chegou a cinco')
                ganhador = vencedor()
                print(f'ganhador: {ganhador}')
                if ganhador:
                    print('pontuado')
                    music_ganhador()
                    terminar()
            if contador > 8:
                print('JOGO FINALIZADO')
                terminar()


        if jogando == 'X':
            jogando = 'O'
        else:
            jogando = 'X'

    
    #Decdir o vencedor
    def vencedor():
        nonlocal point_player_1, point_player_2
        combinacoes_vencedoras = [
            (0,1,2), (3,4,5), (6,7,8), #Linhas
            (0,3,6), (1,4,7), (2,5,8), #Colunas
            (0,4,8), (2,4,6) #Diagonais
        ]

        for a, b, c in combinacoes_vencedoras:
            if estado_tabuleiro[a] != '' and  estado_tabuleiro[a] == estado_tabuleiro[b] == estado_tabuleiro[c]:
                if estado_tabuleiro[a] == player_1:
                    point_player_1+=1
                    label_x_placar.config(text=str(point_player_1))
                else:
                    point_player_2+=1
                    label_o_placar.config(text=str(point_player_2))

                return estado_tabuleiro[a]

        return None

    def terminar():
        nonlocal contador, jogando, estado_tabuleiro

        contador=0
        jogando= jogando = random.choice([player_1, player_2])

        estado_tabuleiro = ['' for _ in range(9)]

        botoes = [btn_0, btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8]

        for btn in botoes:
            btn['text'] = ' '
            btn['fg'] = FUNDO
        

    # Tabuleiro do Jogo -------------------------------------------------------------------------------------------------
    
    # Colunas

    label_col = Label(down_frame, text="", height=23, relief='flat', pady=5, anchor="center", font=("Ivy 5 bold"), bg=CO0, fg=CO7)
    label_col.place(x=90, y=15)
    label_col = Label(down_frame, text="", height=23, relief='flat', pady=5, anchor="center", font=("Ivy 5 bold"), bg=CO0, fg=CO7)
    label_col.place(x=160, y=15)

    # Linhas

    label_rows = Label(down_frame, text=" ", width=190, relief='flat', padx=2, pady=1, anchor="center", font=("Ivy 1 bold"), bg=CO0, fg=CO7)
    label_rows.place(x=30, y=63)
    label_rows = Label(down_frame, text=" ", width=190, relief='flat', padx=2, pady=1, anchor="center", font=("Ivy 1 bold"), bg=CO0, fg=CO7)
    label_rows.place(x=30, y=130)

    #btn Linha 01
    btn_0 = Button(down_frame,command=lambda:controle('1', btn_0), text=" ", width=3, font=("Ivy 19 bold"), relief='flat' , overrelief=RIDGE ,bg=FUNDO, fg=CO7)
    btn_0.place(x=34, y=10)
    btn_1 = Button(down_frame,command=lambda:controle('2',btn_1), text=" ", width=3, font=("Ivy 20 bold"), relief='flat' , overrelief=RIDGE ,bg=FUNDO, fg=CO7)
    btn_1.place(x=98, y=7)
    btn_2 = Button(down_frame,command=lambda:controle('3', btn_2), text=" ", width=3, font=("Ivy 19 bold"), relief='flat' , overrelief=RIDGE ,bg=FUNDO, fg=CO7)
    btn_2.place(x=168, y=10)

    #btn Linha 02
    btn_3 = Button(down_frame,command=lambda:controle('4', btn_3), text=" ", width=3, font=("Ivy 19 bold"), relief='flat' , overrelief=RIDGE ,bg=FUNDO, fg=CO7)
    btn_3.place(x=34, y=75)
    btn_4 = Button(down_frame,command=lambda:controle('5', btn_4), text=" ", width=3, font=("Ivy 20 bold"), relief='flat' , overrelief=RIDGE ,bg=FUNDO, fg=CO7)
    btn_4.place(x=98, y=74)
    btn_5 = Button(down_frame,command=lambda:controle('6', btn_5), text=" ", width=3, font=("Ivy 19 bold"), relief='flat' , overrelief=RIDGE ,bg=FUNDO, fg=CO7)
    btn_5.place(x=168, y=75)

    #btn Linha 02
    btn_6 = Button(down_frame,command=lambda:controle('7', btn_6), text=" ", width=3, font=("Ivy 19 bold"), relief='flat' , overrelief=RIDGE ,bg=FUNDO, fg=CO7)
    btn_6.place(x=34, y=140)
    btn_7 = Button(down_frame,command=lambda:controle('8', btn_7), text=" ", width=3, font=("Ivy 20 bold"), relief='flat' , overrelief=RIDGE ,bg=FUNDO, fg=CO7)
    btn_7.place(x=98, y=139)
    btn_8 = Button(down_frame,command=lambda:controle('9', btn_8), text=" ", width=3, font=("Ivy 19 bold"), relief='flat' , overrelief=RIDGE ,bg=FUNDO, fg=CO7)
    btn_8.place(x=168, y=140)