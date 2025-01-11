class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = list(range(num_vertices)) # lista de vértices
        self.lista_adj = {v: [] for v in range(num_vertices)} # listas iniciadas vazias
        
    
    def adicionar_aresta(self, v1, v2):
        # adiciona v2 à lista de adjacência de v1 e vice-versa
        self.lista_adj[v1].append(v2)
        self.lista_adj[v2].append(v1)
    
    def vizinhos(self, vertice):
        return self.lista_adj[vertice]
