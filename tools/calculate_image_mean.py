""" Find imageset mean. Calculates the mean of a data in a given file for each 
channel, and saves them in npy format, in the order BGR """

from PIL import Image
import numpy as np
caffe_root = '/home/alex/Caffe/caffe/'
import sys
sys.path.insert(0, caffe_root + 'python')
from caffe import io

path = '/home/alex/Documents/Caffe_First_Attempt/'
imageSet = path + 'resized'
imageLabels = path + 'temp/test_labels.txt'
destination = path + 'temp/img_mean.binaryproto'
img_size = (227, 227)
img_mean = np.zeros((3,img_size[0],img_size[1]))
imageFile = open(imageLabels,'r')
nImages = 0

for line in imageFile:
    img = Image.open(imageSet + '/' + line.split()[0])
    img_mean += np.array(img).transpose(2,0,1)
    nImages += 1
img_mean = img_mean/nImages
img_mean = img_mean[[2,1,0],:,:]
meanBlob = io.array_to_blobproto(np.expand_dims(img_mean,0))
toSave = open(destination,'wb')
toSave.write(meanBlob.SerializeToString())
toSave.close()
