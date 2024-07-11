def calculater():
    print('\n')
    print("List of Operations..")
    print('\n')
    print("1.Addition..")
    print("2.Subtraction..")
    print("3.Multiplication..")
    print("4.Division..")

    user_choice=input("Choose operations..(1/2/3/4) : ")

    if user_choice not in ['1','2','3','4']:
        print("INVALID OPERATION...Please Try Again..!!")
        return
    
    try:
        a=int(input("Enter you're first number:-> "))
        b=int(input("Enter you're second number:-> "))
    except ValueError:
        print("INVALID..INPUT..Please Enter NUMERIC VALUE..")

    if user_choice=='1':
        print(f"The addition between {a} and {b} is-->{a+b} ")

    if user_choice=='2':
        print(f"The subtraction between {a} and {b} is-->{a-b} ")

    if user_choice=='3':
        print(f"The multiplication between {a} and {b} is-->{a*b} ")

    if user_choice=='4':
        try:
            mul=a/b
            print(f"The multiplication between {a} and {b} is-->{mul} ")
        except ZeroDivisionError:
            print("INVALID INPUT..The DENOMINATOR Should NOT Be ZERO..")

calculater()