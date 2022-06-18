import heapq
from collections import defaultdict

maxlen = 2 * 10**6

class DistPreprocessSmall:
    def __init__(self, n, adj, cost):
        # See description of these parameters in the starter for friend_suggestion
        self.n = n
        self.INFINITY = n * maxlen
        self.adj = adj
        self.cost = cost
        self.bidistance = [[self.INFINITY] * n, [self.INFINITY] * n]
        self.visited = [[False]*n,[False]*n]    # visited[v] == True iff v was visited by forward or backward search
        self.workset = set()           # All the nodes visited by forward or backward search
        self.q = []
        # Levels of nodes for node ordering heuristics
        self.level = [0] * n
        # Positions of nodes in the node ordering
        self.rank = [-1] * n
        # Number of contracted Neighbors
        self.contracted_neighbors = [0] * n
        
        # Implement preprocessing here
        self.preImportance()
        self.preprocess()


    def preImportance(self):
        for v in range(self.n):
            importance,_ = self.shortcut(v)
            heapq.heappush(self.q, (importance, v))
        
    def preprocess(self):
        rank1 = 0
        while self.q:
            _, first  = heapq.heappop(self.q)
            if self.q:
                importance2, second = heapq.heappop(self.q)
                importance1,shortcuts = self.shortcut(first)
                if importance1 <= importance2:
                    for shortcut in shortcuts:
                        self.add_arc(shortcut[0], shortcut[1], shortcut[2])
                    for i,u in enumerate(self.adj[0][first]):
                        self.level[u] = max(self.level[u], self.level[first] + 1)
                        self.contracted_neighbors[u] += 1
                    for i,u in enumerate(self.adj[1][first]):
                        self.level[u] = max(self.level[u], self.level[first] + 1)
                        self.contracted_neighbors[u] += 1
                    self.rank[first] = rank1
                    rank1 += 1
                else:
                    heapq.heappush(self.q, (importance1, first))
                heapq.heappush(self.q, (importance2, second))
            elif self.rank[first] == -1:
                _,shortcuts = self.shortcut(first)
                for shortcut in shortcuts:
                    self.add_arc(shortcut[0], shortcut[1], shortcut[2])
                    for i,u in enumerate(self.adj[0][first]):
                        self.level[u] = max(self.level[u], self.level[first] + 1)
                        self.contracted_neighbors[u] += 1
                    for i,u in enumerate(self.adj[1][first]):
                        self.level[u] = max(self.level[u], self.level[first] + 1)
                        self.contracted_neighbors[u] += 1
                self.rank[first] = rank1


    def add_arc(self, u, v, c):
        def update(adj, cost, u, v, c):
            for i in range(len(adj[u])):
                if adj[u][i] == v:
                    cost[u][i] = min(cost[u][i], c)
                    return
            adj[u].append(v)
            cost[u].append(c)

        update(self.adj[0], self.cost[0], u, v, c)
        update(self.adj[1], self.cost[1], v, u, c)

    # Makes shortcuts for contracting node v
    def shortcut(self, v):
        # Compute the node importance in the end
        shortcut_cover_set = set()
        shortcuts = []
        # Compute correctly the values for the above heuristics before computing the node importance
        maxOutgoing = max(self.cost[0][v]) if len(self.adj[0][v]) else 0
        #maxIncoming = max(self.cost[1][v]) if len(self.adj[1][v]) else 0
        for i,source in enumerate(self.adj[1][v]):
            if self.rank[source] != -1:
                continue
            Incoming = self.cost[1][v][i]
            dist = self.dijkstra(v, source, Incoming + maxOutgoing)
            for j,target in enumerate(self.adj[0][v]):
                if self.rank[target] != -1:
                    continue
                if self.cost[1][v][i] + self.cost[0][v][j] <= dist[target]:
                    shortcuts.append((source, target, self.cost[1][v][i] + self.cost[0][v][j]))
                    shortcut_cover_set.add(source)
                    shortcut_cover_set.add(target)

        edge_difference = len(shortcuts) - len(self.adj[0][v]) - len(self.adj[1][v])
        neighbors = self.contracted_neighbors[v]
        shortcut_cover = len(shortcut_cover_set)
        level = self.level[v]

        a,b,c,d = 1,1,1,1
        importance = a*edge_difference + b*neighbors + c*shortcut_cover + d*level
        return importance, shortcuts

    def dijkstra(self, v, s, max_dist):
        dist = defaultdict(lambda: self.INFINITY)
        queue = []
        jumps = 5
        dist[s] = 0
        heapq.heappush(queue, (0, s,jumps))
        while queue:
            d, u,j = heapq.heappop(queue)
            if j ==0:
                continue
            if d>max_dist :
                break
            for i,w in enumerate(self.adj[0][u]):
                if w != v and dist[w] > d + self.cost[0][u][i]:
                    dist[w] = d + self.cost[0][u][i]
                    heapq.heappush(queue, (dist[w], w,j-1))
        return dist


    # See description of this method in the starter for friend_suggestion
    def clear(self):
        for v in self.workset:
            self.bidistance[0][v] = self.bidistance[1][v] = self.INFINITY
            self.visited[0][v]    = self.visited[1][v]    = False
        self.workset = set()

    # See description of this method in the starter for friend_suggestion
    def visit(self,queues, side, v, dist):
        # Implement this method yourself
        self.bidistance[side][v] = dist
        for u,w in zip(self.adj[side][v], self.cost[side][v]):
            if not self.visited[side][u] and self.rank[v] < self.rank[u]:
                heapq.heappush(queues[side], (dist + w, u))

    # Returns the distance from s to t in the graph
    def query(self, s, t):
        if s == t:
            return 0
        self.clear()
        queues = [[],[]]
        estimate = self.INFINITY

        self.workset.add(s)
        self.workset.add(t)
        heapq.heappush(queues[0], (0, s))
        heapq.heappush(queues[1], (0, t))
        
        while queues[0] or queues[1]:
            if queues[0]:
                dist,u = heapq.heappop(queues[0])
                if not self.visited[0][u]:
                    self.visit(queues, 0, u, dist)
                    self.visited[0][u] = True
                    self.workset.add(u)
                if self.visited[1][u]:
                    estimate = min(estimate, self.bidistance[0][u] + self.bidistance[1][u])
            if queues[1]:
                dist,u = heapq.heappop(queues[1])
                if not self.visited[1][u]:
                    self.visit(queues, 1, u, dist)
                    self.visited[1][u] = True
                    self.workset.add(u)
                if self.visited[0][u]:
                    estimate = min(estimate, self.bidistance[0][u] + self.bidistance[1][u])

        return -1 if estimate >= self.INFINITY else estimate