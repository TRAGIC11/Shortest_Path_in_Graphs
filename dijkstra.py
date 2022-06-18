import queue

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