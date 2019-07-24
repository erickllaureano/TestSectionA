# Variables globales
levels = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
priorities = ['Highest', 'High', 'Medium', 'Low', 'Lowest']


# Clase controladora
class OrderingObjects:
    # Constructor
    def __init__(self, initial_data):
        self.original_object = initial_data
        self.list_data = self.firts_transform_data(self.original_object)
        self.deleted_old_elements(self.list_data)
        self.list_data = self.recursive_ordering_data(self.list_data)

    # Methods:
    def firts_transform_data(self, data):
        aux_list = list()
        for item in data:
            if type(data[item]) is dict:
                aux = self.firts_transform_data(data[item])
                data[item]['childs'] = aux
                aux_list.append(data[item])
        return aux_list

    def deleted_old_elements(self, data_list):
        accepted_keys = ['name', 'level', 'priority', 'childs']
        for item_list in data_list:
            aux_list = list()
            for item in item_list:
                if item not in accepted_keys:
                    aux_list.append(item)
            for delete_object in aux_list:
                del (item_list[delete_object])
            if len(item_list['childs']) > 0:
                childs = self.deleted_old_elements(item_list['childs'])
                item_list['childs'] = childs
        return data_list

    @staticmethod
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

    def ordering_data_by_level(self, data_list):
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
                data_by_priority = self.ordering_data_by_priority(pre_ordered_data)
                for item_by_priority in data_by_priority:
                    ordered_data.append(item_by_priority)
        return ordered_data

    def recursive_ordering_data(self, data_list):
        data_list = self.ordering_data_by_level(data_list)
        for item_list in data_list:
            if len(item_list['childs']) > 0:
                self.recursive_ordering_data(item_list['childs'])
        return data_list

    def printing_ordering_data(self, data_list, level=0):
        for item_list in data_list:
            string = ''
            for i in range(level):
                string += '-----'
            print(string + '> ' + item_list['name'])
            if len(item_list['childs']) > 0:
                self.printing_ordering_data(item_list['childs'], level + 1)

    def show(self):
        print('\n------------Data------------\n')
        self.printing_ordering_data(self.list_data)
        print('\n------------Data------------\n')

    def add_element(self, new_object):
        transformed_data = self.firts_transform_data(new_object)
        self.deleted_old_elements(transformed_data)
        for new_element in transformed_data:
            self.list_data.append(new_element)
        self.list_data = self.recursive_ordering_data(self.list_data)


if __name__ == '__main__':
    data = {
      "DataA": {
        "name": "One nameA",
        "level": "One",
        "priority": "Low",
        "SubDataA": {
          "name": "One nameSubdataA",
          "level": "One",
          "priority": "Highest"
        },
        "SubDataA2": {
          "name": "One nameSubDataA2",
          "level": "Two",
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
    testing = OrderingObjects(data)
    testing.show()
    new_data = {
        "DataC": {
            "name": "One nameC",
            "level": "One",
            "priority": "High"
        }
    }
    testing.add_element(new_data)
    testing.show()
