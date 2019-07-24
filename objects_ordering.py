# Variables globales
levels = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
priorities = ['Highest', 'High', 'Medium', 'Low', 'Lowest']


# Funciones auxiliares
def firts_transform_data(data):
    aux_list = list()
    for item in data:
        if type(data[item]) is dict:
            aux = firts_transform_data(data[item])
            data[item]['childs'] = aux
            aux_list.append(data[item])
    return aux_list



# Funcion para ejecución individual
