# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:14:57 2019

@author: User
"""
class Animal(object):
    def __init__(self, color, size):
        self.color = color
        self.size = size
        
#The sub-classes "shark" and "whale" inherit the atributes from the super class "Animal"
        
class shark(Animal):
    #We apply polymrphism when we use two or more methods with the same name
    #In order to know which of theese methods is going to be executed, we need
    #to know which class we are using.
    def Show_Size(self):
        print("The size of the " + self.color + " shark is: " + str(self.size))
        
        
class whale(Animal):
    def Show_Size(self):
        print("The size of the " + self.color + " whale is: " + str(self.size))
        
        
Shark_1 = shark("White",100)
Wahle_1 = whale("Black",1000)

Shark_1.Show_Size()
Wahle_1.Show_Size()

