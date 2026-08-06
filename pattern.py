<<<<<<< HEAD
row = int(input("enter by the user"))
print("1. Right triangle")
print("2. inverted triangle")
print("3. pyramid triangle")
print("4. square triangle")

choice = int(input("enter your choice: "))
if choice == 1:
    for i in range(1, row + 1):
        print("*"*i)

elif choice == 2:
    for i in range(row, 0, -1):
        print("*"*i)

elif choice == 3:
    for i in range(row):
        print(" "* (row - i - 1) + "*"* (2*i+1))

elif choice == 4:
    for i in range (1, row + 1):
        print("*"* row)

else:
=======
row = int(input("enter by the user"))
print("1. Right triangle")
print("2. inverted triangle")
print("3. pyramid triangle")
print("4. square triangle")

choice = int(input("enter your choice: "))
if choice == 1:
    for i in range(1, row + 1):
        print("*"*i)

elif choice == 2:
    for i in range(row, 0, -1):
        print("*"*i)

elif choice == 3:
    for i in range(1, row + 1):
        print(""*(row - i - 1)+"*"*(2*i+1))

elif choice == 4:
    for i in range (1, row + 1):
        print("*"* row)

else:
>>>>>>> fe93a3940dc5e255dabade7009f5ff67529871c8
    print("invalid choice")