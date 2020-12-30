import os
from utils import find_valid_pad, create_filename
import root_path

def decrypt(dir_path, filename):
    '''str, str -> str
    this method manages all the functionalioty of buffer preparation 
    for decryption
    '''
    global DIR_PATH
    DIR_PATH = dir_path

    contents = remove_paddings(filename)
    os.chdir(dir_path)
    return write_to_file(decrypt_with_pad(find_valid_pad(), contents))


def write_to_file(chrs):
    '''
    list -> str
    writes a string to a file based on directory path and pad
    '''
    filename = create_filename(DIR_PATH, PAD_ID)
    os.chdir(root_path.path)
    s = "".join(chrs)

    with open(f"{filename}m", "w+") as f:
        f.write(s)
        os.remove(os.path.join(DIR_PATH, f"{PAD_ID}c"))
        return "file wrote successfully"

    return "ERR occured while writing"
    

def decrypt_with_pad(pad_id, contents):
    '''
    str, str -> str
    this function returns the message based on wheteher the encryption
    was successfull or not 
    '''
    global PAD_ID
    PAD_ID = pad_id

    pad_c = list(open(f"{pad_id}c", "rb").read())
    
    new_list = []
    length = len(contents)

    for i in range(length):
        new_list.append(chr(int(contents[i]) - pad_c[i]))

    return new_list


def remove_paddings(filename):
    '''
    str -> list
    return list of valid items in an encrypted file removing the paddings
    '''
    with open(filename, "r") as f:
        contents = f.read().split(",")
        contents = contents[48:]
        contents = contents[:-48]
        return contents
    