import numpy as np
import matplotlib.pyplot as plt

def derivacija(fun,x,h,korak=3):
    if korak == 3:
        print((fun(x+h)-fun(x-h))/(2*h))
    if korak ==2:
        print((fun(x)+fun(x-h))/h)

def der(fun,doli,gori,h,korak=3):
    tocke=[]
    iznosu3=[]
    iznosu2=[]
    a=0
    b=0
    while doli<=gori:
        tocke.append(doli)
        a=(fun(doli+h)-fun(doli-h))/(2*h)
        iznosu3.append(a)
        b=(fun(doli)-fun(doli-h)/h)
        iznosu2.append(b)
        doli=doli+h

    if korak==3:
        return tocke, iznosu3
    if korak==2:
        return tocke, iznosu2
    

def integral(fun, doli, gori, h):
    tocked = []
    tockeg = []
    donja = []
    gornja = []
    gornjavrijednost = 0
    donjavrijednost = 0

    while doli <= gori:
        #formula za donju medu
        tocked.append(doli)
        donjavrijednost = donjavrijednost + fun(doli) * h
        donja.append(donjavrijednost)

        doli = doli + h
        #formula za gornju medu
        tockeg.append(doli)
        gornjavrijednost = gornjavrijednost + fun(doli) * h
        gornja.append(gornjavrijednost)

    return tocked, donja, tockeg, gornja


def trapezna(fun, doli, gori, korak):
    h = (gori - doli) / korak
    donja = 0
    gornja = 0
    prosjek = 0
    i = 0
    while i < korak:

        donja = donja + fun(doli) * h
        gornja =  gornja + fun(doli + h) * h
        doli = doli + h
        prosjek = prosjek + ((h/2) * (fun(doli-h) + fun(doli))) 
        i = i + 1

    return donja, gornja, prosjek