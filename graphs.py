from typing import List, Optional

index: List[int] = [1]
indent: str = "  "

class Routes:
    def __init__(self,route:str,stops:int):
        self.route=route
        self.stops=stops
    def __str__(self):
        return f"route: {self.route}, stops: {self.stops}"

class GraphEdges:
    def __init__(self,source:str,target:str,distance:int):
        self.source=source
        self.target=target
        self.distance=distance
    def __str__(self):
        return f"source: {self.source}, target: {self.target}, distance: {self.distance}"

class Graph:
    def __init__(self,edges: List[GraphEdges]):
        self.edges = edges           

    def getAllPaths(self, source:str, target:str, maxStops:int, path: Optional[List[str]] = [], paths: Optional[List[List[str]]] = []) -> List[str]:
        # print(f'Explorando possibilidade: {[*path,source,"...",target]}')
        path = path + [source]
        # print(f'Path atualizado para {path}')
        currentIndex: int = 1
        
        # SE CHEGOU AO DESTINO, ADICIONA CAMINHO ENCONTRADO EM PATHS E RETORNA
        if (source == target):
            if(path in paths):
                pass
                # print(f'O caminho {path} já foi registrado')
            elif(len(path) > maxStops + 1):
                pass
                # print(f'Caminho muito longo, tem {len(path)-1} paradas e o máximo é {maxStops}')
            else:
                # print(f"Chegou no destino {target}")
                paths = paths + [path]
                # print(f'Paths atualizado para: {paths}')
            return paths
        
        # SE O NÓ ATUAL NÃO TEM NÓS SEGUIDOS A ELE, RETORNA NONE
        if source not in [edge.source for edge in self.edges]:
            # print(f"O nó {source} não tem um próximo nó associado")
            return None
        
        # SE NÃO CHEGOU AO DESTINO E TEM NÓS SEGUIDOS AO NÓ ATUAL, TESTA CADA UM DELES
        for next in [edge.target for edge in self.edges if edge.source == source]:
            # print(f'\n=========ARESTA ({currentIndex})============')
            # print(f'({currentIndex}) Encontrada aresta {source}-{next}')
            if next not in path:
                # print(f'({currentIndex}) {[*path,next,"...",target]} será explorado')              
                # print(f'\n-----------ENTRANDO EM {[*path,next]}--------------')

                # ENTRA EM UMA NOVA RECURSÃO
                paths = self.getAllPaths(next,target,maxStops,path,paths)
                
                # print(f'-----------SAINDO PARA {path}--------------\n')

                if paths:
                    pass
                    # print(f'Paths nesse contexto é: {paths}')
                else:
                    pass
                    # print(f'O caminho {[*path,next,"...",target]} não existe, é muito longo ou já foi registrado, testar próximo')
            
            # CASO O NÓ SEGUINTE AO ATUAL JÁ ESTEJA EM PATH, SEGUE PARA O PRÓXIMO NÓ SEGUINTE
            else:
                pass
                # print(f'({currentIndex}) {next} está em path')
            currentIndex += 1
            # SEGUE PARA O PRÓXIMO NÓ SEGUINTE AO ATUAL

        # APÓS VERIFICAR TODOS OS CAMINHOS POSSÍVEIS, RETORNA PATHS
        return paths

# EXAMPLE INPUT
entrada = {
    "data": [
        {
            "source": "A", "target": "B", "distance": 6
        },
        {
            "source": "A", "target": "E", "distance": 4
        },
        {
            "source": "B", "target": "A", "distance": 6
        },
        {
            "source": "B", "target": "C", "distance": 2
        },
        {
            "source": "B", "target": "D", "distance": 4
        },
        {
            "source": "C", "target": "B", "distance": 3
        },
        {
            "source": "C", "target": "D", "distance": 1
        },
        {
            "source": "C", "target": "E", "distance": 7
        },
        {
            "source": "D", "target": "B", "distance": 8
        },
        {
            "source": "E", "target": "B", "distance": 5
        },
        {
            "source": "E", "target": "D", "distance": 7
        }
    ]
}
graph = Graph([])
for edge in entrada["data"]:
    graph.edges.append(GraphEdges(edge["source"],edge["target"],edge["distance"]))
    
# EXAMPLE OUTPUT
[print(edge) for edge in graph.edges]
while(True):
    start = input("\nInício: ")
    end = input("Destino: ")
    stops = int(input("Paradas: "))
    print(f'Possíveis rotas: {graph.getAllPaths(start,end,stops)}')