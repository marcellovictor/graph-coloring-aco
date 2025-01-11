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

# parametros encontrados na calibração
num_formigas = 5
num_iteracoes = 42
taxa_evaporacao = 0.1

solucoes = []
tempos = []

for i in range(10):
    print(f"\nExecução {i+1}/10")
    
    inicio = time.time()

    aco = ColoracaoFormigas(grafo, num_formigas, num_iteracoes, taxa_evaporacao)
    coloracao, num_cores = aco.executar()

    fim = time.time()
    duracao = (fim - inicio) * 1000000

    solucoes.append((coloracao, num_cores))
    tempos.append(duracao)
    
    print(f"Número de cores: {num_cores}")
    print(f"Tempo de execução: {duracao:.2f} µs")

# calcular métricas
numeros_cores = [s[1] for s in solucoes]
valor_medio = sum(numeros_cores) / len(numeros_cores)
melhor_solucao = min(solucoes, key=lambda x: x[1])
tempo_medio = sum(tempos) / len(tempos)

# resultados finais
print("\nResultados das 10 execuções:")
print(f"Valor médio da solução: {valor_medio:.1f} cores")
print(f"Melhor solução encontrada: {melhor_solucao[1]} cores")
print(f"Tempo médio computacional: {tempo_medio:.2f} µs")
print("\nMelhor coloração encontrada:", melhor_solucao[0])