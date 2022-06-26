import heapq
# import numpy as np
from math import radians,sin, cos, asin, sqrt
# from math import sqrt
import matplotlib.pyplot as plt

class AStar:
    def __init__(self, n, adj, cost, x, y):
        self.n = n
        self.adj = adj
        self.cost = cost
        self.inf = n*10**6
        self.p = {}
        self.d = [self.inf]*n
        self.workset = set()
        self.x = x
        self.y = y


    def clear(self):
        for v in self.workset:
            self.d[v] = self.inf
        self.p.clear()
        self.workset = set()


    def visit(self, q, t, v, dist):
        for u,w in zip(self.adj[v], self.cost[v]):
            if self.d[u]>dist+w:
                self.d[u] = dist+w
                self.workset.add(u)
                heapq.heappush(q, (dist + w + self.pi(u,t), u, dist+w))


    def pi(self,u,t):
        if u not in self.p:
            r = 6400e4
            #haversine formula
            lon1, lat1, lon2, lat2 = map(radians, [self.x[u], self.y[u], self.x[t], self.y[t]])
            dlon = lon2 - lon1
            dlat = lat2 - lat1
            a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
            self.p[u] = 2 * r * asin(sqrt(a))
        return self.p[u]


    # def pi(self,u,t):
    #     if u not in self.p:
    #         self.p[u] = sqrt((self.x[u]-self.x[t])**2 + (self.y[u]-self.y[t])**2)
    #     return self.p[u]*0.91


    def query(self, s, t):
        self.clear()
        q = []
        heapq.heappush(q, (self.pi(s,t), s, 0))
        while q:
            _,v,dist = heapq.heappop(q)
            if v == t:
                return min(dist, self.d[t])
            self.visit(q,t, v, dist)
        return -1


    def query1(self, s, t):
        self.clear()
        q = []
        heapq.heappush(q, (self.pi(s,t), s, 0))
        travelledx = []
        travelledy = []
        while q:
            max_d,v,dist = heapq.heappop(q)
            travelledx.append(self.x[v])
            travelledy.append(self.y[v])
            if v == t:
                plt.scatter(self.x,self.y,s = 0.1)
                plt.scatter(travelledx,travelledy,s=0.1,c='r')
                plt.scatter(self.x[s],self.y[s],c = 'black')
                plt.scatter(self.x[t],self.y[t],c = 'black')
                return min(dist, self.d[t])
            self.visit(q,t, v, dist)
        return -1