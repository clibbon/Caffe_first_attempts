'''Check images walks through the images, loads them, and checks that 
the dimensions match the given dimensions'''
from PIL import Image
imgList = open('../MultitaskModel/singlelabels.txt')
desired_size = 227 # The size images should be
display = True

for line in imgList:
    words = line.split()
    tmp = Image.open('/data/ad6813/Nus_wide/imgs_resized/' + words[0])
    (w, h) = tmp.size
    if display: print tmp.size
    if w != desired_size | h != desired_size:
        print "Image {} is incorrect".format(words[0])