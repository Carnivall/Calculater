print("1 addition")
print("2 subtraction")
print("3 multilicatoin")
print("4 division")
print("5 square")
print("6 square root")
print("7 root")


choice = input("enter your choice : ")

num1=float(input("enter 1 :"))
num2=float(input("enter number 2 :"))

if choice== "1" :
    print(num1,"+",num2,"=",(num1+num2))
elif choice=="2":
      print(num2,"-",num2,"=",(num1-num2))
elif choice=="3":
    print(num1,"*",num2,"=",(num1*num2))
elif choice=="4" :
    if num2==0.0:
        print("divide by 0 error")
    else:
        print(num1,"/",num2,"=",(num1/num2))
elif choice=="5":
     print(num1,"*",num1,"=",(num1*num1))
elif choice=="6":
    import math
    print(math.pow(num1,0.5))
elif choice=="7":
    num3=float(input("enter degree for root:"))
    import math
    print(math.pow(num1,1/num3))