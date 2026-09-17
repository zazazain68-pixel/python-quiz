print("calculator")
while True:
  first=float(input("enter the number"))
  second=float(input("enter the other number"))
  operation=input("choose an operation ( +,-,*,/)")
  if operation=="+":
    print(first+second)
  elif operation=="-":
    print(first-second)
  elif operation=="*":
    print(first*second)
  elif operation=="/":
    if second==0:
      print("cannot devide by zero")
    else:
      print("first/second")
  else:
    print("error")
  again=input("do you want to calculate again? yes or no")
  if again.lower()=="no":
    print("bye")
    break
