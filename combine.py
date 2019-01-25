import glob
import os
os.chdir('//nas01.itap.purdue.edu/puhome/pu.data/desktop/Kitti_work/Seq_00_txt_r2')
read_files = glob.glob("*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())