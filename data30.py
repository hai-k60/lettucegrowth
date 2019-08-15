#Create dataset 30 day
import numpy as np 
import math
import random
ah={}
file1 = open('data30fix.txt','w+')
file2 = open('dataset.txt','w+')

mt=np.linspace(18,30,100)
for i in mt:
    s=0.125*math.exp(0.283*(i+1))
    s=round(s,5)
    ah[i]=s
    h=s/1.5189
    h=h+h*5*np.random.rand()/100
    h=round(h,5)
    rand=5*np.random.rand()/100
    w=0.002*math.exp(0.340*(i+1))
    #w=w+rand*w
    w=round(w,5)
    file1.write(str(s))
    file1.write(' ')
    file1.write(str(h)+'\n')

    file2.write(str(s))
    file2.write(' ')

    file2.write(str(h))
    file2.write(' ')

    file2.write(str(w)+'\n')
file1.close
file2.close
print(ah)

# for i in range(29):
#     f=(ah[i+1]-ah[i])/ah[i]*100
#     f=round(f,2)
#     file2.write(str(f)+'\n')
#     print(f)
# file2.close