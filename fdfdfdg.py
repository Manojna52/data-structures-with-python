class graph:
    def __init__(self,gdict):
        if gdict is None:
            gdict=[]
        self.gdict=gdict

    def vertex(self):
        return list(self.gdict.keys())
    def edges(self):
        a=[]
        for nxt in self.gdict:
            for i_nxt in self.gdict[nxt]:
                if {nxt,i_nxt} not in a:
                    a.append({nxt,i_nxt})
        return a
def dfs(start,graph,vibt=None):
    if vibt is None:
        vibt=set()
    vibt.add(start)
    print(start)
    for next in graph[start]-vibt:
        dfs(next,graph,vibt)
    return vibt
    
        
                



        
graph_ele={"a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["d"])
           }
ii=graph(graph_ele)
print(ii.gdict)
print(ii.vertex())
print(ii.edges())
dfs("a",graph_ele)
