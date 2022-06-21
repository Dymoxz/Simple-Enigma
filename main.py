import random

plugboard = {}

alphabet = "abcdefghijklmnopqrstuvwxyz"


rotorPos1 = 'pezuohxscvfmtbglrinqjwaydk'
rotorPos2 = 'zouesydkfwpciqxhmvblgnjrat'
rotorPos3 = 'ehrvxgaobqusimzflynwktpdjc'
rotorPos4 = 'imetcgfraysqbzxwlhkdvupojn'
rotorPos5 = 'qwertzuioasdfghjkpyxcvbnml' 

rotorList = [rotorPos1, rotorPos2, rotorPos3, rotorPos4, rotorPos5]

rotorChoice = random.sample(rotorList, 3)

input = input("Enter a string: ")

pluggedString = ''

for letter in input:
    if letter in plugboard:
        pluggedString += plugboard[letter]
    else:
        pluggedString += letter
print(pluggedString)

rotor1String = ''
rotor2String = ''
rotor3String = ''

rotorStrings = [pluggedString, '', '', '']

def rotor(read, write, rotorNum, rotor1Position, rotor2Position, rotor3Position):
    a = rotor1Position
    b = rotor2Position
    c = rotor3Position
    for letter in read:
        if a == 26:
            a = 0
            b += 1
        if b == 26:
            b = 0
            c += 1
        if c == 26:
            c = 0
        if rotorNum == rotorChoice[0]:
            # print('EEN', a, b, c)
            letterNum = alphabet.index(letter) + a
            a += 1
        if rotorNum == rotorChoice[1]:
            # print('TWEE', a, b, c)
            letterNum = alphabet.index(letter) + b
        if rotorNum == rotorChoice[2]:
            # print('DRIE', a, b, c)
            letterNum = alphabet.index(letter) + c
        if letterNum >= 26:
            letterNum -= 26
        write += rotorNum[letterNum]
    return write, a, b, c

r1, r2, r3 = 0, 0, 0
x = 1
for rotora in rotorChoice:
    rotorStrings[x], r1, r2, r3 = rotor(rotorStrings[x-1], rotorStrings[x], rotora, r1, r2, r3)
    x += 1
print(rotorStrings)
print(r1,r2,r3)





rotorBack1String = ''
rotorBack2String = ''
rotorBack3String = ''


def rotorReturn(read, write, rotorNum, rotor1Position, rotor2Position, rotor3Position):
    a = rotor1Position
    b = rotor2Position
    c = rotor3Position
    for letter in read:
        if a == 26:
            a = 0
        if rotorNum == rotorChoice[0]:
            # print('EEN', a, b, c)
            letterNum = alphabet.index(letter) + a
        if rotorNum == rotorChoice[1]:
            # print('TWEE', a, b, c)
            letterNum = alphabet.index(letter) + b
        if rotorNum == rotorChoice[2]:
            # print('DRIE', a, b, c)
            letterNum = alphabet.index(letter) + c
        if letterNum >= 26:
            letterNum -= 26
        write += rotorNum[letterNum]
    return write

rotorBackStrings = [rotorStrings[-1], '', '', '']

x = 1
for rotora in rotorChoice:
    rotorBackStrings[x] = rotorReturn(rotorBackStrings[x-1], rotorBackStrings[x], rotora, r1, r2, r3)
    x += 1

print(rotorBackStrings)

allStrings = rotorStrings + rotorBackStrings[1:]
print(allStrings)