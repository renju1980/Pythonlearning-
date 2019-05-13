# -*- coding: utf-8 -*-
"""
Created on Mon May 13 22:54:02 2019

@author: User PC
"""
#Fibonacci series
print("Fibonacci series\n***************")
a=0
b=1
limit =int(input("Enter the limit:"))
print("Series:\n",a,',',b,end=", ")
 
for i in range(2,limit):
        sum=a+b
        print(sum, end=", ")
        #swap
        a=b
        b=sum
    