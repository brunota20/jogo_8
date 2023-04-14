import copy
import time

objetivo = [[1,2,3],[4,5,6],[7,8,0]]

entrada1 = [[6,7,5],[1,2,3],[0,4,8]]
entrada2 = [[3,1,8],[5,6,2],[7,4,0]]
entrada_teste = [[1,2,3],[4,0,6],[7,5,8]]

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
    return lista_visto, lista_aberto, lista_movimentos


def busca_em_largura(entrada):
    lista_aberto = [entrada]
    lista_visto = []
    lista_movimentos = []
    count = 0
    
    while lista_aberto:
        nodo_atual = lista_aberto.pop(0)
        if nodo_atual == objetivo:
            print(count)
            return lista_movimentos
        posicao_zero = acha_zero(nodo_atual)
        regras_possiveis = acha_regra(posicao_zero)
        lista_visto, lista_aberto, lista_movimentos = troca_zero(nodo_atual, posicao_zero, regras_possiveis, lista_visto, lista_aberto, lista_movimentos)
        count += 1
    return False


def movimentos(lista_movimentos, entrada):
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
busca_larg = busca_em_largura(entrada1)
end = time.time()
lista_mov = movimentos(busca_larg, entrada1)
print(lista_mov)
print(f"Quantidade de movimentos (contanto com a entrada): ", len(lista_mov))



print("O tempo de busca foi: ", end - init, " segundos")
