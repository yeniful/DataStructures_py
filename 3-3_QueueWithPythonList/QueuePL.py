def add(item):      # 삽입 연산
    q.append(item)

def remove():       # 삭제 연산
    if len(q) != 0:
        item = q.pop(0)
        return item

def print_q():      # 큐 출력
    print('front -> ', end = '')
    for i in range(len(q)):
        print('{!s:<8}'.format(q[i]), end = '')
    print(' <- rear')


q = []              # 리스트 선언
add('apple')        # 'apple'
add('orange')       # 'apple, orange'
add('cherry')       # 'apple, orange, cherry'
add('pear')         # 'apple, orange, cherry, pear'
print('사과, 오렌지, 체리, 배 삽입 후: \t', end = '')
print_q()
remove()
print('remove한 후: \t\t', end = '')
print_q()
