import random
from enum import IntEnum

PERSONAJES = IntEnum("PERSONAJE", ["PIRATA", "VAMPIRO", "HOMBRE_LOBO", "BRUJA"])
AMIGOS = IntEnum("AMIGO", ["LUCIA", "MARIO", "PEDRO", "JUAN"])
COLORES = IntEnum("COLOR", ["ROJO", "NEGRO", "VERDE", "AZUL"])

POS_AMIGO = 0
POS_COLOR = 1

TAM_DISFRAZ = 2
CANT_DISFRACES = 4


def imprimir_ind(ind):
    for i in range(CANT_DISFRACES):
        print("Personaje:", PERSONAJES(ind[i * TAM_DISFRAZ] + 1).name)
        print("\tAmigo:", AMIGOS(ind[i * TAM_DISFRAZ + POS_AMIGO] + 1).name)
        print("\tColor:", COLORES(ind[i * TAM_DISFRAZ + POS_COLOR] + 1).name)

def crear_ind(cls, str_cls):
    ind = cls()
    for i in range(CANT_DISFRACES * TAM_DISFRAZ):
        ind.append(random.randint(0, 3))
    
    ind.strategy = str_cls()
    return ind



def calcular_condiciones_a_cumplir(ind):
    puntos = 0

    # Verificar si el tamaño del cromosoma es correcto
    if len(ind) != TAM_DISFRAZ * CANT_DISFRACES:
        return puntos  # Retornar 0 si el tamaño es incorrecto

    # No repetir valores en los genes
    valores_unicos = set(ind)
    puntos += (CANT_DISFRACES * TAM_DISFRAZ - len(valores_unicos)) * 5

    # El pirata no es rojo
    if not (ind[PERSONAJES.PIRATA * TAM_DISFRAZ] == AMIGOS.LUCIA - 1 and ind[PERSONAJES.PIRATA * TAM_DISFRAZ + POS_COLOR] == COLORES.ROJO - 1):
        puntos += 5

    # Mario no es hombre lobo ni negro
    if not (ind[PERSONAJES.HOMBRE_LOBO * TAM_DISFRAZ] == AMIGOS.MARIO - 1 or ind[PERSONAJES.HOMBRE_LOBO * TAM_DISFRAZ + POS_COLOR] == COLORES.NEGRO - 1):
        puntos += 5

    # # La bruja es verde
    # if ind[PERSONAJES.BRUJA * TAM_DISFRAZ + POS_COLOR] == COLORES.VERDE - 1:
    #     puntos += 5

    # El vampiro es negro
    if ind[PERSONAJES.VAMPIRO * TAM_DISFRAZ + POS_COLOR] == COLORES.NEGRO - 1:
        puntos += 5

    return puntos



def calcular_restricciones(ind):
    puntos = 0

    # Lucía tiene el pirata o el rojo
    if not (ind[PERSONAJES.PIRATA * TAM_DISFRAZ] == AMIGOS.LUCIA - 1 or ind[PERSONAJES.PIRATA * TAM_DISFRAZ + POS_COLOR] == COLORES.ROJO - 1):
        puntos -= 3

    # Mario tiene el hombre lobo o el negro
    if not (ind[PERSONAJES.HOMBRE_LOBO * TAM_DISFRAZ] == AMIGOS.MARIO - 1 or ind[PERSONAJES.HOMBRE_LOBO * TAM_DISFRAZ + POS_COLOR] == COLORES.NEGRO - 1):
        puntos -= 3

    # # Pedro tiene la bruja o el verde
    # if not (ind[PERSONAJES.BRUJA * TAM_DISFRAZ] == AMIGOS.PEDRO - 1 or ind[PERSONAJES.BRUJA * TAM_DISFRAZ + POS_COLOR] == COLORES.VERDE - 1):
    #     puntos -= 3

    # Lucía tiene el vampiro o el negro
    if not (ind[PERSONAJES.VAMPIRO * TAM_DISFRAZ] == AMIGOS.LUCIA - 1 or ind[PERSONAJES.VAMPIRO * TAM_DISFRAZ + POS_COLOR] == COLORES.NEGRO - 1):
        puntos -= 3

    return puntos

def funcion_puntaje(ind):
    puntos = 0
    puntos += calcular_condiciones_a_cumplir(ind)
    puntos += calcular_restricciones(ind)

    return [puntos]