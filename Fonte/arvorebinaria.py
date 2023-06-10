class Nó:
    def __init__(self,data):
        self.data = data
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.data)
    
class ArvoreBinaria:
    def __init__(self,data=None,nó = None):
        if nó:
            self.root = nó
        elif data:
            nó = Nó(data)
            self.root = nó
        else:
            self.root = None

    def percuros_pós_ordem(self,nó=None):
        if nó is None:
            nó = self.root
        if nó.esquerda:
            self.percuros_pós_ordem(nó.esquerda)
        if nó.direita:
            self.percuros_pós_ordem(nó.direita)
        print(nó,end=' ')
        


    def altura(self,nó=None):
        if nó is None:
            nó = self.root
        alt_dir = 0
        alt_esq = 0
        if nó.esquerda:
           alt_esq = self.altura(nó.esquerda)
        if nó.direita:
            alt_dir = self.altura(nó.direita)
        if alt_dir > alt_esq:
            return alt_dir +1
        return alt_esq +1
        

class ArvoreBinariadeBusca(ArvoreBinaria):
    def inserir(self,valor):
        pai = None
        x = self.root
        while(x):
            pai = x
            if valor <x.data:
                x = x.esquerda
            else:
                x = x.direita
        if pai is None:
            self.root = Nó(valor)
        elif valor < pai.data:
            pai.esquerda = Nó(valor) #sempre insira omenor na esquerda
        else:
            pai.direita = Nó(valor) #sempre insira o maior na direita

    def pesquisar(self,valor,nó=0):
        if nó == 0:
            nó = self.root
        if nó is None:
            return nó
        if nó.data == valor:
            return ArvoreBinariadeBusca(nó) #aqui indices não faz sentido,por isso manda uma subarvore
        if valor < nó.data:
            return self.pesquisar(valor,nó.esquerda)
        return self.pesquisar(valor,nó.direita)
        