#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 20:58:59 2021

@author: basakulcay
"""


import random

def main():
    again='y'
    count=0

    while again=='y':
        print('I have a number between 1 to 1000.')
        print('Can you guess my number?')
        print('Please type your first guess') 
        
        number=random.randint(1, 1000)
        print(number)
    
        guess=int(input(''))
       
        while guess !='':
            if  guess>number:
                print('Too high, try again!')
                count+=1
                print('count:',count)
                guess=int(input(''))
                
                
            elif guess<number:
                print('Too low, try again!')
                count+=1
                print('count:',count)
                guess=int(input(''))

                
            elif guess==number:
                print('Excellent!! You guessed the number!!!!')
                print('Would you like to try again? (y or n)')
                count+=1
                print('count:',count)
                again=str(input(''))
                break
            
            else:
                print('You entered an invalid value')
     
main()

