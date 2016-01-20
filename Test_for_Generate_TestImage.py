## -*- coding: utf-8 -*-
#"""
#Created on Tue Jan 19 14:38:45 2016
#
#@author: ThinkPad
#"""
#
#import binascii
#import random
#from os.path import exists, join
#import scipy.io as sio
#import matplotlib.pyplot as plt
#import numpy as np
#import math 
##import Image
##import sys
##from scipy.misc import imsave
#from PIL import Image
from scipy.misc import imsave                                       
from Generate_TestImage import _Generate_TestIamge_

Inputted_number=20;
NISTdataset_Path=str('F:\\WestWellWork\\NISTMatlabAll\\')
Test_Image=_Generate_TestIamge_(Inputted_number,NISTdataset_Path)

image_name=NISTdataset_Path+'test_number'+str(Inputted_number)+'.jpg'
imsave(image_name, Test_Image)
