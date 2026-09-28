def matriz_tabuleiro(lin, col, sim):
    matriz = []
    line = []

    for m in range(0,3):
        for l in range(0,3):
            line.append(' ')
        matriz.append(line[:])
        line.clear()

    while True:
        for x in range(0,3):
            for y in range(0,3):
                print(f'| {matriz[x][y]} |', end='')
            print()
        matriz[lin][col] = sim

        break

def sistema_preenchimento():                

# def sistema_validacao()
