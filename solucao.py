# -*- coding: utf-8 -*-
"""
Created on Mon May 10 18:19:58 2021

@author: omar
"""

import cv2;
import numpy as np;
def main():
    img = cv2.imread("Syngenta.BMP",1);
    contaVerdes(img);
    alteraCores(img)
def printImagem(img):
    from matplotlib import pyplot as plt;
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show();    
def contaVerdes(img):    
    altura, largura, canais_de_cor = img.shape;
    cont_verdes =0;
    cont_brancos =0;
    for i in range(0, altura):
        for j in range (0, largura):
            aux = img[i][j];
            if aux[2] == 96:
                cont_verdes+=1
            else:
                cont_brancos+=1;
    print("verdes: "+str(cont_verdes));

def alteraCores(img):
    altura, largura, cores = img.shape;
    for i in range(0, altura):
        for j in range(0, largura):
            
            
            red = img.item(i,j,2);
            green = img.item(i,j,1);
            blue = img.item(i,j,0);
            if red==0 and green==0 and blue==0:
                img.itemset((i,j,1),250); #green
                img.itemset((i,j,0),250); # blue
                img.itemset((i,j,2),250); #red
            
    printImagem(img);
            
            
main();
