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
            if aux[2] == 96: #como só existem 3 canais de cor, (branco(255,255,255), preto(0,0,0) e verde, só precisa verificar uma escala do RGB
                cont_verdes+=1
    print("verdes: "+str(cont_verdes));

def alteraCores(img):
    altura, largura, cores = img.shape;
    for i in range(0, altura):
        for j in range(0, largura):
            if img.item(i,j,0) ==0 and img.item(i,j,0) ==0 and img.item(i,j,2)==0:

                img.itemset((i,j,0), 0);
                img.itemset((i,j,1), 0);
                img.itemset((i,j,2), 0);
            if img.item(i, j, 0) == 255 and img.item(i, j, 0) == 255 and img.item(i, j, 2) == 255:
                img.itemset((i, j, 0), 0);
                img.itemset((i, j, 1), 192);
                img.itemset((i, j, 2), 96);
            else:
                img.itemset((i, j, 0), 0);
                img.itemset((i, j, 1), 192);
                img.itemset((i, j, 2), 96);
    printImagem(img);
            
            
main();
