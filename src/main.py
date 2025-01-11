from grafo import Grafo
from aco import ColoracaoFormigas

# grafo simples com 5 vertices
grafo = Grafo(5)  # grafo com 5 vértices
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(3, 4)

# instanciando e executando o algoritmo
aco = ColoracaoFormigas(grafo, num_formigas=10, num_iteracoes=100)
coloracao, num_cores = aco.executar()

print(f"Número de cores usadas: {num_cores}")
print(f"Coloração encontrada: {coloracao}")
