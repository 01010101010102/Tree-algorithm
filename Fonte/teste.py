import random
from arvorebinaria import ArvoreBinariadeBusca


random.seed(77)
T = random.sample(range(1,1000),46)

bst = ArvoreBinariadeBusca()
for item in T:
    bst.inserir(item)

bst.percuros_pós_ordem()

itens = [23,54,6,578,-1,99,9]
for item in itens:
    v = bst.pesquisar(item)
    if v == None:
        print("\n")
        print(item,"não encontrado")
        bst.inserir(item)
        print("item inserido")
        bst.percuros_pós_ordem()
    else:
        print("\n")
        print(bst.root.data,"encontrado")
        print("\n")