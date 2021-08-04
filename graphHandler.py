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

class Distance(BaseModel):
    distance: int
    path: List[str]

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

def getMinDistance(graph: Graph, source: str, target: str, path: Optional[List[str]] = [], minPath: Optional[List[str]] = [], distance: Optional[int] = 0, minDistance: Optional[int] = 10000):
    path = path + [source]
    if (source == target and distance < minDistance):
        minDistance = distance
        minPath = path
        return (path,minPath,distance,minDistance)
    elif (source == target):
        return (None,minPath,None,minDistance)
    if source not in [edge.source for edge in graph.data]:
        return (None,minPath,None,minDistance)
    for next in [edge.target for edge in graph.data if edge.source == source]:
        newDistance = distance + [edge.distance for edge in graph.data if edge.source == source and edge.target == next][0]
        if next not in path:            
            (newPath,minPath,newDistance,minDistance) = getMinDistance(graph,next,target,path,minPath,newDistance,minDistance)
    return (None,minPath,None,minDistance)