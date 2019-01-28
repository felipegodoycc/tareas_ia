from tkinter import *
from time import time
import decimal

inicial = [0,0,1,1,0,1,1,0,1,0,1,1,1,0,0,1,1,1,0,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0]
prueba =  [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
patron110 = [	['000',0],
				['001',1],
				['010',1],
				['011',0],
				['100',1],
				['101',0],
				['110',0],
				['111',1]]

patron30 = 	[	['000',0],
				['001',1],
				['010',1],
				['011',1],
				['100',1],
				['101',0],
				['110',0],
				['111',0]]

def mostrar(lista):
	for i in lista:
		print(i,end="")
	print()

def buscar(s,ptr):
	for i in range(len(ptr)):
		if(s == ptr[i][0]):
			return ptr[i][1]

def lista_to_string(lista):
	temp = ""
	for i in lista:
		temp = temp + str(i)
	return temp


def dibujar_matriz(n,m,matriz,tam=10,inix=5,iniy=5):
	tam=800/n
	for i in range(n):
		for j in range(m):
			if(matriz[j][i]== 0):
				cuadrado = areaDibujo.create_rectangle((inix+i*tam),(iniy+j*tam),(tam+inix+i*tam),(tam+iniy+j*tam),fill = "white")
			elif(matriz[j][i]==1):
				cuadrado = areaDibujo.create_rectangle((inix+i*tam),(iniy+j*tam),(tam+inix+i*tam),(tam+iniy+j*tam),fill = "black")
	ti = Label(ventana, text = "Tiempo de ejecucion " + tem.get() + " segundos").place(x=10,y=750)

def semilla_default():
	temp = lista_to_string(prueba)
	text.set(temp)
def generacion_default():
	gen.set(21)

def un_celular(ini,patron):
	temp = []
	l= len(ini)
	s = str(ini[-1]) + str(ini[0]) + str(ini[1])
	temp.append(buscar(s,patron))
	i = 0
	while (len(temp)<l):
		if(i == l-1):
			s = str(ini[i]) + str(ini[0]) + str(ini[1])
		elif(i == l-2):
			s = str(ini[i]) + str(ini[i+1]) + str(ini[0])
		else:
			s = str(ini[i]) + str(ini[i+1]) + str(ini[i+2])
		i=i+1
		if(i==l):
			i=0
		temp.append(buscar(s,patron))
		#a = s + " -> " + str(buscar(s,patron30))
		
		#print(a)
	#mostrar(temp)
	return temp

def celular_n(ini,n,patron):
	matriz = []
	matriz.append(ini)
	#mostrar(prueba)

	if(n == 1):
		return matriz

	aux = un_celular(ini,patron)
	matriz.append(aux)

	if(n == 2):
		return matriz

	else:
		for i in range(n-2):
			aux = un_celular(aux,patron)
			matriz.append(aux)
		return matriz

def dibujar():
	rec = areaDibujo.create_rectangle(5,5,799,599,fill="White")
	tini= time()
	s = []
	ptr = []
	for i in text.get():
		s.append(int(i))
	if(opcion.get() == 1):
		for i in patron30:
			ptr.append(i)
	elif(opcion.get()==2):
		for i in patron110:
			ptr.append(i)
	m = celular_n(s,gen.get(),ptr)
	dibujar_matriz(len(s),len(m),m)
	tfin= time()
	tiempo=tfin-tini
	a = "%8.6f" % tiempo
	tem.set(a)

ventana = Tk()											#constructor,se inicia script de interfaz grafica
tiempo=0
tem = StringVar()
gen = IntVar()
text = StringVar()
semilla_default()
generacion_default()
opcion = IntVar()
opcion.set(1)
areaDibujo = Canvas(ventana,width=800,height=600)		#constructor, se inicia area de dibujo
rec = areaDibujo.create_rectangle(5,5,799,599)
ventana.geometry("1200x800")								#tamaño de la ventana
areaDibujo.place(x=200,y=50)								#se posiciona area de dibujo
ventana.title("Automata Celular")						#titulo de ventana
titulo = Label(ventana, text = "AUTOMATA CELULAR", font= "Verdana 20" ).pack()
pat = Label(ventana, text = "Seleccione patron: ").place(x=10,y=650)
pat30 = Radiobutton(ventana,text = "Patron 30",value=1,variable=opcion).place(x=10,y=680)
pat110 = Radiobutton(ventana,text = "Patron 110",value =2,variable=opcion).place(x=10,y=700)
semi = Label(ventana, text = "Ingrese semilla: ").place(x=180,y=650)
sem = Entry(ventana, textvariable = text,width=60).place(x=180,y=680)
default = Button(ventana, text = "Por Defecto", command = semilla_default).place(x=180,y=710)
iterr = Label(ventana,text="Ingrese numero de generaciones: ").place(x=600,y=650)
generacion = Entry(ventana, textvariable = gen,width=10).place(x=600,y=680)
defecto = Button(ventana, text = "Por defecto", command = generacion_default).place(x=600,y=710)
generar = Button(ventana, text = "RUN", command = dibujar ,width=30,height=5).place(x=900,y=650)
ventana.mainloop()										#finaliza e inicia la interfaz
