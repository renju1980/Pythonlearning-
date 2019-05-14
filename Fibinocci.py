# -*- coding: utf-8 -*-
"""
Spyder Editor

Code for finding fibicocii series 
"""

# change this value for a different result
n_terms = 5

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
First_num = 0
Second_num = 1
count = 0

# check if the number of terms is valid
if n_terms <= 0:
   print("Please enter a positive integer")
elif n_terms == 1:
   print("Fibonacci sequence upto",n_terms,":")
   print(First_num)
else:
   print("Fibonacci sequence upto",n_terms,":")
   while count < n_terms:
       print(First_num,end=' , ')
       nth = First_num + Second_num
       # update values
       First_num = Second_num
       Second_num = nth
       count += 1