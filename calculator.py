
x = float(input("Enter any number:"))
z= input("Type What you want to do (+,-,*,/,%)")
y= float(input("Enter 2nd number:"))
# x= float(a)
# y=float(b)

if z == '+':
    result=x+y
    print("Answer is " ,result )
elif z== '-':
        result=x-y
        print("Answer is " ,  result )
elif z == '*':
          result=x*y
          print("Answer is " ,result  )
elif z== '%':
        result=x%y
        print("Answer is " ,result  )
elif z == '/':
          result=x/y
          print("Answer is " ,result )
else:
     print("Invalid Syntax")
    
        