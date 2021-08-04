from typing import Optional,List
from pydantic import BaseModel

class GraphEdge(BaseModel):
    source: str
    target: str
    distance: int

class Graph(BaseModel):
    id: int = None
    data: List[GraphEdge]

class Route(BaseModel):
    route: str
    stops: int

class Routes(BaseModel):
    routes: List[Route]

def getAllRoutes(graph: Graph, source:str, target:str, maxStops:int, path: Optional[str] = "", paths: Optional[Routes] = []) -> Routes:
        path = path + source
        currentRoutes = []
        if (paths): currentRoutes = [currentRoute.route for currentRoute in paths.routes]
        if (source == target):
            if((path not in currentRoutes) and (len(path) - 1) <= maxStops):
                currentRoutes.append(path)
            paths = Routes(routes=[])
            for currentRoute in currentRoutes:
                paths.routes.append(Route(route=currentRoute,stops=(len(currentRoute) - 1)))
            return paths
        if source not in [edge.source for edge in graph.data]:
            return None
        for next in [edge.target for edge in graph.data if edge.source == source]:
            if next not in path:
                paths = getAllRoutes(graph,next,target,maxStops,path,paths)
                currentRoutes = []
                if (paths): currentRoutes = [currentRoute.route for currentRoute in paths.routes]
        paths = Routes(routes=[])
        for currentRoute in currentRoutes:
            paths.routes.append(Route(route=currentRoute,stops=(len(currentRoute) - 1)))
        return paths