#Muna Bhattarai
#1001746212
#7/28/2023
#OS used = Linux

import os

#define a function to calculate the expression
def calculate_rpn(expression):
    #initialize stack to store operands
    stack = []
    #define the operators to use
    operators = set(['+', '-', '*', '/'])
    
    for token in expression.split():
        if token.isdigit(): # Check if the token is a digit (operand)
            stack.append(int(token))
        elif token in operators: # If not a digit, check if it is an operator
            # Perform the corresponding operation using the operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if token == '+':
                stack.append(operand1 + operand2)   # Integer addition to match the requirement of single-digit inputs
            elif token == '-':
                stack.append(operand1 - operand2)   # Integer subtraction to match the requirement of single-digit inputs
            elif token == '*':
                stack.append(operand1 * operand2)   # Integer multiplication to match the requirement of single-digit inputs
            elif token == '/':
                stack.append(operand1 // operand2)  # Integer division to match the requirement of single-digit inputs
    
    return stack[0]

#function to parse the file
def read_rpn_expressions_from_file(file_path):
    with open(file_path, 'r', newline='') as file:
        rpn_expressions = file.readlines()
    return [expr.strip() for expr in rpn_expressions]

def main():
    input_file_path = os.path.join(os.path.dirname(__file__), 'input_RPN.txt')
    rpn_expressions = read_rpn_expressions_from_file(input_file_path)
    
    for expr in rpn_expressions:
        result = calculate_rpn(expr)
        print(result)

if __name__ == "__main__":
    main()
