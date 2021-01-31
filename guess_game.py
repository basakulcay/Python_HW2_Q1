#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 17:39:40 2021

@author: basakulcay
"""
import random
def main():
    

    again='y'
    
    while again=='y':
          count=0
          print("I have a number between 1 to 1000.")
          print("Can you guess my number?")
          guess=int(input("Please type your first guess:"))
    
    
          number=random.randint(1,1000)
        
    
          while guess !='':
              if     number > guess:
                     count+=1
                     guess=int(input("Too low.Try again:"))
                     
              elif   number < guess:
                     count+=1
                     guess=int(input("Too high.Try again:"))
                     
              else:
                    count+=1 
                    if count>10 :
                       print("You should be able to do better!!!")
                    elif count==10:
                       print("Ahah! You know the secret!") 
                    else:
                       print("Either you know the secret or you got lucky!") 
                  
                    again=str(input("Excellent!! You guessed the number!!! Would you like to play again (y or n)?"))
                    break
                  


main()

