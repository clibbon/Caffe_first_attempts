''' Sample batch used to select one single batch of images 
for testing through the network '''
nImages         = 1
filePath        = '/home/alex/Documents/Caffe_First_Attempt/MultitaskModel/'
inputFileStr    = filePath + 'singlelabels_val_temp.txt'
outputFileStr   = filePath + 'singlelabels_val_temp_singlebatch.txt'

inputFile       = open(inputFileStr, 'r')
outputFile      = open(outputFileStr, 'w')

for x in range(0,nImages):
    lineToWrite = next(inputFile)
    outputFile.write(lineToWrite)

inputFile.close()
outputFile.close()
    