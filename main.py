#!/usr/bin/env python3
import urllib.request
import argparse
import sys, os
from generate import generate
import root_path
from send import prepare_to_send
from recev import decrypt


def read_from_file(filename):
    '''Read and return text from file

    str -> str
    
    filename - name of the text file to extract text from
    returns string data from file if passed string is valid filepath else
    returns the text passed as perameter'''
    f = open(filename)
    s = f.read()
    f.close()
    return s


class Parser():
    def __init__(self):
        '''NoneType -> NoneType
        Initialize argparse parser, parse and store the arguments to 
        args variable'''

        example_text = """example:

        python3 main.py -g dir/0000
        python3 main.py dir/0000
        python3 main.py -s 'random text' dir/0000
        python3 main.py -s -f filename dir/0000
        python3 main.py -s -t 'random text' dir/0000
        python3 main.py -r 'random text' dir/0000
        python3 main.py -r dir-0000-00t dir/0000
        """
        
        usage = """
        This program have three modes (generation, send and recieve) specified through the -g, -s and -r switches
        respectively. If the switch is not provided generation mode is assumed.
        """

        self.parser = argparse.ArgumentParser(
            prog = "CryptoPad",
            allow_abbrev = True,
            description = "self-contained tool in Python that can be used for securemessaging.",
            usage = usage,
            epilog = example_text,
            formatter_class = argparse.RawDescriptionHelpFormatter)
        self.parser.add_argument("-g", help = "this switch sets the program to generate mode", action = "store_true")
        self.parser.add_argument("-s", help = "this switch sets the program to send mode", action = "store_true")
        self.parser.add_argument("-r", help = "this switch sets the program to recieve mode", action = "store_true")
        
    def gen_mode(self):
        self.parse_arg()

    def recv_mode(self):
        self.parser.add_argument("in_stream", help = "file that contains encrypted text", type = str)
        self.parse_arg()

    def send_mode(self):
        self.parser.add_argument("-f", help = "this switch reads text from a file", type = str)
        self.parser.add_argument("-t", help = "this switch reads text from terminal", type = str)
        self.parser.add_argument("stdin", help = "text to insert", nargs = '?', default = 'Random text')
        self.parse_arg()

    def parse_arg(self):
        self.parser.add_argument("dir_path", help = "directory path to pads", type = str)
        self.args = self.parser.parse_args()


def run():
    root_path.path = os.getcwd()
    rtn_msg = ""
    parser = Parser()
    if sys.argv[1] == '-g':
        parser.gen_mode()
        print("STARTED GEN MODE: DirectoryPath[{}]".format(parser.args.dir_path))
        rtn_msg += generate(parser.args.dir_path)
        
    elif sys.argv[1] == '-s':
        parser.send_mode()
        if parser.args.f:
            print("STARTED SEND MODE: InputFile[{}] with PadDirectoryPath[{}]".format(parser.args.f, parser.args.dir_path))
            rtn_msg += prepare_to_send(parser.args.dir_path, read_from_file(parser.args.f))
        elif parser.args.t:
            print("STARTED SEND MODE: InputTxt[{}] with PadDirectoryPath[{}]".format(parser.args.t, parser.args.dir_path))
            rtn_msg += prepare_to_send(parser.args.dir_path, parser.args.t)
        elif parser.args.stdin:
            print("STARTED SEND MODE: InputTxt[{}] with PadDirectoryPath[{}]".format(parser.args.dir_path, parser.args.stdin))
            rtn_msg += prepare_to_send(parser.args.dir_path, parser.args.stdin)
    
    elif sys.argv[1] == '-r':
        parser.recv_mode()
        print("STARTED RECIEVE MODE: InputFile[{}] with PadDirectoryPath[{}]".format(parser.args.dir_path, parser.args.in_stream))
        rtn_msg += decrypt(parser.args.in_stream, parser.args.dir_path)

    else:
        parser.gen_mode()
        print("STARTED GEN MODE: PadDirectoryPath[{}]".format(parser.args.dir_path))
        rtn_msg += generate(parser.args.dir_path)

#try:
#    urllib.request.urlopen("https://www.google.com").read()
#    print("network interface is up: Quitting!")
#except:
run()