import unittest
import change_vowels
import change_vowels_upgrade
import objects_ordering
import objects_ordering_upgrade


class TestSectionA(unittest.TestCase):

    def test_A1(self):
        self.assertEqual(change_vowels.count_and_replaces_vowels('hacer'),
                         {"str": 'hecir', "count_vowels": 2})

    def test_A1_upgrade(self):
        self.assertEqual(change_vowels_upgrade.count_and_replaces_vowels('hacer'),
                         {"str": 'hecir', "count_vowels": 2})

    def test_A2(self):
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
        list_data = objects_ordering.firts_transform_data(data)
        objects_ordering.deleted_old_elements(list_data)
        list_data = objects_ordering.recursive_ordering_data(list_data)
        self.assertEqual(
            list_data,
            [
                {'name': 'One nameA',
                 'level': 'One',
                 'priority': 'Low',
                 'childs': [
                     {'name': 'One nameSubdataA',
                      'level': 'One',
                      'priority': 'Highest',
                      'childs': []
                      },
                     {'name': 'One nameSubDataA2',
                      'level': 'Two',
                      'priority': 'High',
                      'childs': [
                          {'name': 'One nameSubdataAA',
                           'level': 'One',
                           'priority': 'Highest',
                           'childs': []
                           }
                      ]
                      }
                 ]
                 },
                {'name': 'One nameB',
                 'level': 'Two',
                 'priority': 'Highest',
                 'childs': [
                     {'name': 'One nameSubDataB',
                      'level': 'One',
                      'priority': 'Highest',
                      'childs': []
                      }
                 ]
                 }
            ]
        )
        new_data = {
            "DataC": {
                "name": "One nameC",
                "level": "One",
                "priority": "High"
            }
        }
        objects_ordering.add_data(list_data, new_data)
        list_data = objects_ordering.recursive_ordering_data(list_data)
        self.assertEqual(
            list_data,
            [
                {"name": "One nameC",
                 "level": "One",
                 "priority": "High",
                 "childs": []
                 },
                {'name': 'One nameA',
                 'level': 'One',
                 'priority': 'Low',
                 'childs': [
                     {'name': 'One nameSubdataA',
                      'level': 'One',
                      'priority': 'Highest',
                      'childs': []
                      },
                     {'name': 'One nameSubDataA2',
                      'level': 'Two',
                      'priority': 'High',
                      'childs': [
                          {'name': 'One nameSubdataAA',
                           'level': 'One',
                           'priority': 'Highest',
                           'childs': []
                           }
                      ]
                      }
                 ]
                 },
                {'name': 'One nameB',
                 'level': 'Two',
                 'priority': 'Highest',
                 'childs': [
                     {'name': 'One nameSubDataB',
                      'level': 'One',
                      'priority': 'Highest',
                      'childs': []
                      }
                 ]
                 }
            ]
        )

    def test_A2_upgrade(self):
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
        testing = objects_ordering_upgrade.OrderingObjects(data)
        self.assertEqual(
            testing.get_ordered_object(),
            [
                {'name': 'One nameA',
                 'level': 'One',
                 'priority': 'Low',
                 'childs': [
                     {'name': 'One nameSubdataA',
                      'level': 'One',
                      'priority': 'Highest',
                      'childs': []
                      },
                     {'name': 'One nameSubDataA2',
                      'level': 'Two',
                      'priority': 'High',
                      'childs': [
                          {'name': 'One nameSubdataAA',
                           'level': 'One',
                           'priority': 'Highest',
                           'childs': []
                           }
                      ]
                      }
                 ]
                 },
                {'name': 'One nameB',
                 'level': 'Two',
                 'priority': 'Highest',
                 'childs': [
                     {'name': 'One nameSubDataB',
                      'level': 'One',
                      'priority': 'Highest',
                      'childs': []
                      }
                 ]
                 }
            ]
        )
        new_data = {
            "DataC": {
                "name": "One nameC",
                "level": "One",
                "priority": "High"
            }
        }
        testing.add_element(new_data)
        self.assertEqual(
            testing.get_ordered_object(),
            [
                {"name": "One nameC",
                 "level": "One",
                 "priority": "High",
                 "childs": []
                 },
                {'name': 'One nameA',
                 'level': 'One',
                 'priority': 'Low',
                 'childs': [
                     {'name': 'One nameSubdataA',
                      'level': 'One',
                      'priority': 'Highest',
                      'childs': []
                      },
                     {'name': 'One nameSubDataA2',
                      'level': 'Two',
                      'priority': 'High',
                      'childs': [
                          {'name': 'One nameSubdataAA',
                           'level': 'One',
                           'priority': 'Highest',
                           'childs': []
                           }
                      ]
                      }
                 ]
                 },
                {'name': 'One nameB',
                 'level': 'Two',
                 'priority': 'Highest',
                 'childs': [
                     {'name': 'One nameSubDataB',
                      'level': 'One',
                      'priority': 'Highest',
                      'childs': []
                      }
                 ]
                 }
            ]
        )


if __name__ == '__main__':
    unittest.main()
