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


def deleted_old_elements(data_list):
    accepted_keys = ['name', 'level', 'priority', 'childs']
    for item_list in data_list:
        aux_list = list()
        for item in item_list:
            if item not in accepted_keys:
                aux_list.append(item)
        for delet_object in aux_list:
            del(item_list[delet_object])
        if len(item_list['childs']) > 0:
            childs = deleted_old_elements(item_list['childs'])
            item_list['childs'] = childs
    return data_list


def add_data(old_list, new_object):
    transformed_data = firts_transform_data(new_object)
    deleted_old_elements(transformed_data)
    for new_element in transformed_data:
        old_list.append(new_element)


# Funcion para ejecución individual
