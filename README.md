# Simple-Enigma

Simple version of enigma machine in Python



## **Settings:**
- Select 3 rotors from the following table

|Available Rotors  |Configuration  |
|--|--|
|I|EKMFLGDQVZNTOWYHXUSPAIBRCJ
|II|AJDKSIRUXBLHWTMCQGZNPYFVOE
|III|BDFHJLCPRTXVZNYEIWGAKMUSQO
|IV|ESOVPZJAYQUIRHXLNFTGKDCMWB
|V|VZBRGITYUPSDNHLXAWMJQOFECK

*Rotors 1 and 3 are swapped in the code :( will fix soon

- Select the starting position for each rotor (e.g. ABC)
The rotors will have this letter on top
- Choose which letters to connect via the plugboard. When you type one letter it will go trough as the one it is connected to 

![image](https://user-images.githubusercontent.com/82333980/175790545-fc96ecd8-efd1-4a14-bb6d-8d62115c3e94.png)

## GUI
![image](https://user-images.githubusercontent.com/82333980/175815375-640c8458-6d8c-4190-ac65-e96fb6565901.png)
Every 2 lines with letters is a rotor (except for the top one, which is the plugboard and the bottom one, which is the reflector)
- The cyan letters show the path the input takes to the reflector
- The blue letter is the reflection
- The magenta is the path the reflected letter takes towards the output (back into the plugboard)




