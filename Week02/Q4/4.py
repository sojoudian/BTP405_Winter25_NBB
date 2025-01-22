def processNumberDecorator(func):
    def wrapper(numbers):
        print(f"Numbers: {numbers}")
        print(f"Count of Numbers: {len(numbers)}")
        print(f"Sum of Numbers: {sum(numbers)}")
        return func(numbers)
    return wrapper

@processNumberDecorator
def processNumber(numbers):
    print("Processing the numbers... ")
        


numberList = [10, 20, 30, 40, 50]
processNumber(numberList)