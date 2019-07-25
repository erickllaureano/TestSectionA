# Variables globales
levels = ['One', 'Two', 'Three', 'Four', 'Five',
          'Six', 'Seven', 'Eight', 'Nine', 'Ten']
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


def searching_move_data(temporary_data, pre_ordered_data, key, value):
    index_to_delet = 0
    while index_to_delet < len(temporary_data):
        key_value = temporary_data[index_to_delet].get(
            key, ''
        )
        if key_value == value:
            pre_ordered_data.append(
                temporary_data.pop(index_to_delet)
            )
            index_to_delet = 0
        else:
            index_to_delet += 1


def ordering_data_by_priority(pre_data_list):
    pre_ordered_data = list()
    temporary_data = pre_data_list[:]
    for priority in priorities:
        searching_move_data(
            temporary_data,
            pre_ordered_data,
            'priority',
            priority
        )
    pre_ordered_data += temporary_data
    return pre_ordered_data


def ordering_data_by_level(data_list):
    ordered_data = list()
    temporary_data = data_list[:]
    for level in levels:
        pre_ordered_data = list()
        searching_move_data(
            temporary_data,
            pre_ordered_data,
            'level',
            level
        )
        ordered_data += ordering_data_by_priority(
            pre_ordered_data
        )
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


def init_app(data):
    list_data = firts_transform_data(data)
    deleted_old_elements(list_data)
    list_data = recursive_ordering_data(list_data)
    show(list_data)

    first_data = {
        "DataC": {
            "name": "One nameC",
            "level": "One",
            "priority": "High"
        }
    }

    add_data(list_data, first_data)
    list_data = recursive_ordering_data(list_data)
    show(list_data)


# Funcion para ejecución individual
def main():
    obj = {
      "DataA": {
        "name": "One nameA",
        "level": "One",
        "priority": "Low",
        "SubDataA": {
          "name": "One nameSubdataA",
          "level": "Two",
          "priority": "Highest"
        },
        "SubDataA2": {
          "name": "One nameSubDataA2",
          "level": "One",
          "priority": "High",
          "SubDataAA": {
            "name": "One nameSubdataAA",
            "level": "One",
            "priority": "Highest"
          }
        }
      },
      "DataB": {
        "name": "One nameB",
        "level": "Two",
        "priority": "Highest",
        "subDataB": {
          "name": "One nameSubDataB",
          "level": "One",
          "priority": "Highest"
        }
      }
    }
    init_app(obj)


if __name__ == '__main__':
    main()
