copies=int(input("Enter number of receipt copies:"))
items=int(input("Enter number of items in each receipt:"))
for copy in range(1,copies + 1):
  print("\nReceipt Copy:",copy)
  print("--------------------")

  for item in range(1, items + 1):
    print("Item Number:",item)

  print("--------------------")  
print("\nALL receipts printed successfully!")  


Enter number of receipt copies:3
Enter number of items in each receipt:5

Receipt Copy: 1
--------------------
Item Number: 1
Item Number: 2
Item Number: 3
Item Number: 4
Item Number: 5
--------------------

Receipt Copy: 2
--------------------
Item Number: 1
Item Number: 2
Item Number: 3
Item Number: 4
Item Number: 5
--------------------

Receipt Copy: 3
--------------------
Item Number: 1
Item Number: 2
Item Number: 3
Item Number: 4
Item Number: 5
--------------------

ALL receipts printed successfully!
