def logic(choice, value):
    result = ''
    if choice == 1:
        n = int(value)
        for i in range(n):
            for j in range(i, n):
                result = result + "\n"
            for j in range(i + 1):
                result = result + "*"
            result = result + "\n"

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
    return result
