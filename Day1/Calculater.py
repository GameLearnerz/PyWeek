# A Basic Calculator Module

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
    while True:

        n1=int(input("NUMBER 1:" ))
        if n1=="quit":
            break

        operation=input("(+,-,*,/)" )
        if operation=="quit":
            break

        n2=int(input("NUMBER 2: "))
        if n2=="quit":
            break

        if operation=='+':
            result=add(float(n1),float(n2))
        elif operation=='-':
            result=sub(float(n1),float(n2))
        elif operation=='*':
            result=mul(float(n1),float(n2))
        elif operation=='/':
            result=div(float(n1),float(n2))

        print("The Result Is: ", result)