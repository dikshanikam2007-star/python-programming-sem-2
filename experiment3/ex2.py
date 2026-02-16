def simple_interest(principle,rate,time):
  si=(principle*rate*time)/100
  return si
p=float(input("Enter principle amount:"))
r=float(input("Enter rate of interest:"))
t=float(input("Enter time(in years):"))

interest=simple_interest(p,r,t)
print("Simple Interest is:",interest)





Enter principle amount:1000
Enter rate of interest:5
Enter time(in years):2
Simple Interest is: 100.0
