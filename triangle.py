def triangle(x):
    x_mod = x*2
    for i in range(x_mod):
            print('\n')
            for y in range(x_mod):
                if (i + y == x or y-i == x) and y != 0:
                    print("*", end=" ")
                elif i == x - 1 and y != 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")


height = int(input("Enter Height: "))
triangle(height)
