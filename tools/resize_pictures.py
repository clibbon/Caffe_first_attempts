'''For pre-processing all images for use in the training 
network. All images will be resized to 227*227, and 
cropped if need be '''

import argparse

parser = argparse.ArgumentParser(description='Resize and crop images.')
parser.add_argument('--source', dest = 'source_folder', action='store',
                    default='.')
parser.add_argument('--dest', dest = 'destination_folder', action='store',
                    default='./resized/')
args = parser.parse_args()
resize_dims = (227, 227) # Number of pixels in resized image
import os
from PIL import Image
from my_resize import resize

filenames = os.listdir(args.source_folder)
errorRecord = open('MissingImages.txt', 'w')

# Loop through all images and resize
for filename in filenames:
    try:
        img = Image.open(args.source_folder + '/'+ filename)
        resize(img, resize_dims, True, args.destination_folder + '/' + filename)
    except IOError:
        errorRecord.write(filename + '\n')
        print "Could not load image {}".format(filename)