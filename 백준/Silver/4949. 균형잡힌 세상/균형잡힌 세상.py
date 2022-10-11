while True:
    String = list(input())
    stack = []
    if String == ['.']:
        break
    for i in String:
        if i == '(':
            stack.append(i)
        elif i == '[':
            stack.append(i)
        elif i == ')':
            if stack:
                if stack.pop() == '(':
                    pass
                else:
                    print('no')
                    break
            else:
                print('no')
                break
        elif i == ']':
            if stack:
                if stack.pop() == '[':
                    pass
                else:
                    print('no')
                    break
            else:
                print('no')
                break
    else:
        if not stack:
            print('yes')
        else:
            print('no')
