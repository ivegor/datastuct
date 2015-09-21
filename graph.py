__author__ = 'air'


class Graph:

    def __init__(self):
        self.vert_list = {}
        self.num_verts = 0

    def add_vertex(self, key):
        self.num_verts += 1
        new_vertex = Vertex(key)
        self.vert_list[key] = new_vertex
        return new_vertex

    def get_vertex(self, key):
        if key in self.vert_list:
            return self.vert_list[key]
        return None

    def __contains__(self, item):
        return item in self.vert_list

    def add_edge(self, ver1, ver2, weight=0):
        if ver1 not in self.vert_list:
            self.add_vertex(ver1)
        if ver2 not in self.vert_list:
            self.add_vertex(ver2)
        self.vert_list[ver1].add_neighbor(self.vert_list[ver2], weight)

    def get_vertices(self):
        return self.vert_list.keys()

    def __iter__(self):
        return iter(self.vert_list.values())


class Vertex:

    def __init__(self, key):
        self.id = key
        self.connected = {}

    def add_neighbor(self, nbr, weight):
        self.connected[nbr] = weight

    def __str__(self):
        if self.connected:
            return str(self.id) + " connected to " + str(x.id for x in self.connected)
        return str(self.id) + " w/o connecting"

    def get_connections(self):
        return self.connected.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected[nbr]

if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        print(g.add_vertex(i))
    g.add_edge(0,1,5)
    g.add_edge(0,5,2)
    g.add_edge(1,2,4)
    g.add_edge(2,3,9)
    g.add_edge(3,4,7)
    g.add_edge(3,5,3)
    g.add_edge(4,0,1)
    g.add_edge(5,4,8)
    g.add_edge(5,2,1)
    for v in g:
        for w in v.get_connections():
            print("( %s , %s )" % (v.get_id(), w.get_id()), v.get_weight(w))


