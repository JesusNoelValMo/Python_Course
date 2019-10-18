# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:14:57 2019

@author: User
"""
class shark():
    def __init__(self):
        self.size = 100
        
    def Set_Size(self):
        
        print("The size of the shark is: " + str(self.size))
        
        
class whale():
    def __init__(self):
        self.size = 1000
        
    def Set_Size(self):
        
        
        print("The size of the whale is: " + str(self.size))
        
        
def wich_fish(fish):
    fish.Set_Size()
    
Shark_1 = shark()
whale_1 = whale()
wich_fish(Shark_1)

    
    
