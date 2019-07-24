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


def count_and_replaces_vowels(string):
    count_vowels = 0
    index = 0
    list_string = list(string)
    for letter in list_string:
        if letter in vowels:
            count_vowels += 1
            list_string[index] = next_vowels(letter)
        index += 1
    string = ''.join(list_string)
    return {"str": string, "count_vowels": count_vowels}


# Funcion para ejecución individual
