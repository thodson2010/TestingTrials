
def list_to_string(given_list, delim):
    """Takes a given list and turns it into a string with the given deliminator.
    returns: return_value str"""
    return_value = ''
    for element in given_list:
        # If it's the first item in the list, just add it.
        if return_value == '':
            return_value = '{}{}'.format(return_value, element)
        else:
            # if it's not the first item in the list, then append it.
            return_value = '{}{}{}'.format(return_value, delim, element)

    return return_value

