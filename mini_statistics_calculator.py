print("Statistics Calculator")
while True:
  numbers=[ ]
  while True:
    value=input("enter the number  and to quit type letter q")
    if value.lower()=="q":
      break
      number =float(value)
      numbers.append(number)
      mean=sum(numbers)/len(numbers)
      middle=len(numbers)//2
      median=numbers[middle]
      range_value=max(numbers)-min(numbers)
      mode=max(numbers,key=numbers.count)
      operation=input("choose an operation : mean, median, range, mode")
      if operation.lower()=="mean":
        print("Mean:",mean)
      elif operation.lower()=="median":
        print ("Median:",median)
      elif operation.lower()=="range":
        print("Range:",range_value)
      elif operation.lower()=="mode":
        print("Mode",mode)
      else:
        print("error")
        again=input("do you want to calculate again? yes or no ")
        if again.lower()=="no":
          break
