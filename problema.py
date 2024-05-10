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
    repite = False
    for i in range(CANT_DISFRACES):
        for j in range(CANT_DISFRACES):
            if i!=j:
                if (ind[i * TAM_DISFRAZ] == ind[j * TAM_DISFRAZ] or ind[i * TAM_DISFRAZ + POS_AMIGO] == ind[j * TAM_DISFRAZ + POS_AMIGO] or ind[i * TAM_DISFRAZ + POS_COLOR] == ind[j * TAM_DISFRAZ + POS_COLOR]):
                    repite = True
    if(not repite):
        puntos += 5

    # El disfraz de bruja era de color verde.
    if ind[PERSONAJES.BRUJA * TAM_DISFRAZ + POS_COLOR] == COLORES.VERDE - 1:
        puntos += 5

    # El disfraz de vampiro era de color negro.
    if ind[PERSONAJES.VAMPIRO * TAM_DISFRAZ + POS_COLOR] == COLORES.NEGRO - 1:
        puntos += 5
    
    return puntos



def calcular_restricciones(ind):
    puntos = 0

    # El disfraz de pirata no era de color rojo 
    if (ind[PERSONAJES.PIRATA * TAM_DISFRAZ + POS_COLOR] == COLORES.ROJO - 1):
        puntos -= 3

    # El disfraz de pirata no lo usaba Lucía.
    if (ind[PERSONAJES.PIRATA * TAM_DISFRAZ] == AMIGOS.LUCIA - 1):
        puntos -= 3

    # Mario no se disfrazó de hombre lobo.
    if (ind[PERSONAJES.HOMBRE_LOBO * TAM_DISFRAZ] == AMIGOS.MARIO - 1):
        puntos -= 3

    # Mario no usó un disfraz negro.
    for i in range(CANT_DISFRACES):
        if (ind[i * TAM_DISFRAZ + POS_AMIGO] == AMIGOS.MARIO -1 and ind[i * TAM_DISFRAZ + POS_COLOR] == COLORES.NEGRO - 1):
            puntos -= 3

    # El disfraz de bruja no lo usaba Pedro.
    if (ind[PERSONAJES.BRUJA * TAM_DISFRAZ] == AMIGOS.PEDRO - 1):
        puntos -= 3

    # El disfraz de vampiro no lo usaba Lucía.
    if (ind[PERSONAJES.VAMPIRO * TAM_DISFRAZ] == AMIGOS.LUCIA - 1):
        puntos -= 3

    return puntos

def funcion_puntaje(ind):
    puntos = 0
    puntos += calcular_condiciones_a_cumplir(ind)
    puntos += calcular_restricciones(ind)

    return [puntos]