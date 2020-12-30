import os

def find_valid_pad():
    '''
    gets the valid pad file id based on the current working directory
    '''
    for i in ['{0:02}'.format(num) for num in range(0, 100)]:
        if os.path.exists(f'{i}c'):
            return i
        else:
            continue

def create_filename(dir_path, pad_id):
    '''
    str, str -> str
    return a filename from working directory and pad id
    '''
    name = dir_path.split('/')
    name.append(pad_id)
    return "-".join(name)
