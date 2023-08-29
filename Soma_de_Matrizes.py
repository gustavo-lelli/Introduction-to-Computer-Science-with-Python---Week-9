def gerar_matriz (n_linhas, n_colunas):
        matriz = []
        for i in range(n_linhas):
            linha = []
            for j in range(n_colunas):
                linha.append(0)
            matriz.append(linha)

        return matriz

def soma_matrizes(m1, m2):
    if len(m1) == len(m2) and len(m1[0]) == len(m2[0]):
        m3 = gerar_matriz(len(m1), len(m1[0]))
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                m3[i][j] = m1[i][j] + m2[i][j]
        
        return m3

    else:
        return False
