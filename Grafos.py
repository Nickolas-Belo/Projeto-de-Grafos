import os.path

# O usuário deve entrar com o nome do arquivo ".txt" que contém a matriz.
# O arquivo ".txt" deve estar no mesmo diretório do arquivo ".py".

nome_arq = input("Digite o nome do arquivo que contém a matriz: ").replace(".txt", "")
while os.path.isfile("%s.txt" % nome_arq) == False:
    print("O arquivo não foi encontrado!")
    nome_arq = input("Digite o nome do arquivo que contém a matriz: ").replace(".txt", "")
print()

# Criando uma lista para armazenar os valores do arquivo:
matriz = []
matriz_arq = open("%s.txt" % nome_arq, "r")
for i in matriz_arq.readlines():
    matriz_separada = i.strip().split(" ")
    matriz.append(matriz_separada)
matriz_arq.close()

# Convertendo os valores da lista para números inteiros:
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(matriz[i][j])
        
# Imprimindo a matriz:
def ImprimeMatriz():
    print(" Matriz Adjacência:\n===================")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print("[%2.d]" % matriz[i][j], end = " ")
        print()
    print("===================")

# Condições para o grafo ser simples ou completo: A príncipio as variáveis simples e completo terão valor = 1.
# Caso uma das condições que tornam o grafo não simples ou não completo seja verdadeira, a variável passa a valer 0.

simples = 1
completo = 1

# 1º) Verificar se o grafo é simples:
def VerificaSimples(simples): # Função que retorna se o grafo é simples ou não:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            if i == j: # Caso i == j (linha igual a coluna):
                if matriz[i][j] == 0: # Se o valor for igual a 0, a variável simples não é alterada.
                    continue

                else: # Se o valor for diferente de 0, o grafo possui um laço, então a variável simples passa a valer 0.
                    simples = 0 

            elif i != j: # Caso i != j (linha diferente de coluna):
                # Se o valor for menor que 2, a variável simples não é alterada.
                if matriz[i][j] < 2:
                    continue
                # Se o valor for maior ou igual a 2, o grafo possui arestas múltiplas, então a variável simples passa a valer 0.
                else:
                    simples = 0
                    
    if simples == 0: # Imprime se o grafo é ou não simples:
        print("Não é grafo simples")
    else:
        print("É um grafo simples")
    return simples

# 2º) Verificar se o grafo é completo:
def VerificaCompleto(completo): # Função que retorna se o grafo é completo ou não:
    if simples == 1: # Se a variável simples tem valor igual a 1, então o grafo não possui laços ou arestas múltiplas.
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):

                if i != j: # Caso i != j (linha diferente de coluna):
                    # Se o valor for igual a 1, há uma aresta ligando os vértices e a variável completo não é alterada.
                    if matriz[i][j] == 1:
                        continue
                    # Se o valor for diferente de 0, não há aresta conectando os vértices, então a variável completo passa a valer 0.
                    else:
                        completo = 0

    else: # Se o grafo não é simples, então a variável completo passa a valer 0.
        completo = 0
    if completo == 0: # Imprime se o grafo é ou não completo:
        print("Não é grafo completo")
    else:
        print("É um grafo completo")
    return completo

# 3º) Verificando em quais vértices há arestas múltiplas ou laços e a quantidade de arestas:
def VerificaArestas(simples, completo): # Função que retorna o número de arestas do grafo:
    print("===================")
    print("Arestas Múltiplas / Laços:\n")
    arestas = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            if i != j: # Caso i != j (linha diferente de coluna):
                if matriz[i][j] == 1: # Se o valor for igual a 1...
                    arestas += matriz[i][j] # É somada uma unidade à variável arestas.

                elif matriz[i][j] > 1: # Se o valor for maior que 1, então o grafo possui arestas múltiplas.
                    if j > i: # Uma mensagem é exibida indicando os vértices que possuem arestas múltiplas.
                        print("V%dV%d / V%dV%d possui arestas múltiplas" % (i + 1, j + 1, j + 1, i + 1)) 
                    arestas += matriz[i][j] # É somada a quantidade de arestas entre os vértices à variável arestas.

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):

            if i == j: # Caso i == j (linha igual a coluna):
                if matriz[i][j] == 1: # Se o valor for igual a 1, então o grafo possui laços.
                    # Uma mensagem é exibida indicando os vértices que possuem laços.
                    print("V%d possui um laço" % (i + 1))
                    arestas += matriz[i][j] * 2 # Sâo somadas duas unidades à variável arestas.

    if simples == 1: # Se o grafo é simples, logo não possui arestas múltiplas / laços:
        print("O grafo não possui arestas múltiplas / laços")
    print()

    # Como cada aresta aparece duas vezes na matriz, com exceção dos laços (que são somados duas vezes),
    # Somamos todas as dividimos o resultado por 2:
    arestas = arestas / 2
    
    print("O grafo possui %d arestas" % round(arestas))
    return arestas

# 4º) Sequência de graus:
def VerificaGrau(): # Função que retorna o número de arestas do grafo:
    print("===================")
    print("Graus dos Vértices:\n")
    grau = []
    for i in range(len(matriz)):
        grau.append(0)
        for j in range(len(matriz[i])):
            if i == j: # Caso i == j (linha igual a coluna):
                grau[i] += (matriz[i][j] * 2) # Se houver laços, o grau aumenta 2 vezes.
            else: # Caso i != j (linha diferente de coluna):
                grau[i] += matriz[i][j] # O grau é aumentado a quantidade de arestas do vértice.
    for i in range(len(matriz)):
        print("Grau do vértice V%d = %d" % (i + 1, grau[i]))
    grau.sort(reverse = True) # Função para ordenar os graus.
    print("\nSequência gráfica:", grau) # Imprimindo a sequência gráfica.
    return grau

# Função principal:
def main():
    # Chamada das funções criadas anteriormente:
    ImprimeMatriz()
    VerificaArestas(VerificaSimples(simples), VerificaCompleto(completo))
    VerificaGrau()
    
main() # Chamada da função principal #
