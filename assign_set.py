roll_no = input("enter roll number")

if int(roll_no) in range(1, 1000, 4):
    b = list(range(1, 1000, 4))
    print("you are in set A")

elif int(roll_no) in range(2, 1000, 4):
    print("you are in set B")

elif int(roll_no) in range(3, 1000, 4):
    print("you are in set C")

elif int(roll_no) in range(4, 1000, 4):
    print("you are in set D")

else:
    print("Invalid Roll number")
