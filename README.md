# One-Time-Pad-Cipher
 A self-contained tool in Python that can be used for securemessaging. The tool is be able to apply a One-Time Pad cipher to a given message.
 
 This program have three modes (generation, send and recieve) specified through the -g, -s and -r switches respectively. If the switch is not provided generation mode is assumed.
 
 
 *Example Usage*
 ```
        python3 main.py -g dir/0000
        python3 main.py dir/0000
        python3 main.py -s 'random text' dir/0000
        python3 main.py -s -f filename dir/0000
        python3 main.py -s -t 'random text' dir/0000
        python3 main.py -r 'random text' dir/0000
        python3 main.py -r dir-0000-00t dir/0000
        
```
