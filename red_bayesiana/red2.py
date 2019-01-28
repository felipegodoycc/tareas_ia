import math
import matplotlib
from pomegranate import *

feliz = DiscreteDistribution({'F': 0.8 , 'NF': 0.2})

comida = DiscreteDistribution({'HC': 0.6 , 'NHC' : 0.4 })

despierto = DiscreteDistribution({'D': 0.8 , 'ND': 0.2})

come = ConditionalProbabilityTable(
    [
        ['F', 'HC', 'D', 'C', 0.8],['F', 'HC', 'D', 'NC', 0.2],

        ['F', 'HC', 'ND', 'C', 0],['F', 'HC', 'ND', 'NC', 1],

        ['F', 'NHC', 'D', 'C', 0],['F', 'NHC', 'D', 'NC', 1],

        ['F', 'NHC', 'ND', 'C', 0],['F', 'NHC', 'ND', 'NC', 1],

        ['NF', 'NHC', 'ND', 'C', 0],['NF', 'NHC', 'ND', 'NC', 1],

        ['NF', 'HC', 'D', 'C', 0.5 ],['NF', 'HC', 'D', 'NC', 0.5],

        ['NF', 'HC', 'ND', 'C', 0],['NF', 'HC', 'ND', 'NC', 1],

        ['NF', 'NHC', 'D', 'C', 0],['NF', 'NHC', 'D', 'NC', 1],
    ],[feliz,comida,despierto]
)

gesto = ConditionalProbabilityTable(
    [
        ['C', 'D', 'G', 0.8],['C', 'D', 'NG', 0.2],

        ['NC', 'D', 'G', 0.5],['NC', 'D', 'NG', 0.5],

        ['NC', 'ND', 'G', 0],['NC', 'ND', 'NG', 1],

        ['C', 'ND', 'G', 0],['C', 'ND', 'NG', 1],
    ],[come,despierto]
)

s1 = State(feliz, name="Feliz")
s2 = State(comida, name="Comida")
s3 = State(despierto, name="Despierto")
s4 = State(come, name="Come")
s5 = State(gesto, name="Gesto")

model = BayesianNetwork("Mascota culia 2")

model.add_states(s1,s2,s3,s4,s5)

model.add_edge(s1,s4)
model.add_edge(s2,s4)
model.add_edge(s3,s4)

model.add_edge(s3,s5)
model.add_edge(s4,s5)

model.bake()

model.plot()


F = input("Esta feliz? (F=SI, NF=NO): ")
C = input("Hay comida? (HC=SI, NHC= NO): ")
D = input("Esta despierto? (D=SI, ND=NO): ")

print("Probabilidad realize un gesto si come: "
      + str(model.probability([F,C,D,'C','G'])))

print("Probabilidad realize un gesto si no come: "
      + str(model.probability([F,C,D,'NC','G'])))