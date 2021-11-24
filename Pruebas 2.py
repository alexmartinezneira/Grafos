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
                #print(contador,str(i+1),linea[i])
                
print(G.edges)

nx.draw(G,with_labels = True)  # Dibujar el grafo G con los atributos especificados

plt.show()  # Mostrar el grafo G por pantalla

