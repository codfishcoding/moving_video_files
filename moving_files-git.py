import shutil
import os
import subprocess

source_folder = '/path/to/sourcefolder'
destination_folder = '/path/to/destinationfolder'

files = os.listdir(source_folder)

for f in files:
    full_path = source_folder + "/" + f
    #was going to use subprocess but didnt work with video files only txt files
    #though i would keep it in, in case anyone else has this bug
    #subprocess.Popen("mv" + " " + full_path + " " + destination_folder, shell=True)
    shutil.move(full_path , destination_folder)

print('files moved')