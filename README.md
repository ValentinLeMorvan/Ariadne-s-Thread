Ariadne-s-Thread
================

###Ariadne's Thread - AG44 (Graph Theory and applications) project

### Objectives

- Parsing a text fils containing a matrix into a usable data structure representing a graph

- Finding the strongly connected components of the graph

- Finding the starting point of the newly obtained graph

- Finding the longest path between the starting points and the end

### Implementation

The programm is writen in Python.

The input file contain the size of the matrix on the first line, then the matrix representing the graph.

The original graph is represented into its adjacency matrix. After finding the strongly connected components, the new graph is represented as matrix giving the number of edges between each components.

The strongly connected components are found using the Path-based algorithm.

The longest path is found using the Bellman Ford algorithm.
