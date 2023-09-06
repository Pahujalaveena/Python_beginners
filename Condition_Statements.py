
# Conditional Statements
marks=90
if(marks>=90):
    print("Ist division")
    print("Congratulations")
elif(marks>=60 and marks<90):
    print("2nd division")
    print("Keep it Up!!")
else:
    print("3rd Division")



##

x=int(input("Enter your marks"))
if(x>90 and x<=100):
    print("Grade A")
elif(x>80 and x<=90):
    print("Grade B")
elif(x>70 and x<=80):
    print("Grade C")
elif(x>60 and x<=70):
    print("Grade D")
else:
    print("Grade E")
    


##
#single line if else with positive and negative number
x=int(input("Enter a number"))
print("Positve number") if x>0 else print("Negative number")



