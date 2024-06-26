from deap import algorithms
from deap import base
from deap import creator
from deap import tools
from problema import PERSONAJES
from problema import AMIGOS
from problema import COLORES
from problema import TAM_DISFRAZ
from problema import CANT_DISFRACES
from problema import funcion_puntaje
from problema import crear_ind
from problema import imprimir_ind
import numpy

import matplotlib.pyplot as plt
import seaborn as sns

# Busca el mayor peso
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# Crea individuo
creator.create("Individual", list, fitness=creator.FitnessMax, strategy=None)

creator.create("Strategy", list, typecode="d")

# Registra
toolbox = base.Toolbox()

IND_SIZE = TAM_DISFRAZ * CANT_DISFRACES
# función creadora de individuo
toolbox.register("individual", crear_ind, creator.Individual, creator.Strategy)
# función creadora de población
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
# función evaluadora de pesos
toolbox.register("evaluate", funcion_puntaje)
toolbox.register("select", tools.selTournament, tournsize=4)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=3, indpb=0.1)

pop = toolbox.population(n=100)

hof = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)

stats.register("avg", numpy.mean, axis=0)
stats.register("std", numpy.std, axis=0)
stats.register("min", numpy.min, axis=0)
stats.register("max", numpy.max, axis=0)

# Evolución
ngen = 100
npop = 1000
pop, logbook = algorithms.eaMuPlusLambda(pop, toolbox, mu=npop, lambda_=npop, cxpb=0.7, mutpb=0.3, ngen=ngen, stats=stats, halloffame=hof)

best_solution = tools.selBest(pop, 1)[0]
print("\nMEJOR SOLUCIÓN:")
print("")
print(best_solution)

imprimir_ind(best_solution)

# Historial AVG
plt.figure(figsize=(10, 8))
front = numpy.array([(c['gen'], c['avg'][0]) for c in logbook])
plt.plot(front[:, 0][1:-1], front[:, 1][1:-1], "-bo", c="b")
plt.axis("tight")
plt.show()