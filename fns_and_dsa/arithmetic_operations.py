print("Arithmetic Operations")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

def perform_operation(num1, num2, operation):
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2 
        if num2 == 0:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: unknown operation."
        
result = perform_operation(num1, num2, operation)
print(f"Result: {result}")