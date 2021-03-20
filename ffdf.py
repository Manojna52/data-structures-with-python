class graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict=[]
        self.gdict=gdict
        print(self.gdict)
    def get_vertices(self):
    
        return list(self.gdict.keys())
    def get_edges(self):
        a=[]
        for items in self.gdict:
            u=set()
            u=set(self.gdict[items])
            a.append(u)
        return a
        

graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)

print(g.get_vertices())
y=g.get_edges()
print(y)
