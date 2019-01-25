import numpy as np
import struct
import os

os.chdir("//nas01.itap.purdue.edu/puhome/pu.data/desktop/Kitti_work")
os.mkdir("Seq_00_txt_22")
os.chdir("//nas01.itap.purdue.edu/puhome/pu.data/desktop/Kitti_work/Seq_00_bin")

directory = os.fsencode("//nas01.itap.purdue.edu/puhome/pu.data/desktop/Kitti_work/Seq_00_bin")


for file in os.listdir(directory):
    
    filename = os.fsdecode(file)


    with open(filename, mode='rb') as file: # b is important -> binary
       fileContent = file.read()

    siz=len(fileContent)
    
    os.chdir("//nas01.itap.purdue.edu/puhome/pu.data/desktop/Kitti_work/Seq_00_txt_22")
    nfilename=filename.replace(".txt","")+".txt"
    txtb=open(nfilename,'w')

    print(filename)
    for i in range(int(siz/16)):
    
    
      temp = struct.unpack("ffff",fileContent[16*i:16*(i+1)])
      temp=np.array(temp)
    
      np.savetxt(txtb,[temp],fmt='%.4f')

    txtb.close()
    os.chdir("//nas01.itap.purdue.edu/puhome/pu.data/desktop/Kitti_work/Seq_00_bin")