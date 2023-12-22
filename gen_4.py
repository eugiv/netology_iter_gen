import types


def flat_generator(list_of_list: list):
    flatt = []

    for sublist in list_of_list:
        if not isinstance(sublist, list):
            flatt.append(sublist)
        else:
            for elem in sublist:
                if isinstance(elem, list):
                    while True:
                        elem = [item for lst in elem for item in lst]
                        if all(not isinstance(item, list) for item in elem):
                            break
                    flatt.extend(elem)
                else:
                    flatt.append(elem)

    flat_list_len = len(flatt)
    for item_cnt in range(flat_list_len):
        item = flatt[item_cnt]

        yield item


def test_4():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    test_4()
