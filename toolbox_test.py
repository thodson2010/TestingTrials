

from helper_functions import get_random_list, get_random_string, get_random_delim
from toolbox import list_to_string

def test_list_to_string_empty():
    assert list_to_string([],'') == ''

def test_list_to_string_single_element_comma_delim():
    assert list_to_string(['a'], ',') == 'a'

def test_list_to_string_multiple_element_comma_delim():
    assert list_to_string(['a', 'b', 'c'], ',') == 'a,b,c'

def test_list_to_string_multiple_element_random_no_delim():
    testing_list = get_random_list()
    testing_string = ''
    for element in testing_list:
        testing_string = '{}{}'.format(testing_string, element)
    assert list_to_string(testing_list, '') == testing_string

def test_list_to_string_multiple_element_random_comma_delim():
    testing_list = get_random_list()
    testing_string = ''
    for element in testing_list:
        if testing_string == '':
            testing_string = '{}{}'.format(testing_string, element)
        else:
            testing_string = '{}{}{}'.format(testing_string, ',', element)
    assert list_to_string(testing_list, ',') == testing_string

def test_list_to_string_incorrect_result():
    testing_list = get_random_list()
    testing_string = get_random_string()
    assert list_to_string(testing_list, ',') != testing_string

def test_list_to_string_multiple_delim():
    testing_list = get_random_list()
    testing_string = ''
    testing_delim = get_random_delim()
    for element in testing_list:
        if testing_string == '':
            testing_string = '{}{}'.format(testing_string, element)
        else:
            testing_string = '{}{}{}'.format(testing_string, testing_delim, element)
    assert list_to_string(testing_list, testing_delim) == testing_string
    print()
    print(testing_string)
