
from flask import  Flask,render_template,redirect,url_for,request
import networkx as nx
import matplotlib.pyplot as plt
from networkx.generators import line
import graphviz

def Crear_Grafo(ar):
	G=nx.Graph()
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
	nx.draw(G,with_labels = True)  # Dibujar el grafo G con los atributos especificados
	plt.savefig("Grafo.jpg")  # Mostrar el grafo G por pantalla

	return(G)

def BFS(grafo):
	G=grafo
	bfs=list(nx.edge_bfs(G))
	return(bfs)

def Dijkstra(grafo, start,end):
	G=grafo
	path=nx.dijkstra_path(G, source=start, target=end)
	ruta=( path)
	distance=nx.dijkstra_path_length(G, source=start, target=end)
	distancia=( distance)
	bencina=(distancia/13)*1037
	li=distancia/13
	litros=round(li,3)
	return ruta,distancia,bencina,litros

def DFS(grafo):
	G=grafo
	dfs = list(nx.dfs_preorder_nodes(G))
	return(dfs)

def Kruskal(grafo):
	G=grafo
	T = nx.minimum_spanning_tree(G)
	return(sorted(T.edges(data=True)))

archivo="Matriz_grafo.csv"
grafo=Crear_Grafo(archivo)









app=Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route("/algoritmos",methods=["POST","GET"])
def login():
	bandera=False
	if(request.method=="POST"):
		algoritmo=request.form["algoritmo"]
		
		if(algoritmo=="BFS"):
			bfs=BFS(grafo)
			
			return redirect(url_for("bfs",alg=bfs,b=bandera))
			
		if(algoritmo=="DFS"):
			dfs=DFS(grafo)
			return redirect(url_for("dfs",alg=dfs,b=bandera))


		if(algoritmo=="DIJ"):
		
			inicio=request.form["inicio"]
			final=request.form["final"]
			ruta=Dijkstra(grafo,inicio,final)[0]
			distancia=Dijkstra(grafo,inicio,final)[1]
			bencina=Dijkstra(grafo,inicio,final)[2]
			litros=Dijkstra(grafo,inicio,final)[3]
			return redirect(url_for("dij",ru=ruta,b=distancia,ben=round(bencina),lt=litros))


		if(algoritmo=="KRU"):
			kru=Kruskal(grafo)
			return redirect(url_for("kru",alg=kru,b=bandera))
	else:
		return render_template("login.html")



@app.route("/bfs<alg>,<b>")
def bfs(alg,b):
	s=alg
	return render_template("bfs.html",alg=s,bandera=b)
@app.route("/dfs<alg>,<b>")
def dfs(alg,b):
	s=alg
	return render_template("dfs.html",alg=s,bandera=b)

@app.route("/dij<ru>,<b>,<ben>,<lt>")
def dij(ru,b,ben,lt):
	ruta=ru
	distancia=b
	bencina=ben
	litros=lt
	return render_template("dij.html",rut=ruta,dis=distancia,a=bencina,l=litros)

@app.route("/kru<alg>,<b>")
def kru(alg,b):
	s=alg
	return render_template("kru.html",alg=s,bandera=b)
	






if __name__ == '__main__':
	app.run(debug=True)