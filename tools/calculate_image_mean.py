""" Find imageset mean. Calculates the mean of a data in a given file for each 
channel, and saves them in npy format, in the order BGR """

from PIL import Image
import numpy as np
path = '/home/alex/Documents/Caffe_First_Attempt/'
imageSet = path + 'resized'
imageLabels = path + 'temp/test_labels.txt'
destination = path + 'temp/img_mean.npy'
img_size = (227, 227)
img_mean = np.zeros((3,img_size[0],img_size[1]))
imageFile = open(imageLabels,'r')
nImages = 0

for line in imageFile:
    img = Image.open(imageSet + '/' + line.split()[0])
    img_mean += np.array(img).transpose(2,0,1)
    nImages += 1
img_mean = img_mean/nImages
np.save(destination, img_mean)
