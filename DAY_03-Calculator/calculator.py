def operation(a,b,symbol):
    if symbol == 1:
        print(f"{a} + {b}= {a+b}")
    elif symbol == 2:
        print(f"{a} - {b} ={a - b}")
    elif symbol == 3:
        print(f"{a} X {b} = {a * b}")
    elif symbol == 4:
            if b==0:
                print("cannot br divided")
                   
            else:
                print(f"{a} ÷ {b} = {a /b}")
                   
    else:
        print("Invalid Output")


value1 =int(input("Enter the Value of a :"))
value2 =int(input("Enter the Value of b :"))
print("****Enter Your Choice****")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
while True:
    try:
        sign = int(input("Enter the choice :"))
        if 1 <= sign <= 4:
            break  # valid input, exit the loop
        else:
            print("Invalid input X options(1 - 4)")
    except:
         print("Enter Valid option")
          
operation(value1,value2,sign)