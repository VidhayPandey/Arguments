def cube(num):
    return num * num * num

def by_3(num):
    if num%3==0:
        print(f"Cube of {num}")
        return cube(num)
    else:
        return "Not Divisble by 3."
    
number=int(input("Enter a number: "))
print(by_3(number))
    
