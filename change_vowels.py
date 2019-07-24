# Variables globales
vowels = list('aeiouAEIOU')


# Funciones auxiliares
def next_vowels(vowel):
    """
    Funcion para recibir una vocal
    y retornar la siguiente vocal
    respetando ser caseSensitive

    :param vowel: string
    :return: string
    """
    index = 0

    # Ciclo para encontrar le indice de la vocal indicada
    for letter in vowels:
        if letter == vowel:
            break
        index += 1

    # retorno de la siguiente vocal
    if index == 4:
        return vowels[0]
    if index == 9:
        return vowels[5]
    return vowels[index + 1]


# Funcion para ejecución individual
