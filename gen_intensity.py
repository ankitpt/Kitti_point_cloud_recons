import numpy as np
import matplotlib.pyplot as plt

text_file = open("samp1_10.txt", "r")
lines = text_file.readlines()

data=np.zeros([120000,7])

k=0

for line in lines:
    
    line=line.strip('\n').split(' ')
    line=[float(c) for c in line]
    data[k,:]=line
    k=k+1
    
data=data[0:k,:]

x_min=np.min(data[:,0])
x_max=np.max(data[:,0])

y_min=np.min(data[:,1])
y_max=np.max(data[:,1])

cell_siz=0.05

cols=int((x_max-x_min)/cell_siz)+1
rows=int((y_max-y_min)/cell_siz)+1

img=np.zeros([rows,cols])

for i in range(rows):
    
    for j in range(cols):
        
        
        xl=x_min+j*cell_siz
        yl=y_min+i*cell_siz
        ll=np.array([xl,yl])
        ur=np.array([xl+0.05,yl+0.05])
        
        inidx = np.all((ll <= data[:,0:2]) & (data[:,0:2] <= ur), axis=1)
        
        temp=data[inidx,:]
        
        if(len(temp)==0):
            continue
    
        else:
            print(len(temp))
            img[i,j]=np.mean(temp[:,5])*4
        
        
    