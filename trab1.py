import copy
import time
#lista = [[[4,5,1], [0,7,2], [8,3,6]]]
lista = [[[3,1,8],[5,6,2],[7,4,0]]]
#lista = [[[4,1,2], [5,0,3], [7, 8,6]]]
#lista = [[[1,2,0],[4,5,3],[7,8,6]]]
lista_final = [[1,2,3],[4,5,6],[7,8,0]]



def acha_zero(entrada):
  for line, i in enumerate(entrada):
    for column, num in enumerate(i):
      if num == 0:
        posicao = (line, column)
        #print("essa e a posicao", posicao)
        return posicao


  

def troca_posicao(tuplaPosicao, lista, pai):
  peso_posicao = [[1,2,3],[4,5,6],[7,8,0]]
  peso_da_troca = []
  lista_de_combinacoes = []
  #print(tuplaPosicao)
  for count, posicao in enumerate(tuplaPosicao):
    if count == 0:
      if posicao == 0:
        #print("COUNT = 0, POSICAO 0")
        novaLista = copy.deepcopy(lista)
        novaLista[0][tuplaPosicao[1]] = novaLista[1][tuplaPosicao[1]]
        novaLista[1][tuplaPosicao[1]] = 0
        lista_de_combinacoes.append(novaLista)
        #print(novaLista)
      if posicao == 1:
        #print("COUNT = 0, POSICAO 1")
        novaLista = copy.deepcopy(lista)
        novaLista[1][tuplaPosicao[1]] = novaLista[2][tuplaPosicao[1]]
        novaLista[2][tuplaPosicao[1]] = 0
        lista_de_combinacoes.append(novaLista)
        #print(novaLista)
        novaLista2 = copy.deepcopy(lista)
        novaLista2[1][tuplaPosicao[1]] = novaLista2[0][tuplaPosicao[1]]
        novaLista2[0][tuplaPosicao[1]] = 0
        lista_de_combinacoes.append(novaLista2)
        #print(novaLista2)
      if posicao == 2:
        #print("COUNT = 0, POSICAO 2")
        novaLista = copy.deepcopy(lista)
        novaLista[2][tuplaPosicao[1]] = novaLista[1][tuplaPosicao[1]]
        novaLista[1][tuplaPosicao[1]] = 0
        lista_de_combinacoes.append(novaLista)
        #print(novaLista)
        
    if count == 1:
      if posicao == 0:
        #print("COUNT = 1, POSICAO 0")
        novaLista = copy.deepcopy(lista)
        novaLista[tuplaPosicao[0]][0] = novaLista[tuplaPosicao[0]][1]
        novaLista[tuplaPosicao[0]][1] = 0
        lista_de_combinacoes.append(novaLista)
        #print(novaLista)
      if posicao == 1:
        #print("COUNT = 1, POSICAO 1")
        novaLista = copy.deepcopy(lista)
        novaLista[tuplaPosicao[0]][1] = novaLista[tuplaPosicao[0]][2]
        novaLista[tuplaPosicao[0]][2] = 0
        lista_de_combinacoes.append(novaLista)
        #print(novaLista)
        novaLista2 = copy.deepcopy(lista)
        novaLista2[tuplaPosicao[0]][1] = novaLista2[tuplaPosicao[0]][0]
        novaLista2[tuplaPosicao[0]][0] = 0
        lista_de_combinacoes.append(novaLista2)
        #print(novaLista2)
      if posicao == 2:
        #print("COUNT = 1, POSICAO 2")
        novaLista = copy.deepcopy(lista)
        novaLista[tuplaPosicao[0]][2] = novaLista[tuplaPosicao[0]][1]
        novaLista[tuplaPosicao[0]][1] = 0
        lista_de_combinacoes.append(novaLista)
        #print(novaLista)

  if pai in lista_de_combinacoes:
    lista_de_combinacoes.remove(pai)
  return lista_de_combinacoes, len(lista_de_combinacoes)

print(acha_zero(lista))


print()
init = time.time()
resultado = busca_largura(lista, [[[0,0,0],[0,0,0],[0,0,0]]], lista_final, 1, 0)
end = time.time()



print("O numero de linhas e: ", resultado[0])
print("O numero de nodos visitados e: ", resultado[1])
print("O tempo de busca foi: ", end - init, " segundos")

    


def busca_largura(lista, pais, lista_final, iteracao, nodos):
  print(iteracao, "------------------")
  todos_os_filhos = []
  novos_pais = []
  encontrado = False
  #print(len(lista))
  nodos+=len(lista)
  print(lista)
  for pos, filho in enumerate(lista):
    if filho == lista_final:
      encontrado = True
      print(filho, "deu certo")
    if iteracao > 32:
      print("Explosao")
      return None
    zero = acha_zero(filho)
    filhos, quantidade = troca_posicao(zero, filho, pais[pos])
    for i in range(quantidade):
      novos_pais.append(filho)
    todos_os_filhos = todos_os_filhos + filhos
  if encontrado:
    return iteracao, nodos
  return busca_largura(todos_os_filhos, novos_pais, lista_final, iteracao+1, nodos)
