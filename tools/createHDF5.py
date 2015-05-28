''' Create HDF5 database to load in vector labels. 
Takes a single file as the source, which contains the data in 
the format: path/to/image [label1 label2 label3]
'''

import h5py
from PIL import Image
import numpy as np
# Replace these 4 with relevent paths and names
path = '/home/alex/Documents/Caffe_First_Attempt/'
imgPath = path + 'imgs/'
imageInputFile = path + 'temp/test_labels.txt'
dataBaseLocation = path + 'temp/'
dbName = 'test.hdf5'
resize_dims = (256, 256)
nLabels = 2 # Number of labels



imageList = open(imageInputFile, 'r')
# Annoying method to find length of file
nImages = 0
for line in imageList:
    nImages += 1
    
f = h5py.File(dataBaseLocation + dbName, 'w')
imgdb = f.create_dataset("data", (nImages,3,resize_dims[0],resize_dims[1]), maxshape=(None,3,resize_dims[0],resize_dims[1]), dtype='i8')
labeldb = f.create_dataset("label",(nImages,nLabels), maxshape=(None,nLabels), dtype='i1')

for i, line in enumerate(imageList):
    words = line.split()
    labelIdx = range(line.index('['),line.index(']'))
    labelVec = eval(line[line.index('['):line.index(']')+1])
    # Open and resize the image
    img = Image.open(imgPath + words[0])
    img = img.resize(resize_dims, Image.ANTIALIAS)
    npImg = np.array(img)
    npImg = npImg[:,:,[2,1,0]] # Swap channel order to B,G,R to fit with imagenet
    npImg = npImg.transpose(2,0,1) # Put in order channels, x, y
    imgdb[i,:,:,:] = npImg
    labeldb[i,:] = labelVec

f.close()
    
    
    
