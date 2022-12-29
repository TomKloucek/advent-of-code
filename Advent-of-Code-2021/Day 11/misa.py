class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float("inf")
        self.previousVertex = None

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

class priorityQueue:
    def __init__(self):
        self.priorityQueue = []

    def insert(self, data, priority):
        if self.priorityQueue == []:
            self.priorityQueue.append([data, priority])
        else:
            for index in range(len(self.priorityQueue)):
                if priority < self.priorityQueue[index][1]:
                    self.priorityQueue.insert(index, [data,priority])
                    return
                else:
                    continue
            else:
                self.priorityQueue.append([data, priority])

    def delete(self):
        return self.priorityQueue.pop(0)

    def empty(self):
        return len(self.priorityQueue) == 0

class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def getVertexById(self, id):
        for vertex in self.vertexes:
            if id == vertex.id:
                return vertex

    def computePath(self, sourceId):
        visited = []
        kamjit = priorityQueue()
        for vertex in self.vertexes:
            if vertex.id == sourceId:
                vertex.minDistance = 0
                vertex.previousVertex = vertex
                kamjit.insert(vertex, vertex.minDistance)
                break
        while not kamjit.empty():
            odstraneny = kamjit.delete()[0]
            visited.append(odstraneny)
            for soused in odstraneny.edges:
                vzdalenost = soused.weight
                if self.getVertexById(soused.target) not in visited:
                    if (odstraneny.minDistance + vzdalenost) < self.getVertexById(soused.target).minDistance:
                        self.getVertexById(soused.target).minDistance = odstraneny.minDistance + vzdalenost
                        self.getVertexById(soused.target).previousVertex = odstraneny
                        kamjit.insert(self.getVertexById(soused.target),self.getVertexById(soused.target).minDistance)

    def getShortestPathTo(self, targetId):
        path = []
        x = self.getVertexById(targetId)
        if x.previousVertex is None:
            return path
        while x.previousVertex != x:
            path.append(x)
            x = x.previousVertex
        path.append(x)
        return path[::-1]

    def createGraph(self, vertexes, edgesToVertexes):
        for vertex in vertexes:
            for edge in edgesToVertexes:
                if vertex.id == edge.source:
                    vertex.edges.append(edge)
            self.vertexes.append(vertex)

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float("inf")
            vertex.previousVertex = None

    def getVertexes(self):
        return self.vertexes