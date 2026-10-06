    #MATRIZ
m = [[1, 3], [5, 6]]
print(m[0][0])  #acessa o elemento da primeira linha e primeira coluna
print(m[0][1])  #acessa o elemento da primeira linha e segunda coluna
print(m[1][0])  #acessa o elemento da segunda linha e primeira coluna
print(m[1][1])  #acessa o elemento da segunda linha e segunda coluna
for linha in range(len(m)):
    for coluna in range(len(m[linha])):
        print(m[linha][coluna])  #acessa todos os elementos da matriz



#continuando o programa, fazendo a soma de duas matrizes
m = [[1, 3], [5, 6]]
n = [[6, 7], [8, 9]]
s = [[0 for i in range(len(m))] for j in range(len(m))] #ou [[0, 0], [0, 0]]   #cria uma matriz de zeros com o mesmo tamanho das matrizes m e n
for linha in range(len(m)):
    for coluna in range(len(m[linha])):
        s[linha][coluna] = m[linha][coluna] + n[linha][coluna]
        print(s[linha][coluna], end=" ")  #acessa todos os elementos da matriz e soma com a outra matriz
        print(np.array(s))  #transforma a matriz s em um array numpy e imprime na tela    #arrumar essa linha, ta errada
      
    #print()  #quebra de linha para separar as linhas da matriz