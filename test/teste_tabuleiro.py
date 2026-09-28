lin = 0
col = 0
sim = 'X'
matriz = []
line = []

for m in range(0,3):
    for l in range(0,3):
        line.append(' ')
    matriz.append(line[:])
    line.clear()

while True:
    matriz[lin][col] = sim
    for x in range(0,3):
        for y in range(0,3):
            print(f'| {matriz[x][y]} |', end='')
        print()
    break