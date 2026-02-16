rows = int(input("Enter number of rows:"))
seats_per_row = int(input("Enter number of seats in each row:"))

for row in range(1,rows + 1):
  print("Row",row, ":", end=" ")

  for seat in range(1, seats_per_row + 1):
    print(f"S{seat}",end=" ")
  print()  


Enter number of rows:5
Enter number of seats in each row:10
Row 1 : S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 
Row 2 : S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 
Row 3 : S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 
Row 4 : S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 
Row 5 : S1 S2 S3 S4 S5 S6 S7 S8 S9 S10 
