
import uuid

def get_random_string(length = 6):
    return str(uuid.uuid4())[:length]

def get_random_list(length=6):
    return_list = []
    temp_uuid = str(uuid.uuid4())
    for i in range(1, length+1):
        return_list.append(temp_uuid[i])

    return return_list

def get_random_delim(length=1):
    return_string = ''
    temp_uuid = str(uuid.uuid4())
    for i in range(1, length+1):
        return_string = '{}{}'.format(return_string, temp_uuid[i])
    return return_string
