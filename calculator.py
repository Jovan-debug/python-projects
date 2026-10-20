
operation=["+","-","*","/","q"]


def calculate(num1:float,num2:float,operator:str):
    if operator == "+":
          return num1 + num2
    elif operator == "-":
               return num1 - num2
    elif operator == "*":
                    return num1 * num2
    elif operator == "/":
                    if num2==0:
                        raise ZeroDivisionError("cannot divide by zero")
                    return num1 / num2
    raise ValueError("Invalid operation") #in case one operator isn't among the list of operator

def getnum(prompt:str):
       while True:
              try:
                     return float(input(prompt))
              except ValueError:print("Enter a value digit")


def main():
    print("****Welcome to the calculator app****")
    while True:
        choice=input("Choose an operation to perform (+,-,*,/) or press q to quit:")
        
        if choice not in operation :
                print("enter a valid operation as above")
                continue
        if choice=="q": 
                   print("GOOD BYE Thank you ")
                   break
        num1=getnum("Enter the 1st number:")
        num2=getnum("Enter the 2st number:")
        try:
                result=calculate(num1,num2,choice)
                print(f"result={result}")

        except ZeroDivisionError:
            print("cannot divide a number by 0")

main()