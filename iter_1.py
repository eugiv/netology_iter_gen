class FlatIterator:
    def __init__(self, list_of_lists: list):
        self.list_of_lists = list_of_lists

    def __iter__(self):
        self.counter = -1
        self.iter_elem = [elem for lst in self.list_of_lists for elem in lst]
        self.iter_elem_cnt = len(self.iter_elem)

        return self

    def __next__(self):
        self.counter += 1
        if self.counter >= self.iter_elem_cnt:
            raise StopIteration

        item = self.iter_elem[self.counter]

        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
