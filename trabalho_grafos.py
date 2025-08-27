import numpy as np

class Graph:
  def __init__(self,grafo=None):
    self.processados = []
    if grafo is not None:
      self.grafo = grafo
    else:
      self.grafo = {}
    
  def adicionar_vertice(self, vertice):
    if vertice not in self.grafo:
      self.grafo[vertice] = {}
  
  def adicionar_aresta(self, origem, destino, peso):
    self.adicionar_vertice(origem)
    self.adicionar_vertice(destino)
    self.grafo[origem][destino] = peso
  
  def mostrar_arestas(self):
    for i in self.grafo.keys():
      for j in self.grafo.keys():
        peso = self.grafo[i].get(j)
        if peso is not None:
          print(f"Vértice {i} -> {peso} -> Vértice {j}")
  
  def mostrar_vertices(self):
    return self.grafo.keys()
  
  def custo_mais_baixo(self, custos):
    custo_mais_baixo = np.inf
    processados = []
    no_custo_mais_baixo = None
    for i in custos:
      custo = custos[i]
      if custo < custo_mais_baixo and i not in self.processados:
        custo_mais_baixo = custo
        no_custo_mais_baixo = i
        self.processados.append(i)

    return no_custo_mais_baixo
  
  def dijkstra(self, origem, destino):

    # iniciados os parametros necessários
    infinito = np.inf
    custos = {vertice: infinito for vertice in self.grafo}
    custos[origem] = 0
    pais = {vertice: None for vertice in self.grafo}
    processados = []

    # função que acha o custo mais baixo com base na hash de custos
    def custo_mais_baixo(custos, processados):
        custo_baixo = infinito
        no_custo_baixo = None
        for no, custo in custos.items():
            if custo < custo_baixo and no not in processados:
                custo_baixo = custo
                no_custo_baixo = no
        return no_custo_baixo

    # início do loop
    no_atual = custo_mais_baixo(custos, processados) # no_atual no começo: inicio
    while no_atual is not None:
      custo_atual = custos[no_atual] # 0 (todos os outros inicialmente são infinitos)
      vizinhos = self.grafo[no_atual] # {"A": 6, "B": 2}

      for vizinho, peso in vizinhos.items(): # "A: 6" e "B: 2"
        novo_custo = custo_atual + peso
        if novo_custo < custos[vizinho]:
          custos[vizinho] = novo_custo
          pais[vizinho] = no_atual
      processados.append(no_atual)
      no_atual = custo_mais_baixo(custos, processados)

    if custos[destino] == infinito:
      return "Erro ao processar o caminho"
    
    # cria a lista que vai armazenar o caminho percorrido
    caminho = []
    no_caminho = destino
    while no_caminho is not None:
        caminho.insert(0, no_caminho) # adicionei na lista o nó destino
        no_caminho = pais[no_caminho] # já que fui atualizando o dicionário "pais", é só ir de pai em pai
                                      # até encontrar o fim (no_caminho is None)

        
    return {
        "custo_total": custos[destino],
        "caminho": caminho
    }
  

# exemplo:
g = Graph()
g.adicionar_vertice("inicio")
g.adicionar_vertice("A")
g.adicionar_vertice("B")
g.adicionar_vertice("fim")


g.adicionar_aresta("inicio", "A", 6)
g.adicionar_aresta("inicio", "B", 2)
g.adicionar_aresta("A", "fim", 1)
g.adicionar_aresta("B", "A", 3)
g.adicionar_aresta("B", "fim", 5)


print(g.dijkstra("inicio", "fim"))


        


