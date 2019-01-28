#Se importa la librería sklearn el módulo tre

from sklearn import tree
import graphviz

#Se crea la instancia del árbol de decisión.

clf = tree.DecisionTreeClassifier()




xnames = ["enciende","muestra imagen","acceso al escritorio","lento"]
X = [[1, 1, 1, 0],
     [0, 0, 0, 0],
     [1, 1, 0, 1],
     [1, 1, 1, 1],
     [1, 0, 0, 0],
]

#La salida donde se dice si es hombre o mujer

Y = ['bueno', 'dañado', 'falla so', 'falla disco duro',"daño placa madre"]

#Se le pasa los datos  X y Y
clf = clf.fit(X, Y)

#Se definen los datos 1 y 2

dato1 = [1,0,0,1]

prediction = clf.predict([dato1])
print(prediction)
dot_data = tree.export_graphviz(clf, out_file=None, feature_names=xnames, class_names=Y,filled=True, rounded=True,special_characters=True)
graph = graphviz.Source(dot_data)
graph.render("arbol")


# Se consulta por un computador que enciende, no muestra imagen, no inicia el escritorio y es lento