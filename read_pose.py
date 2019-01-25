import numpy as np
import os

#os.mkdir("Seq_00_txt_r2")

pose=open("00seq_pose.txt",'r')
lines=pose.readlines()


os.chdir("//nas01.itap.purdue.edu/puhome/pu.data/desktop/Kitti_work/Test_3")

directory = os.fsencode("//nas01.itap.purdue.edu/puhome/pu.data/desktop/Kitti_work/Test_3")


k=0

for file in os.listdir(directory):
    
    line=lines[k]
    line=line.strip("\n")
    line=line.split(" ")
    line=[float(c) for c in line]
    Rr=np.reshape(line,[3,4])
    R_camt_to_cam=Rr[0:3,0:3]
    r_camt_to_cam=Rr[0:3,3]
    
    filename = os.fsdecode(file)
    txt=open(filename,'r')
    pts=txt.readlines()
    txt.close()
    
    os.chdir("//nas01.itap.purdue.edu/puhome/pu.data/desktop/Kitti_work/Seq_00_txt_r2")
    nfilename=filename.replace(".bin","")+'r'+".txt"
    txtr=open(nfilename,'w')
    
    print(filename)
    for pti in pts:
        
        pti=pti.strip("\n")
        pti=pti.split(" ")
        pti=[float(c) for c in pti]
        
        
        
        
        pt=pti[0:3]
        
        
        npt=np.empty([3, 1])
        
        npt[0]=-pt[1]
        npt[1]=-pt[2]
        npt[2]=pt[0]
        
        pt_m=np.matmul(R_camt_to_cam,npt)+np.reshape(r_camt_to_cam,[3,1])
        npt_m=np.empty([4, 1])
        npt_m[0]=pt_m[2]
        npt_m[1]=-pt_m[0]
        npt_m[2]=-pt_m[1]
        npt_m[3]=pti[3]
        npt_m=np.reshape(npt_m,[1,4])
        np.savetxt(txtr,npt_m,fmt='%.4f')
    
    txtr.close()
    k=k+1
    os.chdir("//nas01.itap.purdue.edu/puhome/pu.data/desktop/Kitti_work/Test_3")
    
    
    

