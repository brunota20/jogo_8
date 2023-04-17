import copy
import time

objetivo = [[1,2,3],[4,5,6],[7,8,0]]

entrada1 = [[6,7,5],[1,2,3],[0,4,8]]
entrada2 = [[3,1,8],[5,6,2],[7,4,0]]
entrada_teste = [[1,0,2],[5,6,3],[4,7,8]]

regras = {(0,0):[(0,1),(1,0)], (0,1):[(0,0),(0,2),(1,1)], (0,2):[(0,1),(1,2)], 
          (1,0):[(0,0),(1,1),(2,0)], (1,1):[(0,1),(1,0),(1,2),(2,1)], (1,2):[(0,2),(1,1),(2,2)], 
          (2,0):[(2,1),(1,0)], (2,1):[(2,0),(2,2),(1,1)], (2,2):[(2,1),(1,2)]}

def acha_zero(entrada):
  for line, i in enumerate(entrada):
    for column, num in enumerate(i):
      if num == 0:
        posicao = (line, column)
        return posicao

def acha_regra(tupla_zero): # retorna a lista de regras possiveis para determinado 0
  for regra in regras:
    if regra == tupla_zero:
      lista_regras = regras[regra]
  return lista_regras


def troca_zero(entrada, posicao_zero, regras_possiveis, lista_visto, lista_aberto, lista_movimentos):
    linha_zero, coluna_zero = posicao_zero
    lista_visto.append(entrada)
    for regra in regras_possiveis:
        linha, coluna = regra
        nodo_para_alterar = [row[:] for row in entrada]
        nodo_para_alterar[linha_zero][coluna_zero], nodo_para_alterar[linha][coluna] = nodo_para_alterar[linha][coluna], nodo_para_alterar[linha_zero][coluna_zero]
        if nodo_para_alterar not in lista_visto and nodo_para_alterar not in lista_aberto:
            lista_aberto.append(nodo_para_alterar)
            lista_movimentos.append((entrada, nodo_para_alterar, regra))
        elif nodo_para_alterar in lista_visto:
            # estado já foi visto, ignora
            pass
        elif nodo_para_alterar in lista_aberto:
            # estado já está na lista de abertos, ignora
            pass
    return lista_visto, lista_aberto, lista_movimentos



def busca_em_largura(entrada, heuristica_var = "manhattan"):
    lista_aberto = [entrada]
    lista_visto = []
    lista_movimentos = []
    lista_pontuacao = []
    count = 0

    while lista_aberto:
        nodo_atual = lista_aberto.pop(0)
        if nodo_atual == objetivo:
            print(count)
            return lista_movimentos
        posicao_zero = acha_zero(nodo_atual)
        regras_possiveis = acha_regra(posicao_zero)
        lista_visto, lista_aberto, lista_movimentos = troca_zero(nodo_atual, posicao_zero, regras_possiveis, lista_visto, lista_aberto, lista_movimentos)
        if heuristica_var == "manhattan" or heuristica_var == "simples":
            lista_aberto = heuristica_funcao(lista_aberto, heuristica_var, objetivo)
        count += 1
    return False


def qtd_fora_do_lugar(entrada, objetivo):
    count = 0
    for i in range(3):
        for j in range(3):
            if entrada[i][j] != objetivo[i][j] and entrada[i][j] != 0:
                count += 1
    return count


def manhattan_distance(matrix1, matrix2):
    pos1 = acha_zero(matrix1)
    pos2 = acha_zero(matrix2)
    
    # Calculando a soma das distâncias de Manhattan
    distance = 0
    for i in range(3):
        for j in range(3):
            value1 = matrix1[i][j]
            if value1 != 0:
                # Encontrando a posição do elemento correspondente na segunda matriz
                pos2_value = [(k, l) for k in range(3) for l in range(3) if matrix2[k][l] == value1][0]
                # Calculando a distância de Manhattan
                distance += abs(i - pos2_value[0]) + abs(j - pos2_value[1])
    
    return distance + abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) # Adicionando a distância de Manhattan entre os elementos "0" das duas matrizes
    

def heuristica_funcao(matrix, heuristica = "manhattan", objetivo = [[1,2,3],[4,5,6],[7,8,0]]):
    lista_pontuacao = []
    if heuristica == "manhattan":
        for filho in matrix:
            lista_pontuacao.append((filho, manhattan_distance(filho, objetivo)))
    if heuristica == "simples":
        for filho in matrix:
            lista_pontuacao.append((filho, qtd_fora_do_lugar(filho, objetivo)))

    lista_pontuacao = Sort_Tuple(lista_pontuacao)
    
    lista_pontuada = [] #lista_aberto com os estados já ordenados
    for elemento in lista_pontuacao:
        lista_pontuada.append(elemento[0])


    if heuristica == "busca_largura":
        return 0

    return lista_pontuada


def Sort_Tuple(tup):
    tup.sort(key = lambda x: x[1])
    return tup


def movimentos(lista_movimentos, entrada):
    print(lista_movimentos)
    melhores_movimentos = []
    buscar = objetivo
    for movimento in reversed(lista_movimentos):
        if movimento[1] == buscar:
            melhores_movimentos.append(movimento[0])
            buscar = movimento[0]
            if buscar == entrada:
                break
    melhores_movimentos.insert(0,objetivo)
    return list(reversed(melhores_movimentos))




init = time.time()
busca_larg = busca_em_largura(entrada2, "manhattan")
end = time.time()
lista_mov = movimentos(busca_larg, entrada2)
print(lista_mov)
print(f"Quantidade de movimentos (contanto com a entrada): ", len(lista_mov))



print("O tempo de busca foi: ", end - init, " segundos")
