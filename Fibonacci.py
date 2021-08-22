#This program returns the Fibonacci number by using Recursion

def fibonacci(num, num1=0, num2=1):
    if num1 == 0:
        return num1
    if num2 == 1:
        return num2

    return fibonacci(num -1,num2,num1+num2);


def main():
    n = int(input("Enter a number to find its fibonacci number: "))
    result = fibonacci(n)
    print(result)

main()
