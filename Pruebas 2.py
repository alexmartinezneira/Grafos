import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators import line
import graphviz



G=nx.Graph()
ar="Matriz_grafo.csv"


for i in range(70):
    G.add_node(str(i+1))

with open(ar,'r') as archivo:
    contador=0
    for linea in archivo:
        linea=linea.split(',')
        contador+=1
        for i in range(len(linea[:-1])):
            if(float(linea[i])!=0):
                G.add_edge(str(contador),str(i+1))
                G[str(contador)][str(i+1)]['weight']=float(linea[i])
                #print(contador,str(i+1),linea[i])
                
print(G)


#start,end=input("Ingrese los nodos de inicio y fin separados por espacios:").split()
#path=nx.dijkstra_path(G, source=start, target=end)
#print('Ruta del nodo {0} a {1}:'.format(start,end), path)
#distance=nx.dijkstra_path_length(G, source=start, target=end)
#print('La distancia desde el nodo {0} a {1} es:'.format(start,end), distance)
#
#dfs_output = list(nx.dfs_preorder_nodes(G))
#print(dfs_output)

#bfs=list(nx.edge_bfs(G,0))
#print(bfs)
#T = nx.minimum_spanning_tree(G)
#1print(sorted(T.edges(data=True)))