import heapq

class BiDij:
    def __init__(self, n):
        self.n = n;                             # Number of nodes
        self.inf = n*10**6                      # All distances in the graph are smaller
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.visited = [[False]*n,[False]*n]    # visited[v] == True iff v was visited by forward or backward search
        self.workset = [set(),set()]            # All the nodes visited by forward or backward search
        self.adj = []
        self.cost = []

    def define_values(self, adj, cost):
        self.cost = cost
        self.adj = adj

    def clear(self):
        """Reinitialize the data structures for the next query after the previous query."""
        for v in self.workset[0]:
            self.visited[0][v] = False
            self.d[0][v] = self.inf
            self.visited[1][v] = False
            self.d[1][v] = self.inf
        for v in self.workset[1]:
            self.visited[0][v] = False
            self.d[0][v] = self.inf
            self.visited[1][v] = False
            self.d[1][v] = self.inf
        self.workset = [set(),set()]

    def visit(self, q, side, v, dist):
        """Try to relax the distance to node v from direction side by value dist."""
        # Implement this method yourself
        self.visited[side][v] = True
        self.d[side][v] = dist
        for u,w in zip(self.adj[side][v],self.cost[side][v]):
            if not self.visited[side][u]:
                if dist+w < self.d[side][u]:
                    self.d[side][u] = dist+w
                    #q[side].put((dist+w,u))
                    heapq.heappush(q[side],(self.d[side][u],u))
                    self.workset[side].add(u)

    def process(self):
        """Return the distance to node v from the source node."""
        dist = self.inf
        for v in self.workset[0]:
            dist = min(dist, self.d[0][v]+self.d[1][v])
        for v in self.workset[1]:
            dist = min(dist, self.d[1][v]+self.d[0][v])
        return dist

        
    def query(self, adj, cost, s, t):
        if s==t:
            return 0
        self.clear()
        self.workset[0].add(s)
        self.workset[1].add(t)
        q = [[],[]] 
        self.visit(q, 0, s, 0)
        self.visit(q, 1, t, 0)
        
        #while not q[0].empty() and not q[1].empty():
        while q[0] and q[1]:
            #d,u = q[0].get()
            d,u = heapq.heappop(q[0])
            if not self.visited[0][u]:
                self.visit(q, 0, u, d)
            if self.visited[1][u]:
                return self.process()

            #d,u = q[1].get()
            d,u = heapq.heappop(q[1])
            if not self.visited[1][u]:
                self.visit(q, 1, u, d)
            if self.visited[0][u]:
                return self.process()
        
        return -1