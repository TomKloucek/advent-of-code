class Vertex:
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
        self.edges = []
        self.minDistance = float('inf')
        self.previousVertex = None

class PriorityQueue:
    def __init__(self):
        self.values = []
        self.priorities = []

    def append(self,item):
        if (len(self.priorities)) == 0:
            self.priorities.append(item.minDistance)
            self.values.append(item.id)
            return
        for i in range(len(self.priorities)):
            if item.minDistance < self.priorities[i]:
                self.priorities.insert(i,item.minDistance)
                self.values.insert(i,item.id)
                return
        self.priorities.append(item.minDistance)
        self.values.append(item.id)

    def pop(self):
        return self.priorities.pop(0),self.values.pop(0)

    def is_empty(self):
        if len(self.priorities) == 0: return True
        return False

class Edge:
    def __init__(self, source:int, target:int, weight:int):
        self.source = source
        self.target = target
        self.weight = weight

class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def getVertex(self,id):
        for vertex in self.vertexes:
            if vertex.id == id:
                return vertex

    def computePath(self, sourceId):
        togo = PriorityQueue()
        visited = []
        self.getVertex(sourceId).minDistance = 0
        self.getVertex(sourceId).previousVertex = self.getVertex(sourceId)
        togo.append(self.getVertex(sourceId))
        while not togo.is_empty():
            (distance,current_vertex) = togo.pop()
            visited.append(current_vertex)

            for neighbor in self.getVertex(current_vertex).edges:
                if self.getVertex(neighbor.target).minDistance != -1:
                    distance =  neighbor.weight
                    if self.getVertex(neighbor.target) not in visited:
                        old_cost = self.getVertex(neighbor.target).minDistance
                        new_cost = self.getVertex(current_vertex).minDistance + distance
                        if new_cost < old_cost:
                            self.getVertex(neighbor.target).minDistance = new_cost
                            self.getVertex(neighbor.target).previousVertex = self.getVertex(current_vertex)
                            togo.append(self.getVertex(neighbor.target))

    def getShortestPathTo(self, targetId):
        path = []
        next = self.getVertex(targetId)
        if next.previousVertex is None:
            return path
        while next.minDistance != 0:
            path.append(next)
            next = next.previousVertex
        path.append(next)
        return path[::-1]

    def createGraph(self, vertexes, edgesToVertexes):
        self.vertexes = vertexes
        for vertex in vertexes:
            for edge in edgesToVertexes:
                if edge.source == vertex.id:
                    vertex.edges.append(edge)

    def resetDijkstra(self):
        for vertex in self.getVertexes():
            vertex.minDistance = float('inf')
            vertex.previousVertex = None

    def getVertexes(self):
        return self.vertexes