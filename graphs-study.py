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
    def allPaths(self, source:str, target:str, maxStops:int) -> List[List[str]]:
        paths: List[str] = []
        currentPath = self.getPath(source,target,maxStops)
        while (currentPath not in paths):
            paths = paths + [currentPath]
            currentPath = self.getPath(source,target,maxStops)            

    def getPath(self, source:str, target:str, maxStops:int, path: Optional[List[str]] = [], paths: Optional[List[List[str]]] = [], index: Optional[List[int]] = [1]) -> List[str]:
        print(f"{indent*(len(index)-1)}{index} Entrando com path: {path}, explorando {source}-...-{target}, maxStops: {maxStops}")
        path = path + [source]
        print(f'{indent*(len(index)-1)}{index} Path atualizado para {path}')
        currentIndex: int = 1
        
        # SE CHEGOU AO DESTINO, RETORNA PATH
        if (source == target):
            if(path in paths):
                print(f'{indent*(len(index)-1)}{index} O caminho {path} já foi registrado')
                return None
            else:
                print(f"{indent*(len(index)-1)}{index} Chegou no destino {target}")
                return path
        
        # SE O NÓ ATUAL NÃO TEM NÓS SEGUIDOS A ELE, RETORNA NONE
        if source not in [edge.source for edge in self.edges]:
            print(f"{indent*(len(index)-1)}{index} O nó {source} não tem um próximo nó associado")
            return None
        
        # SE NÃO CHEGOU AO DESTINO E TEM NÓS SEGUIDOS AO NÓ ATUAL, TESTA CADA UM DELES
        for next in [edge.target for edge in self.edges if edge.source == source]:
            distance: List[int] = [edge.distance for edge in self.edges if (edge.source == source and edge.target == next)]
            print(f'{indent*(len(index)-1)}{index}\n{indent*(len(index)-1)}{index} =========ARESTA ({currentIndex})============')
            print(f'{indent*(len(index)-1)}{index} ({currentIndex}) Encontrada aresta {source} --{distance[0]}--> {next}')
            if next not in path:
                print(f'{indent*(len(index)-1)}{index} ({currentIndex}) {source}-{next}-...-{target} será explorado')
                newIndex: List[int] = (index + [currentIndex])                
                print(f'\n{indent*(len(newIndex)-1)}-----------ENTRANDO NA RECURSÃO {newIndex}--------------')

                # ENTRA EM UMA NOVA RECURSÃO
                newPath = self.getPath(next,target,10,path,paths,newIndex)

                print(f'{indent*(len(newIndex)-1)}-----------SAINDO DA RECURSÃO {newIndex}--------------\n')
                print(f'{indent*(len(index)-1)}{index} ({currentIndex}) O valor retornado foi: {newPath}')
                
                # CASO O NÓ SEGUINTE AO ATUAL TENHA UMA CONEXÃO VÁLIDA COM O NÓ DE DESTINO, RETORNA O CAMINHO ENCONTRADO
                if newPath:
                    print(f'{indent*(len(index)-1)}{index} ({currentIndex}) Foi encontrado caminho {source}-{next}-...-{target}')
                    return newPath
                print(f'{indent*(len(index)-1)}{index} ({currentIndex}) Não foi encontrado caminho {source}-{next}-...-{target}, devemos tentar outro caminho')
                print(f'{indent*(len(index)-1)}{index} ({currentIndex}) Path continua sendo {path}')
            
            # CASO O NÓ SEGUINTE AO ATUAL JÁ ESTEJA EM PATH, SEGUE PARA O PRÓXIMO NÓ SEGUINTE
            else:
                print(f'{indent*(len(index)-1)}{index} ({currentIndex}) {next}-...-{target} já foi explorado')
            currentIndex += 1
            # SEGUE PARA O PRÓXIMO NÓ SEGUINTE AO ATUAL
            
        print(f"{indent*(len(index)-1)}{index} Não existe caminho {source}-...-{target} não explorado")
        # CASO NENHUM NÓ SEGUINTE AO ATUAL TENHA CONEXÃO VÁLIDA COM O NÓ DE DESTINO, RETORNA NONE
        return None

# EXAMPLE INPUT
input = {
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
for edge in input["data"]:
    graph.edges.append(GraphEdges(edge["source"],edge["target"],edge["distance"]))
    
# EXAMPLE OUTPUT
[print(edge) for edge in graph.edges]
print(f'Final output: {graph.getPath("B","E",3,paths=[["B","A","E"]])}')
# print('A --6--> B --6--> A [X]\n          \--2--> C --3--> B [X]\n                   \--1--> D --8--> B [X]\n                   \--7--> E [OK]\n\nA --6--> B --2--> C --7--> E')