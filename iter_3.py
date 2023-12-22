class FlatIterator:
    def __init__(self, list_of_list: list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.counter = -1

        self.flatt = []
        for sublist in self.list_of_list:
            if not isinstance(sublist, list):
                self.flatt.append(sublist)
            else:
                for elem in sublist:
                    if isinstance(elem, list):
                        while True:
                            elem = [item for lst in elem for item in lst]
                            if all(not isinstance(item, list) for item in elem):
                                break
                        self.flatt.extend(elem)
                    else:
                        self.flatt.append(elem)
        self.flat_list_len = len(self.flatt)

        return self

    def __next__(self):
        self.counter += 1

        if self.counter >= self.flat_list_len:
            raise StopIteration
        item = self.flatt[self.counter]

        return item


# flatt = []
#
# for sublist in list_of_lists_2:
#     if not isinstance(sublist, list):
#         flatt.append(sublist)
#     else:
#         for elem in sublist:
#             if isinstance(elem, list):
#                 while True:
#                     elem = [item for lst in elem for item in lst]
#                     if all(not isinstance(item, list) for item in elem):
#                         break
#                 flatt.extend(elem)
#             else:
#                 flatt.append(elem)
#
# print(flatt)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()