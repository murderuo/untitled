import os

print(os.listdir())
files=os.listdir()
n_files=[]

for file in files:
    if 'ts' not in file:
        continue
    else: n_files.append(file)

#
# # importing shutil module
import shutil
for source in n_files:
    # Source file
    # source='file.txt'

    # Open the source file
    # in read mode and
    # get the file object
    fsrc=open(source,'r')

    # destination file
    dest='file_copy.mp4'

    # Open the destination file
    # in write mode and
    # get the file object
    fdst=open(dest,'w')

    # Now, copy the contents of
    # file object f1 to f2
    # using shutil.copyfileobj() method
    shutil.copyfileobj(fsrc,fdst,1024)

    # We can also specify
    # the buffer size by paasing
    # optional length parameter
    # like shutil.copyfileobj(fsrc, fdst, 1024)

    print("Contents of file object copied successfully")

    # Close file objects
    fsrc.close()
    fdst.close()
