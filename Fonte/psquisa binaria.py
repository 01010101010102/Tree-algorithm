#pesquisa binária
import random

def pesquisa(item,menor = None, maior = None):
    T =list(range(1000+1))
    if menor== None:
        menor = 0
    if maior == None:
        maior = len(T) - 1
    if maior < menor:
        T.append(item)
        print(T.index(item))
        return -1
    #T sera o local de pesquisa onde teremos que encontrar o item.
    ponto_central = (menor + maior) // 2
    if ponto_central == item:
        print(ponto_central,",na posição:%d" % T.index(item))
    elif item < T[ponto_central]:
        return pesquisa(item,menor, ponto_central-1)
    elif item > T[ponto_central]:
        return pesquisa(item,ponto_central+1,maior)


pesquisa(int(input("digite o numero a ser pesquisado:")))
