
num1 = int(input ("Enter a Number:"))
Operand = input ("Enter an Operand (+,-,/,*)")
num2 = int(input ("Enter a Number:"))
if Operand == '+' :
    print ("Ans=",num1 + num2)
elif Operand == '-' :
    print ("Ans=",num1 - num2)
elif Operand == '/':
    print ("Ans=",num1 / num2)
elif Operand == '*':
    print ("Ans=",num1 * num2)
else: print ("Wrong Operand")