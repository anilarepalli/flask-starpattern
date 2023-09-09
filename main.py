# shape = input("Enter the * pattern :")
# triangle = 1

choice = input('''Enter your choice
               1.Triangle,
               2.Butterfly,
               3.Chocolate,
               4.for Square,
               5.for Right triangle,
               6.for Rectangle
               7.for Rhombus\n''')

choice = int(choice)

if choice == 1:
    n = int(input("Enter value"))
    for i in range(n):
        for j in range(i, n):
            print(end=' ')
        for j in range(i + 1):
            print('*', end=' ')
        print()

elif choice == 2:
    n = int(input("Enter value"))
    for i in range(n - 1):
        for j in range(i + 1):
            print('*', end=' ')
        for j in range(2 * i, n + 3):
            print(' ', end=' ')
        for j in range(i + 1):
            print('*', end=' ')
        print()
    for i in range(n):
        for j in range(i, n):
            print('*', end=' ')
        for j in range(i):
            print(' ', end=' ')
        for j in range(i):
            print(' ', end=' ')
        for j in range(i, n):
            print('*', end=' ')
        print()

elif choice == 3:
    n = int(input("Enter value"))
    for i in range(n - 1):
        for j in range(i + 1):
            print('*', end=' ')
        for j in range(i, n - 1):
            print(' ', end=' ')
        for j in range(i, n - 1):
            print(' ', end=' ')

        for j in range(i + 1):
            print('*', end=' ')
        for j in range(i):
            print('*', end=' ')
        for j in range(i, n - 1):
            print(' ', end=' ')
        for j in range(i, n - 1):
            print(' ', end=' ')
        for j in range(i + 1):
            print('*', end=' ')
        print()

    for i in range(n):
        for j in range(i, n):
            print('*', end=' ')
        for j in range(i):
            print(' ', end=' ')
        for j in range(i):
            print(' ', end=' ')
        for j in range(i, n - 1):
            print('*', end=' ')

        for j in range(i, n):
            print('*', end=' ')
        for j in range(i):
            print(' ', end=' ')
        for j in range(i):
            print(' ', end=' ')
        for j in range(i, n):
            print('*', end=' ')
        print()

elif choice == 4:
    n = int(input("Enter value"))
    for i in range(n):
        for j in range(n):
            print('*', end=' ')
        print()

elif choice == 5:
    n = int(input("Enter value"))
    for i in range(n):
        for j in range(i + 1):
            print('*', end=' ')
        print()

elif choice == 6:
    n = int(input("Enter value"))
    for i in range(n):
        for j in range(2 * n):
            print('*', end=' ')
        print()

elif choice == 7:
    n = int(input("Enter value"))
    for i in range(n - 1):
        for j in range(i, n - 1):
            print(end=' ')
        for j in range(i + 1):
            print('*', end=' ')
        print()
    for i in range(n):
        for j in range(i):
            print(end=' ')
        for j in range(i, n):
            print('*', end=' ')
        print()
else:
    print("Wrong Choice, terminating the program.")
