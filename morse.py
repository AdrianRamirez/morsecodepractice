import time
from pygame import mixer
import string
string.ascii_letters
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import random

mixer.init()
punto = mixer.Sound('dit.wav')
linea = mixer.Sound('dah.wav')

s = "-- --- .-. ... .   -.-. --- -.. ."
delay = 1
charspace = 0.25
wordspace = 0.7
wordspace -= charspace

code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
        '?': '..--..', '=': '-...-'}


def translate(inp):
    s = ""
    for i in inp:
        if i == ' ':
            s = s + '|'
        else:
            s = s + code[i] + ' '

    return s

while(1):
    inp = "Nueva letra sonando:"
    print(inp)
    inp = random.choice(string.ascii_letters)
    s = ""
    s = translate(inp.capitalize())
    let = inp
    #inp = input("Enter any key to continue: ")

    def playpunto():
        punto.play()
        time.sleep(delay * 0.18)


    def playlinea():
        linea.play()
        time.sleep(delay * 0.35)

    tic = time.time()
    for i in s:
        if i == '.':
            playpunto()
        elif i == '_' or i == '-':
            playlinea()
        elif i == ' ':
            time.sleep(charspace)
        elif i == '|':
            time.sleep(wordspace)
    #print(time.time() - tic)
    inp = input("Morse: ")
    print(s)
    inp = input("letra: ")
    if inp.capitalize() == let.capitalize():
        print("correcto")
    if inp.capitalize() != let.capitalize():
        print("incorrecto")
    print("la letra que ha sonado es la:", let)
    inp = input("Siguiente letra: ")
    
