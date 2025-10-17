try:
  age=int(input("enter your age :"))
  if age>=18:
    print("your eligible to vote")
  else:
    print("your not eligible to vote")
except valueError:
  print("please enter a valid integer")
