#the purpose of this program is to convert .jpg images to .pdf images (or other types?) with specific compression. 

import glob
import shutil
import os

src_dir = "/Users/Nicholas/Desktop/Cobra insurance continuation documents/unconverted"
dst_dir = "/Users/Nicholas/Desktop/Cobra insurance continuation documents/converted"

print os.path.join(src_dir)

print glob.iglob(os.path.join(src_dir))

for file in glob.iglob(os.path.join(src_dir),):
    if file.endswith(".jpg"):   
        shutil.move(src_dir,dst_dir)

#for file in glob.iglob(os.path.join(src_dir)):#the problem is here...
#    shutil.copy(file, dst_dir)
#    print "ok"

src_dir_obj = ["a"]
dst_dir_obj = ["a"]

if cmp(src_dir_obj, dst_dir_obj):
    print "these files: ", os.listdir(source_dir), " have been imported from /Users/Nicholas/Desktop/Cobra insurance continuation documents/unconverted to /Users/Nicholas/Desktop/Cobra insurance continuation documents/converted"
else:
    print "failed"
    
