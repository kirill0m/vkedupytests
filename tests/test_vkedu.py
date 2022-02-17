import pytest


list_hello = ['H', 'e', 'l', 'l', 'o']
list_vkedu = ['V', 'K', 'e', 'd', 'u']
nums_boundaries = [2, 7]
fnames_set = {'Tom', "Mike", 'Ted', 'Etc'}
snames_set = {'Smith', 'Johnson', 'Williams'}
names_set = fnames_set.union(snames_set)


#list tests
@pytest.mark.parametrize('test_list, result', [
    (list_hello, 'Hello'),
    (list_vkedu, 'VKedu')
])
def test_list_to_string(test_list, result):
    assert ''.join(test_list) == result


def test_list_of_squares():
    assert [num**2 for num in range(nums_boundaries[0], nums_boundaries[-1])] == [4, 9, 16, 25, 36]


def test_list_of_nums():
    try:
        for i in list_hello:
            assert i / 2
    except TypeError:
        pass


#set tests
def test_set_uppercase():
    for i in fnames_set:
        assert i[0] == i[0].upper()


def test_set_unique_values():
    assert len(fnames_set.union(snames_set)) == len(fnames_set) + len(snames_set)


def test_set_issuset():
    assert fnames_set.issubset(names_set) == True