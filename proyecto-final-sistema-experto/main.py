import re

from pyknow import *

# Entrada

class Problema(Fact):
    """Aqui declararemos los problemas de un computador"""
    pass

# Salida

class Diagnostico(Fact):
    """Aqui obtendremos el posible diagnostico al o los problemas"""
    pass

class Caso(Fact):
    """Aqui juntaremos casos con diagnostico"""
    pass

class Diagnosticos(KnowledgeEngine):
    @DefFacts()
    def diags(self):
        problemas = open('Problemas.txt','r')
        diagnosticos = open('Diagnostico.txt','r')
        p = problemas.readlines()
        d = diagnosticos.readlines()
        a=[]
        b=[]
        for line in p:
            a.append(line.rstrip('\n').split(','))
        for line in d:
            b.append(line.rstrip('\n').split(','))

        for item in a:
            d=""
            c=""
            for diag in b:
                if(diag[0] == item[3]):
                    d=diag[2]
                    c=diag[1]

            yield Caso(
                p1=item[0],
                p2=item[1],
                p3=item[2],
                diag=d,
                tipo=c)

    @Rule(Problema())
    def mensaje(self):
        self.declare(Diagnostico(id=1,diag="Fallo en placa madre"))

    @Rule(
        Caso(
            p1=MATCH.p1,
            p2=MATCH.p2,
            p3=MATCH.p3,
            diag=MATCH.d
        ),
        Problema(
            p1=MATCH.p1,
            p2=MATCH.p2,
            p3=MATCH.p3,
            id=MATCH.id
        )
    )
    def diagnostico(self,d,id):
        self.declare(Diagnostico(id=id,diag=d))

c = Diagnosticos()
c.reset()
opcion = 1
while(opcion != 0):
    print("MENU")
    print("1.- Obtener diagnostico")
    print("2.- Ingresar nuevo diagnostico")
    print("")
    print("0.- Salir")
    opcion = int(input("Ingrese opcion: "))

    if(opcion==1):
        ct = 0
        file = open('Problemas.txt','r')
        lineas = file.readlines()
        sintomas = []
        for linea in lineas:
            a = linea.split(',')
            for item in range(len(a)-1):
                sintomas.append(a[item])
        print("Sintomas:")
        for i in sintomas:
            print(str(ct+1)+".- "+ str(i))
            ct=ct+1
        op1 = int(input("Ingrese sintoma 1: "))
        op2 = int(input("Ingrese sintoma 2: "))
        op3 = int(input("Ingrese sintoma 3: "))
        c.reset()
        a = Problema(id=1,p1=sintomas[op1-1],p2=sintomas[op2-1],p3=sintomas[op3-1])
        c.declare(a)
        c.run()
        print(c.facts)
    if(opcion==2):
        s1 = input("Ingrese sintoma 1: ")
        s2 = input("Ingrese sintoma 2: ")
        s3 = input("Ingrese sintoma 3: ")
        print("Seleccione diagnostico:")
        sintomas = ['error en la fuente', 'fallos en la targeta grafica (gpu)', 'fallos en la memoria ram', 'fallos en la cpu', 'fallos en placa madre', 'fallos con el disco duro']
        ct=0
        for i in sintomas:
            print(str(ct+1)+'.- '+i)
            ct=ct+1
        op = int(input("Opcion seleecionada"))
        archivo = open('Problemas.txt','a')
        s = '\n'+s1+','+s2+','+s3+','+str(op-1)
        archivo.write(s)
        archivo.close()
        c.reset()