def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    
num=int(input("Please enter a number: "))
print(f"The Factorial of {num} is {factorial(num)}")