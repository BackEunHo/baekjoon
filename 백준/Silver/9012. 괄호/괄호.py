import sys

t = int(sys.stdin.readline())
for _ in range(t):
    arr= []
    ps = list(sys.stdin.readline().strip())
    if len(ps) % 2 !=0: #입력받은 문자열의 길이가 짝수 아닐 시 
        print("NO")
        continue
    else: #ps의 길이가 짝수
        if ps[0] == ')' or ps[-1] == '(':
            print("NO")
            continue
        else:
            for i in ps:
                if i == '(':
                    arr.append(i)
                elif i == ')':
                    if arr: 
                        arr.pop()
                    else: # 스택에 괄호가 없을시
                        print('NO')
                        break
            else:
                if not arr:
                    print("YES")
                else:
                    print('NO')
        
                
            