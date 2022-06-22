
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
def plugboardBack(inputy):
    output = ''
    for letter in inputy:
        if letter in plugDict.values():
            for key, value in plugDict.items():
                if value == letter:
                    output += key
        else:
            output += letter
    return output

newAlpha = plugboardBack(alphabet)
print(newAlpha)

inputa = 'A'

def plugboard(inputy):
    output = ''
    for letter in inputy:
        if letter in plugDict:
            output += plugDict[letter]
        else:
            output += letter
    return output

plugOutput = plugboard(inputa)

def rotor(inputy, rotor):
    output = ''
    for letter in inputy:
        letterIndex = alphabet.index(letter)
        newLetter = rotor[letterIndex]
        output += newLetter
    return output

rotor1output = rotor(plugOutput, III)
rotor2output = rotor(rotor1output, II)
rotor3output = rotor(rotor2output, I)

def reflector(inputy, reflector):
    output = ''
    for letter in inputy:
        letterIndex = alphabet.index(letter)
        newLetter = reflector[letterIndex]
        letterIndex = alphabet.index(newLetter)
        newLetter = reflector[letterIndex]
        output += newLetter
    return output

# def reflector2(inputy, reflector):
#     output = ''
#     for letter in inputy:
#         letterIndex = reflector.index(letter)
#         newLetter = alphabet[letterIndex]
#         output += newLetter
#     return output

reflectorOutput = reflector(rotor3output, reflectorA)


def rotorBack(inputy, rotor, prevRotor):
    output = ''
    for letter in inputy:
        letterIndex = prevRotor.index(letter)
        if rotor == I:
            if letterIndex == 25:
                
                letterIndex -= 25
            else:
                letterIndex = letterIndex
            letter = alphabet[letterIndex + 1]
        else:
            letter = alphabet[letterIndex]
        letterIndex = rotor.index(letter)
        output += letter
        print(letter)
    return output

rotor3backOutput = rotorBack(reflectorOutput, I, reflectorA)
rotor2backOutput = rotorBack(rotor3backOutput, II, I)
rotor1backOutput = rotorBack(rotor2backOutput, III, II)

def plugback(inputy, prevRotor):
    output = ''
    for letter in inputy:
        pluggedIndex = prevRotor.index(letter)
        pluggedLetter = newAlpha[pluggedIndex]
    return pluggedLetter

plugBackOutput = plugback(rotor1backOutput, I)

print(inputa, plugOutput,rotor1output, rotor2output, rotor3output, reflectorOutput, rotor3backOutput, rotor2backOutput, rotor1backOutput, plugBackOutput)