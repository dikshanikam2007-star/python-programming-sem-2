#simple interest using a function with parameters for principal,rate,and time
"""
Created on Mon Mar 16 15:08:34 2026
@author: DIKSHA
"""

def simple_interest(principle,rate,time):
  si=(principle*rate*time)/100
  return si
p=float(input("Enter principle amount:"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter time(in years):"))

interest=simple_interest(p,r,t)
print("Simple Interest is:",interest)
