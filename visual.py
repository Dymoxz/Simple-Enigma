import os
import termcolor

os.system('cls')
I = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
II = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'	
III = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
IV = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
V = 'VZBRGITYUPSDNHLXAWMJQOFECK'
reflectorA = 'EJMZALYXVBWFCRQUONTSPIKHGD'
reflectorB = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
reflectorC = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

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

inputa = 'A'

def highlight(string, replace, color):
    return string.replace(replace, termcolor.colored(replace, 'white', color))


nigga = alphabet.split(inputa)
for i in nigga:
    if i == '':
        nigga[nigga.index(i)] = inputa

alphabetHigh = highlight(alphabet, inputa, 'on_red')
newAlphaHigh = highlight(plugAlpha, inputa, 'on_red')


def rotor(input, alpha, rotorNum):
    for letter in input:
        letterIndex = alpha.index(letter)
        rotorOut = rotorNum[letterIndex]
    return rotorOut

rotor3output = rotor(inputa, plugAlpha, III)
rotor2output = rotor(rotor3output, alphabet, II)
rotor1output = rotor(rotor2output, alphabet, I)


rotor3_P1 = highlight(III, rotor3output, 'on_red')
rotor3_P2 = highlight(alphabet, rotor3output, 'on_red')
rotor2_P1 = highlight(II, rotor2output, 'on_red')
rotor2_P2 = highlight(alphabet, rotor2output, 'on_red')
rotor1_P1 = highlight(I, rotor1output, 'on_red')
rotor1_P2 = highlight(alphabet, rotor1output, 'on_red')


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


rotor1outputBack = alphabet[I.index(alphaLetter)]
rotor2outputBack = alphabet[II.index(rotor1outputBack)]
rotor3outputBack = alphabet[III.index(rotor2outputBack)]
rotor3outputBack2 = plugAlpha[III.index(rotor2outputBack)]
alphabet_P1 = alphabetHigh
alphabet_P2 = highlight(alphabet_P1, rotor3outputBack2, 'on_green')
newAlpha_P1 = newAlphaHigh
newAlpha_P2 = highlight(newAlpha_P1, rotor3outputBack2, 'on_green')

print()
print('Enigga 3000')
print()
print('         Plugboard')
print(alphabet_P2)
print(newAlpha_P2)
print()
print('          Rotor 1')

#rotor 3
print(highlight(rotor3_P1, rotor2outputBack, 'on_green'))
print(highlight(rotor3_P2, rotor2outputBack, 'on_green'))
print()
print('          Rotor 2')
#rotor 2
print(highlight(rotor2_P1, rotor1outputBack, 'on_green'))
print(highlight(rotor2_P2, rotor1outputBack, 'on_green'))
print()
print('          Rotor 3')
#rotor 1
print(highlight(rotor1_P1, alphaLetter, 'on_green'))
print(highlight(rotor1_P2, alphaLetter, 'on_green'))
print()
print('         Reflector')
#reflector
print(secondHigh)
print(highlight(alphabet, alphaLetter, 'on_red'))
