import pyliststack as stack


print('Postfix Expression Evaluator')
print('For help, type \"help\" or \"?\"')
print('To quit, type \"quit\" or \"q\"')

while True:
    expression = input("\nEnter a Postfix expression to be evaluated: ")
    tokens = expression.split(" ") # Split the expression into individual tokens
    # separated by space
    myStack = stack.Stack() # Create an instance of the Stack object
    # Handle help option


    if tokens[0] == "help" or tokens[0] == "?":
        print('Postfix Expression Evaluator takes in a mathematical expression expressed in Postfix notation and evaluates it.')
        print('Example: \"1 2 + 4 *\" will evaluate to \"12\"')
        # Handle quit option
    elif tokens[0] == "quit" or tokens[0] == "q":
        break
    # Handle Postfix expression entered
    else:
        valid = True
        while len(tokens) > 0:
            # Remove first token from the expression
            item = tokens.pop(0)
            # Handle operand
            if item.isdigit():
                myStack.push(int(item))
                # Handle "+" operator
            elif item == "+":
                if len(myStack) > 1:
                    myStack.push(myStack.pop() + myStack.pop())
                else:
                    valid = False
                    break
                # Handle "-" operator
            elif item == "-":
                if len(myStack) > 1:
                    temp = myStack.pop()
                    myStack.push(myStack.pop() - temp)
                else:
                    valid = False
                    break
                # Handle "*" operator
            elif item == "*":
                if len(myStack) > 1:
                    myStack.push(myStack.pop() * myStack.pop())
                else:
                    valid = False
                    break
                # Handle "/" operator
            elif item == "/":
                if len(myStack) > 1:
                    temp = myStack.pop()
                    myStack.push(myStack.pop() / temp)
                else:
                    valid = False
                    break
                # Handle "^" operator
            elif item == "^":
                if len(myStack) > 1:
                    temp = myStack.pop()
                    myStack.push(pow(myStack.pop(),temp))
            # Any other characters are invalid
            else:
                valid = False
                break
    # For valid expression, there should only be one item left in the stack
        if len(myStack) != 1:
            valid = False
        # If expression is valid, print evaluation result
        # else print error message
        if valid:
            print('Evaluation Result: ', myStack.pop())
        else:
            print('Invalid Postfix expression!')