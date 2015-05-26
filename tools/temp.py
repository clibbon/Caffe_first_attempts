# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:50:05 2015

@author: alex
"""

from PIL import Image
tmp = Image.open('/home/alex/Documents/Caffe_First_Attempt/100000.jpg')
(w, h) = tmp.size
if w != 227 | h != 227:
    print "Image {} is incorrect".format(w)