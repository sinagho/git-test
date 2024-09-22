
user_input = int(input("Enter the number"))

if user_input % 2 == 0:
    print("Zoj")
elif user_input % 5 == 0:
    print("Taqsim bar 5")
    for i in range(1,4):
        print(i)
else:
    print("False")

print("end")

print("the code is ended.")

def addition(x, y):
    return x + y

def area(x, y = 5):
    return x + (y ** 3)

def subtraction(x, y):
    return x - y

print("*" * 40)