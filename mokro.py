#! /usr/bin/env python3
# Copyright 2013 Cory Lutton
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
""" The Enigma machines were a family of portable cipher machines
with rotor scramblers. Good operating procedures, properly enforced,
would have made the cipher unbreakable.
However, most of the German armed and secret services and civilian agencies
that used Enigma employed poor procedures and it was these that allowed the
cipher to be broken.

The German plugboard-equipped Enigma became the Third Reich's
principal crypto-system. It was reconstructed by the Polish
General Staff's Cipher Bureau in December 1932Ã¢â‚¬â€with the aid of
French-supplied intelligence material that had been obtained
from a German spy. Shortly before the outbreak of World War II,
the Polish Cipher Bureau initiated the French and British into its
Enigma-breaking techniques and technology at a conference held in Warsaw.

From this beginning, the British Government Code and Cypher School at
Bletchley Park built up an extensive cryptanalytic facility. Initially,
the decryption was mainly of Luftwaffe and a few Army messages,
as the German Navy employed much more secure procedures for using Enigma.

Alan Turing, a Cambridge University mathematician and logician,
provided much of the original thinking that led to the design of
the cryptanalytical Bombe machines, and the eventual breaking of naval Enigma.
However, when the German Navy introduced an Enigma version with a
fourth rotor for its U-boats, there was a prolonged period when those messages
could not be decrypted. With the capture of relevant cipher keys and the use
of much faster U.S. Navy Bombes, regular, rapid reading of
German naval messages resumed.

http://www.matematiksider.dk/enigma_eng.html
http://users.telenet.be/d.rijmenants/en/enigmaproc.htm
http://ciphermachines.com/enigma
http://enigmaco.de/enigma/enigma.html

"""
import sys

__version__ = "1.0"


class Enigma:
    """ An Enigma machine is any of a family of related
    electro-mechanical rotor cipher machines used for the encryption
    and decryption of secret messages. Enigma was invented by
    German engineer Arthur Scherbius at the end of World War I.
    The early models were used commercially from the early 1920s,
    and adopted by military and government services of several countries
    Ã¢â‚¬â€ most notably by Nazi Germany before and during World War II.
    Several different Enigma models were produced, but the German
    military models are the ones most commonly discussed.

    """
    def __init__(self):
        self.numcycles = 0
        self.rotors = []

        # Settings for the machine
        self.rotorsettings = [("III", 0),
                            ("II", 0),
                            ("I", 0)]
        self.reflectorsetting = "B"
        self.plugboardsetting = []

        # Create the plugboard
        self.plugboard = Plugboard(self.plugboardsetting)

        # Create each of the rotors
        for i in range(len(self.rotorsettings)):
            self.rotors.append(Rotor(self.rotorsettings[i]))

        # Create reflector
        self.reflector = Reflector(self.reflectorsetting)

    def print_setup(self):
        """ Prints initial setup information """
        print()
        print("Rotor sequence: (right to left)")
        for r in self.rotors:
            print(r.setting, "\t", r.sequence)

        print()
        print("Reflector sequence:")
        print(self.reflector.setting, "\t", self.reflector.sequence, "\n")

        print("Plugboard settings:")
        print(self.plugboard.mapping, "\n")

    def reset(self):
        """ Reset to initial state """
        self.numcycles = 0
        for r in self.rotors:
            r.reset()

    def encode(self, c):
        """ Run a cycle of the enigma with one character """
        c = c.upper()

        if (not c.isalpha()):
            return c

        # To avoid merely implementing a simple (and easily breakable)
        # substitution cipher, every key press caused one or more rotors
        # to step before the electrical connections were made.
        self.rotors[0].rotate()

        # Double step
        if self.rotors[1].base[0] in self.rotors[1].notch:
            self.rotors[1].rotate()

        # Normal stepping
        for i in range(len(self.rotors) - 1):
            if(self.rotors[i].turnover):
                self.rotors[i].turnover = False
                self.rotors[i + 1].rotate()

        # Passthrough the plugboard forward
        index = self.plugboard.forward(c)

        # Move through the rotors forward
        for r in self.rotors:
            index = r.forward(index)

        # Pass through the reflector
        index = self.reflector.forward(index)

        # Move back through rotors in reverse
        for r in reversed(self.rotors):
            index = r.reverse(index)

        # Passthrough the plugboard reverse
        c = self.plugboard.reverse(index)

        return c


class Rotor:
    """ The rotors (alternatively wheels or drums, Walzen in German)
    formed the heart of an Enigma machine. Each rotor was a disc
    approximately 10 cm (3.9 in) in diameter made from hard rubber
    or bakelite with brass spring-loaded pins on one face arranged
    in a circle; on the other side are a corresponding number
    of circular electrical contacts. The pins and contacts represent
    the alphabet Ã¢â‚¬â€ typically the 26 letters AÃ¢â‚¬â€œZ.

    Setting Wiring                      Notch   Window  Turnover
    Base    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    I       EKMFLGDQVZNTOWYHXUSPAIBRCJ  Y       Q       R
    II      AJDKSIRUXBLHWTMCQGZNPYFVOE  M       E       F
    III     BDFHJLCPRTXVZNYEIWGAKMUSQO  D       V       W
    IV      ESOVPZJAYQUIRHXLNFTGKDCMWB  R       J       K
    V       VZBRGITYUPSDNHLXAWMJQOFECK  H       Z       A
    VI      JPGVOUMFYQBENHZRDKASXLICTW  H/U     Z/M     A/N
    VII     NZJHGRCXMYSWBOUFAIVLPEKQDT  H/U     Z/M     A/N
    VIII    FKQHTLXOCBJSPDZRAMEWNIUYGV  H/U     Z/M     A/N

    """
    def __init__(self, settings):
        """ Setup an enigma transformation rotor """
        self.setting = settings[0]
        self.ringoffset = settings[1]
        self.base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings = {
                "I":    ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", ["R"], ["Q"]],
                "II":   ["AJDKSIRUXBLHWTMCQGZNPYFVOE", ["F"], ["E"]],
                "III":  ["BDFHJLCPRTXVZNYEIWGAKMUSQO", ["W"], ["V"]],
                "IV":   ["ESOVPZJAYQUIRHXLNFTGKDCMWB", ["K"], ["J"]],
                "V":    ["VZBRGITYUPSDNHLXAWMJQOFECK", ["A"], ["Z"]],
                "VI":   ["JPGVOUMFYQBENHZRDKASXLICTW", ["AN"], ["ZM"]],
                "VII":  ["NZJHGRCXMYSWBOUFAIVLPEKQDT", ["AN"], ["ZM"]],
                "VIII": ["FKQHTLXOCBJSPDZRAMEWNIUYGV", ["AN"], ["ZM"]]}
        self.turnovers = self.settings[self.setting][1]
        self.notch = self.settings[self.setting][2]
        self.sequence = None
        self.turnover = False
        self.reset()

    def reset(self):
        """ Reset the rotor positions """
        self.base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.sequence = self.sequence_settings()
        self.ring_settings()

    def sequence_settings(self):
        """ Set the intial sequence """
        return self.settings[self.setting][0]

    def ring_settings(self):
        """ Apply the initial ring settings offset """
        for _ in range(self.ringoffset):
            self.rotate()

    def forward(self, index):
        """ Move right to left through the rotor """
        return self.base.index(self.sequence[index])

    def reverse(self, index):
        """ Move left to right back through the rotor """
        return self.sequence.index(self.base[index])

    def rotate(self):
        """ Cycle the rotor 1 position """
        self.base = self.base[1:] + self.base[:1]
        self.sequence = self.sequence[1:] + self.sequence[:1]

        if(self.base[0] in self.turnovers):
            self.turnover = True


class Reflector:
    """ With the exception of the early Enigma models A and B,
    the last rotor came before a reflector (German: Umkehrwalze,
    meaning reversal rotor), a patented feature distinctive of the
    Enigma family amongst the various rotor machines designed
    in the period. The reflector connected outputs of the
    last rotor in pairs, redirecting current back through the
    rotors by a different route. The reflector ensured that
    Enigma is self-reciprocal: conveniently, encryption was
    the same as decryption. However, the reflector also gave
    Enigma the property that no letter ever encrypted to itself.
    This was a severe conceptual flaw and a cryptological mistake
    subsequently exploited by codebreakers.

    Setting     Wiring
    Base        ABCDEFGHIJKLMNOPQRSTUVWXYZ
    A           EJMZALYXVBWFCRQUONTSPIKHGD
    B           YRUHQSLDPXNGOKMIEBFZCWVJAT
    C           FVPJIAOYEDRZXWGCTKUQSBNMHL

    """
    def __init__(self, setting):
        self.setting = setting
        self.base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.settings = {"A":   "EJMZALYXVBWFCRQUONTSPIKHGD",
                        "B":    "YRUHQSLDPXNGOKMIEBFZCWVJAT",
                        "C":    "FVPJIAOYEDRZXWGCTKUQSBNMHL"}

        self.sequence = self.sequence_settings()

    def sequence_settings(self):
        """ Set the intial sequence """
        return self.settings[self.setting]

    def forward(self, index):
        """ Passthrough the reflector. """
        return self.sequence.index(self.base[index])


class Plugboard:
    """ The plugboard (Steckerbrett in German) permitted variable wiring
    that could be reconfigured by the operator.
    It was introduced on German Army versions in 1930, and was soon adopted
    by the Navy as well. The plugboard contributed a great deal to the
    strength of the machine's encryption: more than an extra rotor would
    have done. Enigma without a plugboard (known as unsteckered Enigma)
    can be solved relatively straightforwardly using hand methods;
    these techniques are generally defeated by the addition of a plugboard,
    and Allied cryptanalysts resorted to special machines to solve it.

    """
    def __init__(self, mapping):
        """ mapping = [("A", "B"), ("C", "D")] """
        self.base = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.mapping = {}

        for m in self.base:
            self.mapping[m] = m

        for m in mapping:
            self.mapping[m[0]] = m[1]
            self.mapping[m[1]] = m[0]

    def forward(self, c):
        """ Return the index of the character """
        return self.base.index(self.mapping[c])

    def reverse(self, index):
        """ Return the character of the index """
        return self.mapping[self.base[index]]


def main():
    """ Create and run an Enigma machine. """

    machine = Enigma()
    ciphertext = ""

    try:
        plaintext = sys.argv[1]
        machine.print_setup()

        print("Plaintext", "\t", plaintext)
        for character in plaintext:
            ciphertext += machine.encode(character)

        print("Ciphertext", "\t", ciphertext)

        # Reset and Decode same message
        machine.reset()
        plaintext = ""
        for character in ciphertext:
            plaintext += machine.encode(character)

        print("Plaintext", "\t", plaintext, "\n")
    except IndexError:
        for plaintext in sys.stdin:
            for character in plaintext:
                sys.stdout.write(machine.encode(character))

if __name__ == '__main__':
    #import cProfile
    #cProfile.run('main()')
    main()