#!/usr/bin/env python3
import os

def generate(dir_path):
    '''
    str -> None
    generates pads and all other stuff required for a successfull generation of
    a batch of pads
    '''
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    os.chdir(dir_path)
    create_directory()
    return create_pads()


def create_directory():
    '''
    None -> None
    create the first directory from the range 0000-9999
    '''
    for i in ['{0:04}'.format(num) for num in range(0, 10000)]:
        if os.path.exists(i):
            continue
        else:
            print("making directory", i)
            os.mkdir(i)
            os.chdir(i)
            return i


def create_pads():
    '''
    None -> None
    generates and manages the creation of pads
    '''
    print("Generating Pads with /dev/random")
    for i in ['{0:02}'.format(num) for num in range(0, 100)]:
        write_random(48, '{}p'.format(i))
        write_random(48, '{}s'.format(i))
        write_random(2000, '{}c'.format(i))
    
        if i == 99:
            return "Generated {} pads".format(i+1)


def write_random(length, filename):
    '''
    str, str -> None
    write random numbers to pads
    '''
    rand = ''
    with open("/dev/random", 'rb') as file:
        rand = file.read(length)
        
    with open(filename, 'wb') as wr:
        wr.write(rand)

