#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

# {(([])[])[]}[]
# { }[ ]
# p1 = (([])[])[]}[]
# p2 = {(([])[])[] , []

def isBalanced(s):
    return check_pair(s)
    
def check_pair(s):
    print(f"s: {s} | s[0]: {s[0]}")
    aberto, fecho = '',''
    chave_aberta, chave_fechada = '{','}'
    parenteses_aberto, parenteses_fechado = '(',')'
    colchetes_aberto, colchetes_fechado = '[',']'
    if s[0] == chave_aberta:
        aberto = chave_aberta
        fecho = chave_fechada
    if s[0] == parenteses_aberto:
        aberto = parenteses_aberto
        fecho = parenteses_fechado
    if s[0] == colchetes_aberto:
        aberto = colchetes_aberto
        fecho = colchetes_fechado
    
    ocorrencias = s.count(fecho)
    total = s.split(aberto,1)[1].rsplit(fecho,1)  
    p1 = s.split(s[0],1)
    p1_fechado = p1[1].split(fecho,1)
    p2 = s.split(fecho,1)
    p2_fechado = p2[0].split(aberto,1)
    print(f"total: {total}")
   
    print(f"ocorrencias: {ocorrencias}")
    print(f"p1: {p1} | p1_fechado: {p1_fechado}")
    print(f"p2: {p2} | p2_fechado: {p2_fechado}")
    balanced = 0
    if p1_fechado[1] == p2[1]:
        balanced += 1
        
    if p2_fechado[1] == p1_fechado[0]:
        balanced += 1
    
    if p2_fechado[0] == p1[0]:
        balanced += 1
        
    if balanced < 3:
        print("NO")
        return "NO"
        
    if total[0] == '' and total[1]=='':
        print("YES")
        return "YES"
    
    check_pair(total[0])
    check_pair(total[1])
        
    
    
conjunto = "{([])}"