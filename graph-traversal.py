#!/usr/bin/env python3
from collections import defaultdict
import networkx as nx
import subprocess

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.traversalCounter = 0

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def printTraversal(self, type: str, vertex: int = None):
        self.traversalCounter += 1
        self.printGraph(outfile=f"{type}-traversal-{self.traversalCounter}.png", colourNode=vertex)
        # self.traversalCounter = 0

    def printGraph(self,outfile:str = 'graph.png', colourNode: int = None):

        dirGraph = nx.DiGraph(directed=True)

        for vertex in self.graph:
            dirGraph.add_node(vertex, color='#d32f2f' if colourNode == vertex else '#2196f3' )
            for edge in self.graph[vertex]:
                dirGraph.add_edge(vertex, edge)

        A = nx.drawing.nx_agraph.to_agraph(dirGraph)
        A.layout()
        A.draw(outfile)

    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex from
            # queue
            s = queue.pop(0)

            self.printTraversal('bfs', s)
            print (s, end = " ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS(self, s: int, visited: list = None):
        if not visited:
            # Mark all the vertices as not visited
            visited = [False] * (len(self.graph))

        # Mark the source node as visited
        visited[s] = True

        self.printTraversal('dfs', s)
        print (s, end = " ")

        # Get all adjacent vertices of the
        # vertex s. If a adjacent
        # has not been visited, then process it (stack)
        for i in self.graph[s]:
            if visited[i] == False:
                self.DFS(i, visited)



if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    g.addEdge(4, 3)
    g.addEdge(3, 4)
    g.printGraph()

    startingVertex = 2
    print("Graph adjacent list: ", g.graph)
    print (f"Breadth First Traversal (starting from vertex {startingVertex})")
    g.BFS(startingVertex)
    print()
    print (f"Depth First Traversal (starting from vertex {startingVertex})")
    g.DFS(startingVertex)
    print()
