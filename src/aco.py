from grafo import Grafo
import random

class ColoracaoFormigas:
    def __init__(self, grafo, num_formigas, num_iteracoes, taxa_evaporacao=0.1):
        # parametros básicos do algoritmo
        self.grafo = grafo
        self.num_formigas = num_formigas
        self.num_iteracoes = num_iteracoes
        self.num_max_cores = len(self.grafo.vertices) + 1
        
        # parametros de controle do feromonio
        self.taxa_evaporacao = taxa_evaporacao  # Agora recebido como parâmetro
        self.feromonios = self.inicializar_feromonios()


    def inicializar_feromonios(self):
        """
        linha i: vértice
        coluna j: cor
        o valor na posicao [i][j] representa a quantidade de feromonio para o vertice i usar a cor j
        """
        # cria uma matriz num_vertices X num_cores preenchida com 1.0 (valor inicial dos feromonios)
        return [[1.0] * self.num_max_cores for _ in range(len(self.grafo.vertices))]


    def cores_disponiveis(self, vertice, coloracao):
        """
        determina quais cores podem ser usadas para um vertice, considerando as cores ja usadas pelos seus vizinhos.
        coloracao é uma lista onde o índice é o vertice e o valor é a cor (-1 se não colorido)
        """
        # obtém as cores já usadas pelos vizinhos
        cores_vizinhos = set()
        for vizinho in self.grafo.vizinhos(vertice):
            if coloracao[vizinho] != -1:
                cores_vizinhos.add(coloracao[vizinho])

        # retorna todas as cores que podem ser usadas
        return [cor for cor in range(self.num_max_cores) if cor not in cores_vizinhos]


    def escolher_cor(self, vertice, cores_possiveis):
        """
        escolhe uma cor para o vertice baseado no feromonio.
        usa um sistema de sorteio onde cores com mais feromonio tem mais chance de serem escolhidas.
        """
        # soma total de feromonio das cores possiveis
        total_feromonio = sum(self.feromonios[vertice][cor] for cor in cores_possiveis)
        
        # sistema de sorteio - quanto mais feromonio, mais chance
        valor_aleatorio = random.random() * total_feromonio
        soma_atual = 0
        
        for cor in cores_possiveis:
            soma_atual += self.feromonios[vertice][cor]
            if soma_atual >= valor_aleatorio:
                return cor


    def formiga_colore_grafo(self):
        """
        uma única formiga cria uma possível coloração para o grafo.
        a ordem dos vertices é aleatória e as escolhas são baseadas no feromonio.
        """
        coloracao = [-1] * len(self.grafo.vertices)
        
        ordem_coloracao = list(range(len(self.grafo.vertices)))
        random.shuffle(ordem_coloracao)
        
        for indice_vertice in ordem_coloracao:
            cores_possiveis = self.cores_disponiveis(indice_vertice, coloracao)
            cor_escolhida = self.escolher_cor(indice_vertice, cores_possiveis)
            coloracao[indice_vertice] = cor_escolhida
        
        return coloracao


    def atualizar_feromonios(self, solucoes):
        """
        atualiza a matriz de feromonios baseado nas soluções encontradas.
        primeiro evapora parte do feromonio antigo, depois adiciona novo feromonio proporcional à qualidade das soluções.
        """
        # evaporação do feromonio
        for i in range(len(self.grafo.vertices)):
            for j in range(self.num_max_cores):
                self.feromonios[i][j] *= (1 - self.taxa_evaporacao)

        # adiciona novo feromonio baseado na qualidade das soluções
        for coloracao in solucoes:
            num_cores = len(set(cor for cor in coloracao if cor != -1))
            deposito = 1.0 / num_cores  # quanto menos cores, mais feromonio
            
            # deposita feromonio nos caminhos usados
            for vertice in range(len(coloracao)):
                if coloracao[vertice] != -1:
                    self.feromonios[vertice][coloracao[vertice]] += deposito

    def executar(self):
        """
        método principal que executa o algoritmo aco
        
        - o algoritmo executa por um numero determinado de iterações.
        - em cada uma, várias formigas constroem soluções de coloração guiadas pelos feromonios.
        - os feromonios são atualizados ao final de cada iteração, fortalecendo os caminhos que levaram a boas soluções.
        """
        melhor_coloracao = None
        melhor_num_cores = self.num_max_cores
        
        for iteracao in range(self.num_iteracoes):
            solucoes_iteracao = []
            
            for formiga in range(self.num_formigas):
                coloracao = self.formiga_colore_grafo()
                num_cores = len(set(coloracao))
                solucoes_iteracao.append(coloracao)
                
                if num_cores < melhor_num_cores:
                    melhor_num_cores = num_cores
                    melhor_coloracao = coloracao.copy()
            
            self.atualizar_feromonios(solucoes_iteracao)
        
        return melhor_coloracao, melhor_num_cores
