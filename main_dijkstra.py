from grafos_dijkstra import Graph

g = Graph()

# exemplo do livro "Entendendo Algoritmos"
g.adicionar_vertice("inicio")
g.adicionar_vertice("A")
g.adicionar_vertice("B")
g.adicionar_vertice("fim")

g.adicionar_aresta("inicio", "A", 6)
g.adicionar_aresta("inicio", "B", 2)
g.adicionar_aresta("B", "A", 3)
g.adicionar_aresta("A", "fim", 1)
g.adicionar_aresta("B", "fim", 5)

result = g.dijkstra(origem="inicio", destino="fim")
print(result)

