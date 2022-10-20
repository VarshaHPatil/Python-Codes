# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 16:03:54 2019

@author: Varsha
"""


N=int(input())
Array=[0]*N
j=0
Array=[[int (j) for j in input().split()] for i in  range(N)]
# Initiate four turning corners of matrix
LeftTop=0
LeftBottom=N-1
RightBottom=N-1
RightTop=0
#check whether matrix size is even or odd 
even=0
if(N%2==0):
    even=1

# print matrix counter spiral
while(1):
    i=0
    for i in range(LeftTop,LeftBottom+1,1):
        print(Array[i][LeftTop], end=" ")
   
    if(even!=1):
        if(LeftBottom==RightTop):  #end conditions
            break
   
    i=0
    for i in range(LeftTop+1,RightBottom+1,1):
        print(Array[LeftBottom][i], end=" ")
     
    LeftBottom-=1
   
    i=0
    for i in range(LeftBottom,RightTop-1,-1):
        print(Array[i][RightBottom], end=" ")
     
    RightBottom-=1
    RightTop+=1
    i=0
    if(even==1):
        if(RightTop==RightBottom+1):   #end conditions
            break
    for i in range(RightBottom,LeftTop,-1):
        print(Array[LeftTop][i], end=" ")
    LeftTop+=1