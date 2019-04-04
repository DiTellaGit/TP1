#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 00:07:13 2019

@author: mat
"""

import sys
def esPrimo(n):
    i = 2
    esprimo= "si"
    while i <= n/2:
        if n % i == 0:
            esprimo= "no"
            break 
        else:
            i += 1
    return esprimo
            
def iesimoPrimo(i):
    listaprimos=[]
    contar = 2 
    while len(listaprimos) < i:
        if esPrimo(contar) == "si":
            listaprimos.append(contar)
        contar += 1
        
    return listaprimos[i-1]
        
def cantidadDivisoresPrimos(n):
    i = 1
    contar = 0
    while iesimoPrimo(i) <= n/2:
        if n % iesimoPrimo(i)== 0:
            contar += 1
            i += 1
        else:
            i += 1
    return  contar       

def iesimoDivisorPrimo(n, i):
    m = 0
    c = 1
    if i <= cantidadDivisoresPrimos(n):
        while m < i:
            if n % iesimoPrimo(c) == 0:
                c += 1
                m += 1
            else:
                c +=1
            return iesimoPrimo(c-1)
    else:
        return str(n)+" no tiene "+str(i)+" divisores primos"

def primeraLaguna(n):
    i = 2
    laguna = iesimoPrimo(i) - iesimoPrimo(i-1) -1
    if n % 2 !=0:
        while laguna < n:
            i += 1
            laguna = iesimoPrimo(i) - iesimoPrimo(i-1) -1
        return iesimoPrimo(i-1) + 1
    else:
        return "no existen lagunas de numeros pares"


#print(esPrimo(104537))
#iesimoPrimo(4)
print(cantidadDivisoresPrimos(15))
#iesimoDivisorPrimo(5, 1)
#primeraLaguna(33)