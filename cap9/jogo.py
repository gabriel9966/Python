import random
from os import name,system

def limpa_tela():
    
    if name == "nt":
        _ = system('cls')#windows
        
    else:
        _ = system('clear')
#board = tabuleiro   , ''' = string com multiplas linhas
board = ["""
         
>>>>>>>Hangman<<<<<<<         
         
   +-----+
   |     |
         |
         |
         | 
         |
         |
================         
    ""","""
   +-----+
   |     |
   o     |
         |
         | 
         |
         |
================   

    """,'''
   +-----+
   |     |
   o     |
   |     |
         | 
         |
         |
================   
    ''','''
   +-----+
   |     |
   o     |
   |     |
    -    | 
         |
         |
================       
    
    ''','''
    
   +-----+
   |     |
   o     |
   |     |
  - -    | 
         |
         |
================       
        
    
    
    ''','''
    
   +-----+
   |     |
   o     |
   |     |
  - -    | 
    \    |
         |
================       

    ''',
    '''
    
   +-----+
   |     |
   o     |
   |     |
  - -    | 
  / \    |
         |
================       

    '''  
]