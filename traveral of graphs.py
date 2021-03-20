class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict={}
        self.gdict=gdict
def dfs(start,graph,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    print(start)
    for next in graph[start]-visited:
        dfs(next,graph,visited)
    return visited

gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }
dfs("a",gdict)
