def imprime_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end = "")
            if j != len(matriz[i]) - 1:
                print(end = " ")
        print()
