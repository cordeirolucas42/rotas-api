from graphHandler import Graph, Distance
from graphHandler import getAllRoutes, getMinDistance
from typing import Optional, List
from fastapi import FastAPI

graphsDB: List[Graph] = []

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "Nome": "Lucas Cordeiro",
        "Idade": 27,
        "Data da Vacina": "04/08/21"
    }


@app.post("/graph")
def create_graph(graph: Graph):
    if (graphsDB):
        graph.id = graphsDB[-1].id + 1
    else:
        graph.id = 1
    graphsDB.append(graph)
    return graphsDB[-1]


@app.get("/graph/{graphId}")
def get_graph(graphId: int):
    for graph in graphsDB:
        if(graph.id == graphId):
            return graph


@app.post("/routes/{graphId}/from/{town1}/to/{town2}")
def get_all_routes(graphId: int, town1: str, town2: str, maxStops: int):
    currentGraph = [graph for graph in graphsDB if graph.id == graphId][0]
    return getAllRoutes(currentGraph, town1, town2, maxStops)


@app.post("/distance/{graphId}/from/{town1}/to/{town2}")
def get_min_distance(graphId: int, town1: str, town2: str):
    currentGraph = [graph for graph in graphsDB if graph.id == graphId][0]
    (_, minPath, _, minDistance) = getMinDistance(currentGraph, town1, town2)
    return Distance(distance=minDistance, path=minPath)

# py -m uvicorn main:app --reload
