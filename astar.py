import heapq
import math

class AStar:
    def __init__(self, n, adj, cost, x, y):
        # See the explanations of these fields in the starter for friend_suggestion        
        self.n = n
        self.adj = adj
        self.cost = cost
        self.inf = n*10**6
        self.p = {}
        self.d = [self.inf]*n
        #self.visited = [False]*n
        self.workset = set()
        # Coordinates of the nodes
        self.x = x
        self.y = y

    # See the explanation of this method in the starter for friend_suggestion
    def clear(self):
        for v in self.workset:
            self.d[v] = self.inf
            #self.visited[v] = False
        self.p.clear()
        self.workset = set()

    # a* algorithm

    # See the explanation of this method in the starter for friend_suggestion
    def visit(self, q, t, v, dist):
        # Implement this method yourself
        for u,w in zip(self.adj[v], self.cost[v]):
            if self.d[u]>dist+w:
                self.d[u] = dist+w
                self.workset.add(u)
                heapq.heappush(q, (dist + w + self.pi(u,t), u, dist+w))


    def pi(self,u,t):
        if u in self.p:
            return self.p[u]
        else:
            self.p[u] = math.sqrt((self.x[u]-self.x[t])**2 + (self.y[u]-self.y[t])**2)
            return self.p[u]

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        self.clear()
        #print(self.d)
        q = []
        heapq.heappush(q, (self.pi(s,t), s, 0))
        while q:
            _,v,dist = heapq.heappop(q)
            if v == t:
                return min(dist, self.d[t])
            self.visit(q,t, v, dist)

        # Implement the rest of the algorithm yourself
        return -1