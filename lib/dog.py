#!/usr/bin/env python3

class Dog:
    def __init__(self,name, breed="Mutt"):
        self.name = name
        self.breed = breed
    
    def breed(self):
        print("Woof!")

fido = Dog("Fido")
fido.name

