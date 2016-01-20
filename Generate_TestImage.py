# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:23:45 2016

This code is used for generating any number of random number or letter, 
After finish inputting the number or letter, we revise the pixel value of the inputted number or  letter 
into its corresponding decimal value.
And then put all the inputted number of letters into one test image (600*800) randomly.
There mustn't have overlap bettwen two number or letters 

@author: Oscar
@E-mail: Xinghui.Shu@westwell-lab.com
"""

#import binascii
import random
#from os.path import exists
import scipy.io as sio
import matplotlib.pyplot as plt
import numpy as np
import math 
#import Image
#import sys
#from scipy.misc import imsave
def _Generate_TestIamge_(Inputted_number,pathway):
    #Imshow the image of the Matrix
    def _Display_(vec):
    #    if not exists(vec):
    #        raise("Input Matrix vec_A for _Display_ function is not found")
        fig = plt.figure(1)
        ax = plt.imshow(vec)
        plt.show()
        
    #Initialize the letter and word. Input random number or letter randomly from NISTdataset
    def _Initial_():
    #    if not exists(matfn):
    #        raise IOError("Input Path_Way for _Initial_ function is not found")
#        matfn=str('F:\\WestWellWork\\NISTMatlabAll\\')
        image_output = np.zeros((600, 800))
        ii=0
        
        # Randomly generate and Check input number and letter
        while (ii<48  or  (ii>57 and ii<65)   or  ( ii>90 and ii<97 ) or ii> 122):
            ii=math.ceil(random.random()*74)+48
        if ((ii>=48  and ii<=57) or (ii>=65 and  ii<=90 ) or (ii>=97 and ii<=122)):    
            hexVal=hex(int(ii))
        else:
            raise("Wrong random ASCII Number")
        # Load the corresponding number or letter    
        path=pathway+hexVal[2:4]+'.mat'
        data=sio.loadmat(path)
        ImageData=data["characterData"]
        randum=int(math.ceil(random.random()*ImageData.shape[0]))
        charImg = np.reshape(ImageData[randum,:],(128,128))
        
        # Initial the center of the number of letter
        Center_x=int(0)
        Center_y=int(0)
        
        # Randomly generate and Check the center of the number of letter
        while (Center_x<64 or  Center_x>600-64):
            Center_x=int(math.ceil(random.random()*600))
        while (Center_y<64 or Center_y>600-64 ):
            Center_y=int(math.ceil(random.random()*800))
            
        if(Center_x>=64 and  Center_x<=600-64 and Center_y>=64 and  Center_y<=600-64):
            image_output[Center_x-64:Center_x+64,Center_y-64:Center_y+64]=charImg
        else:
            raise("Wrong random center point")   
        return (image_output,hexVal[2:4])
    
    # Revise the image pixel value of the input number or letter into its corresponding decimal value
    def _PixelValue_(vec,hex_num):
    #    hex_num=int(str.decode(hex_num))
    #    if (hex_num)
    #        hex_num=int(hex_num,10)
        hex_num=int(hex_num,16)    
        for i in range (0,600):
            for j in range (0,800):
                if (vec[i][j]>0):
                    vec[i][j]=hex_num
        return (vec)
     
    # Make a multiply between the original Matrix and new inputted Matrix   
    def _MutiplyVec_(vec_A,vec_B):
    #    if not exists(vec_A):
    #        raise IOError("No input Matrix vec_A for _MutiplyVec_ function is not found: %s"% vec_A) 
    #    if not exists(vec_B):
    #        raise IOError("No input Matrix vec_B for _MutiplyVec_ function is not found: %s"% vec_B)
        Vec_C=[]
        Vec_C= np.array(vec_A)*np.array(vec_B)
        return (Vec_C)
        
    
    
    # The number of the number or letter you want to input: Num
    Num=Inputted_number    
     
    # The Path_Way you can Change: matfn
#    matfn=str('F:\\WestWellWork\\NISTMatlabAll\\')
    
    # The times of overlaps between two word
    found_time=0
    
    #Initial the first number
    Char_A,hex_numA=_Initial_()
    Char_A=_PixelValue_(Char_A,hex_numA)
    
    #The number of Inputted number or letter
    Num_of_Input=0
    
    while (Num_of_Input<Num):
        #Initial the next number
        Char_B,hex_numB=_Initial_()
        Char_B=_PixelValue_(Char_B,hex_numB)
        
        # Make a multiply between the original Matrix and new inputted Matrix   
        Multi_Result=_MutiplyVec_(Char_A,Char_B)
        
        # Test Matrix: All-Zero Matrix
        Test_Matrix=np.zeros((600,800))
        
        # Check that whether there are some overlaps between two word: 
        # By checking whether the Result Matrix is all-zeor after make the multiply
        # If it is not all zero, please re-input the Matrix before  
        while (((Multi_Result!=Test_Matrix).any()) and Num_of_Input<Num):
            found_time+=1
            print ("Retry,exists overlap! The times of Overlap:",found_time)
            Char_B,hex_numB=_Initial_()
            Char_B=_PixelValue_(Char_B,hex_numB)
            Multi_Result=_MutiplyVec_(Char_A,Char_B)
        
        # If the result is all zero Matrix, Add New number or letter sucessfully       
        if ((Multi_Result==Test_Matrix).all()):        
            Char_A=np.array(Char_A)+np.array(Char_B)
            Num_of_Input+=1
            print("Add New number or letter successfully !")
        else:
            print("Fail to add new number or letter, Still exists overlap !")
    #        raise IOError("Still exists overlap")
        print("The number of Inputted number or letter:", Num_of_Input)
    
    if (Num_of_Input>=Num):
        _Display_(Char_A)
    else:
        print("Have not finish inputting number or letter")
        
    return (Char_A)
     
    



