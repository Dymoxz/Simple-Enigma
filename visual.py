import os
import termcolor
import msvcrt
import time
IBackup = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
IIBackup = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'	
IIIBackup = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
IVBackup = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
VBackup = 'VZBRGITYUPSDNHLXAWMJQOFECK'




I = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
II = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'	
III = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
IV = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
V = 'VZBRGITYUPSDNHLXAWMJQOFECK'
reflectorA = 'EJMZALYXVBWFCRQUONTSPIKHGD'
reflectorB = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
reflectorC = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

alphabet1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

plugDict = {'A': 'R', 'R': 'A', 'G': 'K', 'K': 'G', 'X': 'O', 'O': 'X'}

#split alphabet into list with letters
alphabetList = list(alphabet)

#if letter is in plugDict replace alphabetList letter with plugDict letter
def plugboard(inputy):
    output = ''
    for letter in inputy:
        if letter in plugDict.values():
            for key, value in plugDict.items():
                if value == letter:
                    output += key
        else:
            output += letter
    return output
plugAlpha = plugboard(alphabet)
def highlight(string, replace, color):
    return string.replace(replace, termcolor.colored(replace, 'white', color))

string = ''
encrypted = ''

#grab first letter of string and put it at the end
def shift(string):
    return string[1:] + string[0]
    



while True:
    inputa = str(msvcrt.getch())
    inputa = inputa.split("'")[1]
    print(inputa)
    string += inputa
    os.system('cls')

    def shift(string):
        return string[1:] + string[0]
    I = shift(I)
    alphabet1 = shift(alphabet1)
    if I[0] == IBackup[-1]:
        II = shift(II)
        alphabet2 = shift(alphabet2)
    if II[0] == IIBackup[-1]:
        III = shift(III)
        alphabet3 = shift(alphabet3)

    alphabetHigh = highlight(alphabet, inputa, 'on_red')
    newAlphaHigh = highlight(plugAlpha, inputa, 'on_red')


    def rotor(input, alpha, rotorNum):
        for letter in input:
            letterIndex = alpha.index(letter)
            rotorOut = rotorNum[letterIndex]
        return rotorOut

    rotor3output = rotor(inputa, plugAlpha, III)
    rotor2output = rotor(rotor3output, alphabet2, II)
    rotor1output = rotor(rotor2output, alphabet1, I)


    rotor3_P1 = highlight(III, rotor3output, 'on_red')
    rotor3_P2 = highlight(alphabet3, rotor3output, 'on_red')
    rotor2_P1 = highlight(II, rotor2output, 'on_red')
    rotor2_P2 = highlight(alphabet2, rotor2output, 'on_red')
    rotor1_P1 = highlight(I, rotor1output, 'on_red')
    rotor1_P2 = highlight(alphabet1, rotor1output, 'on_red')


    def reflector(input, reflectorus):
        for letter in input:
            reflectIndex = alphabet.index(letter)
            reflectLetter = reflectorus[reflectIndex]
            alphaIndex = alphabet.index(reflectLetter)
            alphaLetter = alphabet[alphaIndex]   
            reflectLetter2 = reflectorus[alphaIndex]
            return reflectLetter, alphaLetter, reflectLetter2
    reflectLetter, alphaLetter, reflectLetter2 = reflector(rotor1output, reflectorA)


    firstHigh = reflectorA.replace(reflectLetter, termcolor.colored(reflectLetter, 'white', 'on_red'))
    secondHigh = firstHigh.replace(reflectLetter2, termcolor.colored(reflectLetter2, 'white', 'on_green'))


    rotor1outputBack = alphabet2[I.index(alphaLetter)]
    rotor2outputBack = alphabet3[II.index(rotor1outputBack)]
    rotor3outputBack = alphabet[III.index(rotor2outputBack)]
    rotor3outputBack2 = plugAlpha[III.index(rotor2outputBack)]
    encrypted += rotor3outputBack2

    alphabet_P1 = alphabetHigh
    alphabet_P2 = highlight(alphabet_P1, rotor3outputBack2, 'on_green')
    newAlpha_P1 = newAlphaHigh
    newAlpha_P2 = highlight(newAlpha_P1, rotor3outputBack2, 'on_green')

    print()
    print('Enigga 3000')
    print()
    h1 = highlight('Red is input (forward), Blue/Green is output (Back)', 'Blue/Green', 'on_green')
    print(highlight(h1, 'Red', 'on_red'))
    print()
    print('         Plugboard')
    print(alphabet_P2)
    print(newAlpha_P2)
    print()
    print('          Rotor 1')

    #rotor 1
    print(highlight(rotor3_P1, rotor2outputBack, 'on_green'))
    print(highlight(rotor3_P2, rotor2outputBack, 'on_green'))
    print()
    print('          Rotor 2')
    #rotor 2
    print(highlight(rotor2_P1, rotor1outputBack, 'on_green'))
    print(highlight(rotor2_P2, rotor1outputBack, 'on_green'))
    print()
    print('          Rotor 3')
    #rotor 3
    print(highlight(rotor1_P1, alphaLetter, 'on_green'))
    print(highlight(rotor1_P2, alphaLetter, 'on_green'))
    print()
    print('         Reflector')
    #reflector
    print(secondHigh)
    print(highlight(alphabet, alphaLetter, 'on_red'))
    print(f'Input: {string}')
    print(f'Output: {encrypted}')
