#!/usr/bin/env python3
import os
import sys
import root_path
from utils import find_valid_pad, create_filename


def prepare_to_send(dir_path, text):
    '''str, str -> str
    this method manages all the functionalioty of buffer preparation 
    for transmission
    '''
    global DIR_PATH
    DIR_PATH = dir_path
    os.chdir(DIR_PATH)
    return encrypt_with_pad(find_valid_pad(), text)
    

def encrypt_with_pad(pad_id, text):
    '''
    str, str -> str
    this function returns the message based on wheteher the encryption
    was successfull or not 
    '''
    global PAD_ID 
    PAD_ID = pad_id
    pad_p = list(open(f"{pad_id}p", "rb").read())
    pad_c = list(open(f"{pad_id}c", "rb").read())
    pad_s = list(open(f"{pad_id}s", "rb").read())
    ascii_text = convert_to_ascii(text)
    if len(ascii_text) < 2001:
        return write_to_file(encrypt(ascii_text, pad_p, pad_c, pad_s))
    else:
        return "ERR: text size is bigger than buffer size"


def write_to_file(ints):
    '''
    list -> str
    writes a list of integers to a file based on directory path and pad
    '''
    filename = create_filename(DIR_PATH, PAD_ID)
    
    os.chdir(root_path.path)
    string_ints = [str(int) for int in ints]
    s = ",".join(string_ints)

    with open(f"{filename}t", "w") as f:
        f.write(s)
        os.remove(os.path.join(DIR_PATH, f"{PAD_ID}c"))
        return "file wrote successfully"

    return "ERR occured while writing"


def encrypt(ascii_text, pad_p, pad_c, pad_s):
    '''
    byte, byte, byte, byte -> list(int)
    returns a list of integers encrypted using pad
    '''
    new_list = pad_p
    length = len(ascii_text)

    for i in range(length):
        new_list.append(ascii_text[i] + pad_c[i])

    for i in pad_s:
        new_list.append(i)
    
    return new_list


def convert_to_ascii(arr):
    '''
    byte -> int
    takes a byte array and return ascii equivalent of it
    '''
    lst = []
    for i in arr:
        lst.append(ord(i))
    return lst

#prepare_to_send('dir/0000', "hello")