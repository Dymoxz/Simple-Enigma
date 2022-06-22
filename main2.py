rotorPos1 = 'QWERTZUIOASDFGHJKPYXCVBNML'
rotorPos2 = 'JGDQOXUSCAMIFRVTPNEWKBLZYH'
rotorPos3 = 'NTZPSFBOKMWRCJDIVLAEYUXHGQ'
rotorPos4 = 'JVIUBHTCDYAKEQZPOSGXNRMWFL'
reflector = 'QYHOGNECVPUZTFDJAXWMKISRBL' 

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rotorList = [rotorPos1, rotorPos2, rotorPos3, rotorPos4]

rotorChoice = [rotorPos1, rotorPos2, rotorPos3]

input = input("Enter a stringus: ")




rotor1Output = ''
for letter in input:
    letterNum = alphabet.index(letter)
    rotor1Input = letterNum
    rotor1Output += rotorPos1[rotor1Input]

print(rotor1Output)

rotor2Output = ''
for letter in rotor1Output:
    letterNum = alphabet.index(letter)
    rotor2Input = letterNum
    rotor2Output += rotorPos2[rotor2Input]

print(rotor2Output)

rotor3Output = ''
for letter in rotor2Output:
    letterNum = alphabet.index(letter)
    rotor3Input = letterNum
    rotor3Output += rotorPos3[rotor3Input]

print(rotor3Output)






reflectorOutput = ''
for letter in rotor3Output:
    letterNum = alphabet.index(letter)
    reflectorInput = letterNum
    reflectorOutput += reflector[reflectorInput]

print(reflectorOutput)








rotor1Output = ''
for letter in reflectorOutput:
    letterNum = alphabet.index(letter)
    rotor1Input = letterNum
    rotor1Output += rotorPos1[rotor1Input]

print(rotor1Output)

rotor2Output = ''
for letter in rotor1Output:
    letterNum = alphabet.index(letter)
    rotor2Input = letterNum
    rotor2Output += rotorPos2[rotor2Input]

print(rotor2Output)

rotor3Output = ''
for letter in rotor2Output:
    letterNum = alphabet.index(letter)
    rotor3Input = letterNum
    rotor3Output += rotorPos3[rotor3Input]

print(rotor3Output)