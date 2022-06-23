import os
import termcolor
import msvcrt
import time

#Backup Rotors
IBackup = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
IIBackup = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'	
IIIBackup = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
IVBackup = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
VBackup = 'VZBRGITYUPSDNHLXAWMJQOFECK'

#All available rotors
III = 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
II = 'AJDKSIRUXBLHWTMCQGZNPYFVOE'	
I = 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
IV = 'ESOVPZJAYQUIRHXLNFTGKDCMWB'
V = 'VZBRGITYUPSDNHLXAWMJQOFECK'\
#All available reflectors
reflectorA = 'EJMZALYXVBWFCRQUONTSPIKHGD'
reflectorB = 'YRUHQSLDPXNGOKMIEBFZCWVJAT'
reflectorC = 'FVPJIAOYEDRZXWGCTKUQSBNMHL'

#Seperate alphabets per rotor
alpha_R1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_R2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha_R3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

plugDict = {
    'A': 'R', 
    'R': 'A', 
    'G': 'K', 
    'K': 'G', 
    'X': 'O',
    'O': 'X'
}

#---------------------------------------------#


def CreatePlugboard(inputy):
    output = ''
    for letter in inputy:
        if letter in plugDict.values():
            for key, value in plugDict.items():
                if value == letter:
                    output += key
        else:
            output += letter
    return output

def Highlight(string, replace, color):
    return string.replace(replace, termcolor.colored(replace, 'white', color))

def Rotor(input, alpha, rotorNum, prevIndex):
    rotorOut = rotorNum[prevIndex]
    rotorIndex = alpha.index(rotorOut)
    return rotorOut, rotorIndex

def Reflector(input, reflectorus, prevIndex):
    reflectIn = reflectorus[prevIndex]
    alphaIndex = alphabet.index(reflectIn)
    alphaLetter = alphabet[alphaIndex]   
    relfectOut = reflectorus[alphaIndex]
    return reflectIn, alphaLetter, relfectOut, alphaIndex

def Plugboard(input):
    return input, plugboard.index(input)

def PlugboardBack(prevIndex):
    return plugboard[prevIndex], prevIndex

def RotorBack(input, alpha, rotorNum, prevIndex):
    rotorOut = alpha[prevIndex]
    rotorIndex = rotorNum.index(rotorOut)
    return rotorOut, rotorIndex

def Rotate(string):
    return string[1:] + string[0]

def StartPositionRotor(rotor, startLetter):
    return rotor[rotor.index(startLetter):] + rotor[:rotor.index(startLetter)]


#---------------------------------------------#

plugboard = CreatePlugboard(alphabet)
string = ''
encrypted = ''

rotorChoices = []
rotorChoice = input('Which rotor would you like to use? (1, 2, 3, 4, 5) Choose 3, seperated by commas: \n')
rotorChoice = rotorChoice.split(',')
for rotoros in rotorChoice:
    if rotoros == '1':
        rotorChoices.append(I)
    elif rotoros == '2':
        rotorChoices.append(II)
    elif rotoros == '3':
        rotorChoices.append(III)
    elif rotoros == '4':
        rotorChoices.append(IV)
    elif rotoros == '5':
        rotorChoices.append(V)

rotorPosition = input('Which position would you like to start the rotors at? (KGU) String of 3 letters:\n')
# rotorPosition = rotorPosition.upper()
for rotor in rotorChoices:
    rotorChoices[rotorChoices.index(rotor)] = StartPositionRotor(rotor, rotorPosition[rotorChoices.index(rotor)])
    
print('Type to encrypt message: \n')

#add rotorChoice to list of rotors

while True:
    input = str(msvcrt.getch())
    input = input.split("'")[1]
    input = input.upper()
    print(input)
    string += input
    os.system('cls')

    rotorChoices[0] = Rotate(rotorChoices[0])
    alpha_R1 = Rotate(alpha_R1)
    if rotorChoices[0][0] == IBackup[-1]:
        rotorChoices[1] = Rotate(rotorChoices[1])
        alpha_R2 = Rotate(alpha_R2)
    if rotorChoices[1][0] == IIBackup[-1]:
            rotorChoices[2] = Rotate(rotorChoices[2])
            alpha_R3 = Rotate(alpha_R3)
    #----------------Heen weg---------------------#

    plugInput, plugIndex = Plugboard(input)
    # print(plugInput, plugIndex)

    rotor1LetterOut, rotor1Index = Rotor(input, alpha_R1, rotorChoices[0], plugIndex)
    # print(rotor1LetterOut, rotor1Index)

    rotor2LetterOut, rotor2Index = Rotor(rotor1LetterOut, alpha_R2, rotorChoices[1], rotor1Index)
    # print(rotor2LetterOut, rotor2Index)

    rotor3LetterOut, rotor3Index = Rotor(rotor2LetterOut, alpha_R3, rotorChoices[2], rotor2Index)
    # print(rotor3LetterOut, rotor3Index)

    reflectIn, alphaLetter, reflectOut, reflectIndex = Reflector(rotor3LetterOut, reflectorA, rotor3Index)
    # print(reflectIn, alphaLetter, reflectOut, reflectIndex)

    #----------------Terug weg-------------------#

    retor3BackLetter, rotor3Index = RotorBack(reflectOut, alpha_R3, rotorChoices[2], reflectIndex)
    # print(retor3BackLetter, rotor3Index)

    retor2BackLetter, rotor2Index = RotorBack(retor3BackLetter, alpha_R2, rotorChoices[1], rotor3Index)
    # print(retor2BackLetter, rotor2Index)

    retor1BackLetter, rotor1Index = RotorBack(retor2BackLetter, alpha_R1, rotorChoices[0], rotor2Index)
    # print(retor1BackLetter, rotor1Index)

    plugBackOutput, plugIndex = PlugboardBack(rotor1Index)
    # print(plugBackOutput, plugIndex)

    #---------------------------------------------#

    print('\nEnigga\n')
    h1 = Highlight('Blue/Green is input (forward), Red is output (Back), Yellow is the reflector', 'Blue/Green', 'on_green')
    h1 = Highlight(h1, 'Red', 'on_red')
    print(Highlight(h1, 'Yellow', 'on_yellow'))


    alphaHeen = Highlight(alphabet, plugInput, 'on_green')
    alphaTerug = Highlight(alphaHeen, plugBackOutput, 'on_red')
    print(alphaTerug)

    plugHeen = Highlight(plugboard, plugInput, 'on_green')
    plugTerug = Highlight(plugHeen, plugBackOutput, 'on_red')
    print(plugTerug + '\n')


    rotor1Heen = Highlight(rotorChoices[0], rotor1LetterOut, 'on_green')
    rotor1Terug = Highlight(rotor1Heen, retor1BackLetter, 'on_red')
    print(rotor1Terug)
    alpha1Heen = Highlight(alpha_R1, rotor1LetterOut, 'on_green')
    alpha1Terug = Highlight(alpha1Heen, retor1BackLetter, 'on_red')
    print(alpha1Terug + '\n')


    rotor2Heen = Highlight(rotorChoices[1], rotor2LetterOut, 'on_green')
    rotor2Terug = Highlight(rotor2Heen, retor2BackLetter, 'on_red')
    print(rotor2Terug)
    alpha2Heen = Highlight(alpha_R2, rotor2LetterOut, 'on_green')
    alpha2Terug = Highlight(alpha2Heen, retor2BackLetter, 'on_red')
    print(alpha2Terug + '\n')


    rotor3Heen = Highlight(rotorChoices[2], rotor3LetterOut, 'on_green')
    rotor3Terug = Highlight(rotor3Heen, retor3BackLetter, 'on_red')
    print(rotor3Terug)
    alpha3Heen = Highlight(alpha_R3, rotor3LetterOut, 'on_green')
    alpha3Terug = Highlight(alpha3Heen, retor3BackLetter, 'on_red')
    print(alpha3Terug + '\n')


    reflectorHeen = Highlight(reflectorA, reflectIn, 'on_green')
    reflectorTerug = Highlight(reflectorHeen, reflectOut, 'on_red')
    print(reflectorTerug)
    alphaReflector = Highlight(alphabet, alphaLetter, 'on_yellow')
    print(alphaReflector + '\n')


    encrypted += plugBackOutput
    print('Input Text: ' + string)
    print('Output Text: ' + encrypted)