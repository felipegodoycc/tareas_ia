import math
from pomegranate import *

feliz = DiscreteDistribution({'F': 0.8 , 'NF': 0.2})

comida = DiscreteDistribution({'HC': 0.6 , 'NHC' : 0.4 })

come = ConditionalProbabilityTable(
    [['F', 'HC', 'C', 0.8],
     ['F', 'HC', 'NC', 0.2],

     ['NF', 'HC', 'C', 0.5],
     ['NF', 'HC', 'NC', 0.5],

     ['NF', 'NHC', 'C', 0],
     ['NF', 'NHC', 'NC', 1],

     ['F', 'NHC', 'C', 0],
     ['F', 'NHC', 'NC', 1]],[feliz,comida])

s1 = State(feliz, name="Feliz")
s2 = State(comida, name="Comida")
s3 = State(come, name= "Come comida")

model = BayesianNetwork("Mascota Culia")

model.add_states(s1, s2, s3)

model.add_edge(s1, s3)
model.add_edge(s2, s3)


model.bake()

print(model.probability(['F', 'HC', None]))

