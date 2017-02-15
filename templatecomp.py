import cv2
import numpy as np
import sys

def add(one,two):
    three=one+two
    return three

def sub(one,two):
    three=one-two
    return three

def xchange(one,p):
    grid_line_x = 7
    grid_line_y = 7
    m=600/(grid_line_x-1)
    n=600/(grid_line_y-1)
    if(p>0 and p<10):
        val=one-m/4
    else:
        val=one-m/2

        
    return val


def ychange(one):
    grid_line_x = 7
    grid_line_y = 7
    m=600/(grid_line_x-1)
    n=600/(grid_line_y-1)
    val=one+n/4
    return val       

grid_line_x = 7
grid_line_y = 7
m=600/(grid_line_x-1)
n=600/(grid_line_y-1)
grid_map = [ [ 0 for i in range(grid_line_y-1) ] for j in range(grid_line_x-1) ]
r=grid_map

img_org=cv2.imread('task1sets/task1_img_6.jpg')
img_gray=cv2.cvtColor(img_org, cv2.COLOR_BGR2GRAY)


#search for 0
temp=cv2.imread('digits/0.jpg',0)
w,h = temp.shape[::-1]
res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.68
loc = np.where(res >= threshold)
(x,y)=loc
for i in range(len(x)):
    r[int(x[i]/100)][int(y[i]/100)]=0

#search for 1
temp=cv2.imread('digits/1.jpg',0)
w,h = temp.shape[::-1]
res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.55
loc = np.where(res >= threshold)
(x,y)=loc
for i in range(len(x)):
    r[int(x[i]/100)][int(y[i]/100)]=1

#search for 2
temp=cv2.imread('digits/2.jpg',0)
w,h = temp.shape[::-1]
res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.65
loc = np.where(res >= threshold)
(x,y)=loc
for i in range(len(x)):
    r[int(x[i]/100)][int(y[i]/100)]=2

#search for 3
temp=cv2.imread('digits/3.jpg',0)
w,h = temp.shape[::-1]
res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.65
loc = np.where(res >= threshold)
(x,y)=loc
for i in range(len(x)):
    r[int(x[i]/100)][int(y[i]/100)]=3

#search for 4
temp=cv2.imread('digits/4.jpg',0)
w,h = temp.shape[::-1]
res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.65
loc = np.where(res >= threshold)
(x,y)=loc
for i in range(len(x)):
    r[int(x[i]/100)][int(y[i]/100)]=4

#search for 5
temp=cv2.imread('digits/5.jpg',0)
w,h = temp.shape[::-1]
res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.65
loc = np.where(res >= threshold)
(x,y)=loc
for i in range(len(x)):
    r[int(x[i]/100)][int(y[i]/100)]=5

#search for 6
temp=cv2.imread('digits/6.jpg',0)
w,h = temp.shape[::-1]
res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.65
loc = np.where(res >= threshold)
(x,y)=loc
for i in range(len(x)):
    r[int(x[i]/100)][int(y[i]/100)]=6

#search for 7
temp=cv2.imread('digits/7.jpg',0)
w,h = temp.shape[::-1]
res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.61
loc = np.where(res >= threshold)
(x,y)=loc
for i in range(len(x)):
    r[int(x[i]/100)][int(y[i]/100)]=7

#search for 8
temp=cv2.imread('digits/8.jpg',0)
w,h = temp.shape[::-1]
res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.72
loc = np.where(res >= threshold)
(x,y)=loc
for i in range(len(x)):
    r[int(x[i]/100)][int(y[i]/100)]=8

#search for 9
temp=cv2.imread('digits/9.jpg',0)
w,h = temp.shape[::-1]
res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.70
loc = np.where(res >= threshold)
(x,y)=loc
for i in range(len(x)):
    r[int(x[i]/100)][int(y[i]/100)]=9

#search for plus
temp=cv2.imread('digits/plus.jpg',0)
w,h = temp.shape[::-1]
res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.65
loc = np.where(res >= threshold)
(x,y)=loc
for i in range(len(x)):
    r[int(x[i]/100)][int(y[i]/100)]='+'

#search for minus
temp=cv2.imread('digits/minus.jpg',0)
w,h = temp.shape[::-1]
res=cv2.matchTemplate(img_gray,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.53
loc = np.where(res >= threshold)
(x,y)=loc
for i in range(len(x)):
    r[int(x[i]/100)][int(y[i]/100)]='-'


for i in range(len(r)):
    if(r[i][1]=='+'):
        p=add(r[i][0],r[i][2])
    else:
        p=sub(r[i][0],r[i][2])

    if(r[i][3]=='+'):
        r[i][5]=add(p,r[i][4])
    else:
        r[i][5]=sub(p,r[i][4])

    

for i in range(len(r)):
    for j in range(len(r)):
        sys.stdout.write(str(r[i][j]))
    sys.stdout.write('\n')

grid_map=r



for i in range(len(r)):
    x=550
    y=50+100*i
    m,n=(xchange(x,r[i][5]), ychange(y))
    cv2.putText(img_org, str(r[i][5]), (m,n),cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 4)


cv2.imshow('output',img_org)
cv2.waitKey()
