# Shortest_Path_in_Graphs

The purpose of this project was to compare different shortest path finding algorithms.
We have used the real map of the New York City from [source](http://www.diag.uniroma1.it//~challenge9/download.shtml). This graph has 264,346 nodes and 733,846 edges.
We will now compare multiple algorithms to find shortest path from point A to point B on the same map. Some algorithms might be better than the other in some specific situations, to take care of this we use 1000 queries and consider total time taken to process these 1000 queries will be considered to compare these algorithms.
<br/>

The first algorithm, when talking about shortest path in graphs, is Dijkstra's Algorithm.
## Dijkstra:
Displayed here is the first query. We have to travel from the point on the right to the point on the left. We have plotted all the nodes in colour blue and all the processed nodes in colour red. You can see that all the nodes inside a circle of radius roughly equal to the shortest path have been processed. Processing 1000 queries took around 1152 seconds, roughly more than 1 second per query.<br> 

![Dijkstra's Algorithm](https://github.com/TRAGIC11/Shortest_Path_in_Graphs/blob/main/images/Dijkstra.png) <br>

> Time taken: 1151.855808019638 secs

Looking at the previous image, we feel there is room for major improvement. Instead of making 1 big circle around the source node, what if we make 2 small circles around target and source node each. The total area of two small circles is half the area of the big circle, this suggests that this algorithm would be twice as fast than the Dijkstra's algorithm.

## Bidirectional Dijkstra:
First look at the map and you know Bidirectional Dijkstra is going to be faster than the normal Dijkstra's algorithm. But how much fast? Turns out that this algorithm took only 295 seconds to process all the 1000 queries!!!<br>
Almost 4 times faster than the Dijkstra's.<br> 
![Bidirectional Dijkstra's Algorithm](https://github.com/TRAGIC11/Shortest_Path_in_Graphs/blob/main/images/Bi_Dijkstra.png) <br>

> Time taken: 294.5640931129455 secs

We can still see that these algorithms lack the sense of direction in which they should head.

## A* Algorithm:
Well A* algorithm seems to know in which direction you should head. This algorithm processes even less nodes. Total time taken here is 155 seconds to process all the 1000 queries. <br>
![A* Algorithm](https://github.com/TRAGIC11/Shortest_Path_in_Graphs/blob/main/images/Astar.png) <br>

> Time taken: 154.3322422504425 secs

A* algorithm was a big improvement. We can now process each query in less than 1/5th of a second. Can there be any faster algorithm?

## Contraction Hierarchies:
Contraction Hierarchies add shortcuts between nodes based on few heuristics. To add these shortcuts, we need to preprocess the graph and assign rank to each of the node which later helps during querying. Preprocessing took 159 mins, or 2 hours and 49 mins. This would have been faster but turns out python is bad at memory handling. I observed that 95 % of the nodes were preprocessed within first 10 mins. <br> 
Although the preprocessing takes so a lot of time, querying looks very fast. It processed all the 1000 queries in around 14 seconds!!! This is around 80 times faster than the Dijstra's algorithm.<br>
You can see in the image below why contraction hierarchies are so fast, it processes very little number of nodes. Hardly anything compared to Dijkstra's algorithm.<br>
![Contraction Hierarchies](https://github.com/TRAGIC11/Shortest_Path_in_Graphs/blob/main/images/Contraction_Hierarchies.png) <br>


> Time taken to Preprocess: 10153 seconds

> Time taken to Query     : 14.02899217605591 secs

#### Coming soon:
>Highway Hierarchies
