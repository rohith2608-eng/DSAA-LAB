def evaluate_postfix(postfix_expr):
    stack = []
    operators = set(['+','-','*','/','%','^'])
    for elem in postfix_expr:
        if elem not in operators:
            stack.append(float(elem))
        else:
            b=stack.pop()
            a=stack.pop()
            if elem =='+':
                stack.append(a+b)
            elif elem =='-':
                stack.append(a-b)
            elif elem =='*':
                stack.append(a*b)
            elif elem =='/':
                stack.append(a/b)
            elif elem =='%':
                stack.append(a%b)
            elif elem =='^':
                stack.append(a**b)
            return stack.pop()
postfix = '236*+'
evaluate_postfix(postfix)
print('{}\t: {}'.format(postfix,evaluate_postfix(postfix)))
postfix = '23*6+'
evaluate_postfix(postfix)
print('{}\t: {}'.format(postfix,evaluate_postfix(postfix)))
postfix = '23*42/+'
evaluate_postfix(postfix)
print('{}\t: {}'.format(postfix,evaluate_postfix(postfix)))
