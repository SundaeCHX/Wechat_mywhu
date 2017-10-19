# -*- coding: utf-8 -*-

CODE = {'A': '.-', 'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.',  ' ': ' '}
CODE1 = {'A': '.-', 'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'}
UNCODE = dict(map(lambda t:(t[1],t[0]),CODE.items()))
UNCODE1 = dict(map(lambda t:(t[1],t[0]),CODE1.items()))


def morse(msg):
    word=''
    morse=msg
    for char in morse:
        word=word+CODE[char.upper()] + ' '
    return word.encode('utf-8')

def umorse(msg):
    word=''
    msg=msg.split(' ')
    for char in msg:
        if char=='':
            word=word+' '
        else:
            word=word+UNCODE[char]
    return word.encode('utf-8')

def morse1(msg):
    word=''
    morse=msg
    for char in morse:
        if char==' ':
            word=word
        else:
            word=word+CODE1[char.upper()]+'/'
    return word.encode('utf-8')

def umorse1(msg):
    word=''
    msg=msg.split('/')
    for char in msg:
        if char=='':
            word=word+' '
        else:
            word=word+UNCODE1[char]
    return word.encode('utf-8')
