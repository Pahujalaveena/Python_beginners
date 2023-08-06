# Calculator
num1=input("Enter the first number: ")
op=input("Enter the operator (+,-,*,/,%): ")
num2=input("Enter the second number: ")

if(op=="+"):
    sum=int(num1)+int(num2)
    print("Addition:"+str(sum))
if(op=="-"):
    diff=int(num1)-int(num2)
    print("Subtraction:"+str(diff))
if(op=="*"):
    mul=int(num1)*int(num2)
    print("Multiplition:"+str(mul))
if(op=="/"):
    div=int(num1)/int(num2)
    print("Division:"+str(div))
if(op=="%"):
    rem=int(num1)%int(num2)
    print("Remainder:"+str(rem))
