# Variables globales
vowels = list('aeiouAEIOU')


# Funciones auxiliares
def next_vowels(vowel):
    index = vowels.index(vowel)
    if index == 4:
        return vowels[0]
    if index == 9:
        return vowels[5]
    return vowels[index + 1]


def count_and_replaces_vowels(string):
    count_vowels = 0
    new_string = ''
    for i, letter in enumerate(string):
        if letter in vowels:
            count_vowels += 1
            new_string += next_vowels(letter)
        else:
            new_string += letter
    return {"str": new_string, "count_vowels": count_vowels}


# Funcion para ejecución individual
def main():
    user_string = input('Ingrese la cadena a evaluar: ')
    results = count_and_replaces_vowels(user_string)
    print('Cadena resultante: ' + results['str'])
    print('Conteo de vocales: ' + str(results['count_vowels']))


if __name__ == '__main__':
    main()
