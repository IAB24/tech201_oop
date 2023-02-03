def addition(int1, int2):
    return int1 + int2


def subtraction(int1, int2):
    return int1 - int2


def multiplication(int1, int2):
    return int1 * int2


def division(int1, int2):
    return int1 / int2


choice = int(input("Enter 1 for addition, 2 for subtraction, 3 for division, 4 for multiplication "))

int1 = int(input("Enter your first number "))
int2 = int(input("Enter your second number "))

if choice == 1:
    print(int1, "+", int2, "=", addition(int1, int2))
elif choice == 2:
    print(int1, "-", int2, "=", subtraction(int1, int2))
elif choice == 3:
    print(int1, "/", int2, "=", division(int1, int2))
elif choice == 4:
    print(int1, "*", int2, "=", multiplication(int1, int2))
else:
    print("Invalid output. Please try again")