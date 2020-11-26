def contar_rutas_mas_cortas(C):
    m = auxiliar(C,1,2)
    if m==[]:
        return []
    else: 
        for i in range(0, len(m)):
            for j in range (0, len(m[0])):
                if matriz[i][j] == 'T':
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 0
    return matriz
