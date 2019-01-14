def longestValidParentheses(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
            continue

        found = False
        idx = len(stack) - 1
        total = 0
        for j in reversed(range(len(stack))):
            if stack[j] == '(':
                found = True
                idx = j
                break
            if stack[j] == ')':
                break
            total += stack[j]
            
        if not found:
            stack.append(s[i])
            continue
        
        stack = stack[:idx]
        stack.append(total + 2)
    
    largest = 0
    temp = 0
    for i in range(len(stack)):
        if stack[i] != '(' and stack[i] != ')':
            temp += stack[i]
            continue
        largest = max(largest, temp)
        temp = 0

    return max(largest, temp)

print(longestValidParentheses("()()"))
