# Shortest_Path_in_Graphs

The purpose of this project was to compare different shortest path finding algorithms.
We have used the real map of the state of Delaware from [source](http://www.diag.uniroma1.it//~challenge9/data/tiger/). This graph has 49109 nodes and 60512 edges.
We have used 4 algorithms, which take 1000 queries and return the shortest distance for each of the queries.

## Dijkstra:
Time taken: 32.87926530838013

## Bidirectional Dijkstra:
Time taken: 5.849478006362915

## A* Algorithm:
Time taken: 252.84441208839417

## Contraction Hierarchies:
Time taken to Preprocess: 10.156567335128784

Time taken to Query     : 0.12765955924987793

# Conclusion

> Bidirectional Dijkstra has lower bound of being twice as fast as regular Dijkstra, but here you can see it is 5.6 times faster.

> A* algorithm is one of the most suitable algorithms for Maze related problems. But here you can see that it performs very slow on real world related problems. It is 7.7 times slower than regular Dijkstra.

> Contraction Hierarchies uses a number of heuristics to preprocess the data. We then use this preprocessed data to calculate the shortest path and we can see that Contraction Hierarchies work the fastest. It is 258 times faster than regular Dijkstra.
