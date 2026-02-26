def evaluate_postfix(postfix_expr):
    stack = []
    operators = set(['+', '-', '*', '/', '%', '^'])

    for elem in postfix_expr:
        if elem not in operators:
            stack.append(float(elem))
        else:
            b = stack.pop()
            a = stack.pop()

            if elem == '+':
                stack.append(a + b)
            elif elem == '-':
                stack.append(a - b)
            elif elem == '*':
                stack.append(a * b)
            elif elem == '/':
                stack.append(a / b)
            elif elem == '%':
                stack.append(a % b)
            elif elem == '^':
                stack.append(a ** b)

    return stack.pop()


# Driver Code
postfix = "236*+"
print(postfix, ":", evaluate_postfix(postfix))

postfix = "23*6+"
print(postfix, ":", evaluate_postfix(postfix))

postfix = "23*42/+"
print(postfix, ":", evaluate_postfix(postfix))
