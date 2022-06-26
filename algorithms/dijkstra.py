import queue
import matplotlib.pyplot as plt

def dijkstra(adj, cost, s, t):
    #write your code here
    n = len(adj)
    travelled = [False for i in range(n)]
    dist = [float('inf') for i in range(n)]
    dist[s] = 0
    travelled[s] = 0
    # use djikstra 
    q = queue.PriorityQueue()
    q.put((0, s))
    while not q.empty():
        a,b = q.get()
        if travelled[b] == True:
            continue
        travelled[b] = True
        dist[b] = a
        if dist[t] != float('inf'):
            return dist[t]
        for i in range(len(adj[b])):
            if travelled[adj[b][i]] == False:
                q.put((a+cost[b][i], adj[b][i]))
    return -1

def dijkstra1(adj, cost, s, t, x, y):
    #write your code here
    n = len(adj)
    travelled = [False for i in range(n)]
    dist = [float('inf') for i in range(n)]
    dist[s] = 0
    travelled[s] = 0
    # use djikstra 
    q = queue.PriorityQueue()
    q.put((0, s))
    travelledx = []
    travelledy = []
    while not q.empty():
        a,b = q.get()
        if travelled[b] == True:
            continue
        travelledx.append(x[b])
        travelledy.append(y[b])
        
        travelled[b] = True
        dist[b] = a
        if dist[t] != float('inf'):
            plt.scatter(x,y,s=0.1)
            plt.scatter(travelledx,travelledy,s=0.1,c = 'r')
            plt.scatter(x[s],y[s],c = 'black')
            plt.scatter(x[t],y[t],c = 'black')
            return dist[t]
        for i in range(len(adj[b])):
            if travelled[adj[b][i]] == False:
                q.put((a+cost[b][i], adj[b][i]))
    return -1