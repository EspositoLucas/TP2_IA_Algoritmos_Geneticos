import random
from enum import IntEnum

PERSONAJES = IntEnum("PERSONAJE", ["PIRATA", "VAMPIRO", "HOMBRE_LOBO", "BRUJA"])
AMIGOS = IntEnum("AMIGO", ["LUCIA", "MARIO", "PEDRO", "JUAN"])
COLORES = IntEnum("COLOR", ["ROJO", "NEGRO", "VERDE", "AZUL"])
POS_PERSONAJE = 0
POS_AMIGO = 1
POS_COLOR = 2

TAM_DISFRAZ = 3
CANT_DISFRACES = 4

def imprimir_ind(ind):
    print(ind)
    for i in range(CANT_DISFRACES):
        print("Personaje:", PERSONAJES(ind[i * TAM_DISFRAZ + POS_PERSONAJE] + 1).name)
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

    
    for i in range(CANT_DISFRACES):
        # El disfraz de bruja era de color verde.
        if ind[i * TAM_DISFRAZ + POS_PERSONAJE] + 1  == PERSONAJES.BRUJA and ind[i * TAM_DISFRAZ + POS_COLOR] + 1 == COLORES.VERDE:
            puntos += 5

        # El disfraz de vampiro era de color negro.
        if ind[i * TAM_DISFRAZ + POS_PERSONAJE] + 1  == PERSONAJES.VAMPIRO and ind[i * TAM_DISFRAZ + POS_COLOR] + 1 == COLORES.NEGRO:
            puntos += 5
    
    return puntos



def calcular_restricciones(ind):
    puntos = 0

    # No repetir valores en los genes
    repite = False
    for i in range(CANT_DISFRACES):
        for j in range(CANT_DISFRACES):
            if i!=j:
                if (ind[i * TAM_DISFRAZ + POS_PERSONAJE] == ind[j * TAM_DISFRAZ + POS_PERSONAJE] or ind[i * TAM_DISFRAZ + POS_AMIGO] == ind[j * TAM_DISFRAZ + POS_AMIGO] or ind[i * TAM_DISFRAZ + POS_COLOR] == ind[j * TAM_DISFRAZ + POS_COLOR]):
                    repite = True
    if(repite):
        puntos -= 300

    for i in range(CANT_DISFRACES):
        # El disfraz de pirata no era de color rojo 
        if ind[i * TAM_DISFRAZ + POS_PERSONAJE] + 1  == PERSONAJES.PIRATA and ind[i * TAM_DISFRAZ + POS_COLOR] + 1 == COLORES.ROJO:
            puntos -= 3

        # El disfraz de pirata no lo usaba Lucía.
        if ind[i * TAM_DISFRAZ + POS_PERSONAJE] + 1  == PERSONAJES.PIRATA and ind[i * TAM_DISFRAZ + POS_AMIGO] + 1 == AMIGOS.LUCIA:
            puntos -= 3

        # Mario no se disfrazó de hombre lobo.
        if ind[i * TAM_DISFRAZ + POS_PERSONAJE] + 1  == PERSONAJES.HOMBRE_LOBO and ind[i * TAM_DISFRAZ + POS_AMIGO] + 1 == AMIGOS.MARIO:
            puntos -= 3

        # Mario no usó un disfraz negro.
        if (ind[i * TAM_DISFRAZ + POS_AMIGO] + 1 == AMIGOS.MARIO and ind[i * TAM_DISFRAZ + POS_COLOR] + 1 == COLORES.NEGRO):
            puntos -= 3

        # El disfraz de bruja no lo usaba Pedro.
        if (ind[i * TAM_DISFRAZ + POS_PERSONAJE] + 1 == PERSONAJES.BRUJA and ind[i * TAM_DISFRAZ + POS_AMIGO] + 1 == AMIGOS.PEDRO):
            puntos -= 3

        # El disfraz de vampiro no lo usaba Lucía.
        if (ind[i * TAM_DISFRAZ + POS_PERSONAJE] + 1 == PERSONAJES.VAMPIRO and ind[i * TAM_DISFRAZ + POS_AMIGO] + 1 == AMIGOS.LUCIA):
            puntos -= 3

    return puntos

def funcion_puntaje(ind):
    puntos = 0
    puntos += calcular_condiciones_a_cumplir(ind)
    puntos += calcular_restricciones(ind)

    return [puntos]