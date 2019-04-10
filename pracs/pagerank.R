library(igraph)
A=matrix(c(0,1/2,1/2,0,0,0,1/6,1/6,1/6,1/6,1/6,1/6,1/3,1/3,0,0,1/3,0,0,0,0,0,1/2,1/2,0,0,0, 1/2,0,1/2,0,0,0,1,0,0),nrow=6)
graph1=graph.adjacency(A,weighted = "True" ,mode = "directed")
plot(graph1)