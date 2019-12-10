from collections import defaultdict
class graph(object):
    def __init__(self):
        self.nodes=defaultdict(list)

    def addEdge(self,val1, val2):
        self.nodes[val1].append(val2)


    def BFS(self, start):
        visited=[False]*len(self.nodes)
        queue=[start]
        visited[start]=True
        while queue:
            s=queue.pop(0)
            print(s)

            for i in self.nodes[s]:
                if not visited[i]:
                    visited[i]=True
                    queue.append(i)

    def _dfs(self, v, visited):
        print(v)
        for i in self.nodes[v]:
            if not visited[i]:
                visited[i] = True
                self._dfs(i, visited)
        return

    def DFS(self, start):
        visited=[False]*len(self.nodes)
        visited[start]=True
        self._dfs(start, visited)

if __name__ == "__main__":
    g=graph()
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(2,0)
    g.addEdge(2,3)
    g.addEdge(3,3)

    g.BFS(2)
    g.DFS(2)