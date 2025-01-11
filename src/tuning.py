from grafo import Grafo
from aco import ColoracaoFormigas
import time

# cria grafo
grafo = Grafo(10)
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 2)
grafo.adicionar_aresta(1, 3)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(0, 4)
grafo.adicionar_aresta(0, 5)
grafo.adicionar_aresta(3, 6)
grafo.adicionar_aresta(3, 7)
grafo.adicionar_aresta(6, 7)
grafo.adicionar_aresta(7, 8)
grafo.adicionar_aresta(8, 9)

# range de valores
valores_num_formigas = [v for v in range(5, 16)]
valores_num_iteracoes = [v for v in range(5, 101)]
valores_taxa_evaporacao = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

melhor_num_cores = grafo.num_vertices + 2
melhores_parametros = {"num_formigas": None, "num_iteracoes": None, "taxa_evaporacao": None}


# calibra
for num_formigas in valores_num_formigas:
        for num_iteracoes in valores_num_iteracoes:
            for taxa_evaporacao in valores_taxa_evaporacao:

                aco = ColoracaoFormigas(grafo, num_formigas, num_iteracoes, taxa_evaporacao)
                coloracao, num_cores = aco.executar()

                if num_cores < melhor_num_cores:
                    melhor_num_cores = num_cores
                    melhores_parametros["num_formigas"] = num_formigas
                    melhores_parametros["num_iteracoes"] = num_iteracoes
                    melhores_parametros["taxa_evaporacao"] = taxa_evaporacao

print(melhores_parametros)
print("Cores:", num_cores)
