"""
Script used to add a path onto each of the lines in a given script
"""

source_file = "../MultitaskModel/singlelabels_train.txt" # The file containing the lists
append_path = "/data/ad6813/Nus-wide/imgs_resized/" # Path to add
dest_file = "../MultitaskModel/singlelabels_train_temp.txt"

source = open(source_file,'r')
dest = open(dest_file,'w')

for line in source:
    dest.write(append_path + line)
