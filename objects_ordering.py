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


def ordering_data_by_priority(pre_data_list):
    pre_ordered_data = list()
    temporary_data = pre_data_list[:]
    while len(temporary_data) > 0:
        for priority in priorities:
            index_to_delet = 0
            while index_to_delet < len(temporary_data):
                if temporary_data[index_to_delet]['priority'] == priority:
                    pre_ordered_data.append(temporary_data.pop(index_to_delet))
                    index_to_delet = 0
                else:
                    index_to_delet += 1
    return pre_ordered_data


def ordering_data_by_level(data_list):
    ordered_data = list()
    temporary_data = data_list[:]
    while len(temporary_data) > 0:
        for level in levels:
            pre_ordered_data = list()
            index_to_delet = 0
            while index_to_delet < len(temporary_data):
                if temporary_data[index_to_delet]['level'] == level:
                    pre_ordered_data.append(temporary_data.pop(index_to_delet))
                    index_to_delet = 0
                else:
                    index_to_delet += 1
            data_by_priority = ordering_data_by_priority(pre_ordered_data)
            for item_by_priority in data_by_priority:
                ordered_data.append(item_by_priority)
    return ordered_data


def recursive_ordering_data(data_list):
    data_list = ordering_data_by_level(data_list)
    for item_list in data_list:
        if len(item_list['childs']) > 0:
            recursive_ordering_data(item_list['childs'])
    return data_list


def printing_ordering_data(data_list, level=0):
    for item_list in data_list:
        string = ''
        for i in range(level):
            string += '-----'
        print(string + '> ' + item_list['name'])
        if len(item_list['childs']) > 0:
            printing_ordering_data(item_list['childs'], level+1)


def show(data_list):
    print('\n------------Data------------\n')
    printing_ordering_data(data_list)
    print('\n------------Data------------\n')

# Funcion para ejecución individual
