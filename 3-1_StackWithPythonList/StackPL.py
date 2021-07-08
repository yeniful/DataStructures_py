def push(item):                 # 삽입
    stack.append(item)

def peek():                     # top 항목 접근
    if (len(stack) != 0):
            return stack[-1]    # 리스트의 마지막 항목 리턴

def pop():                      # 삭제 연산
    if (len(stack) != 0):
        item = stack.pop(-1)    # 리스트의 마지막 항목 제거
        return item             # 제거한 항목 리턴


stack = []
push('apple')
push('orange')
push('cherry')
print("사과, 오렌지, 체리 push 후:\t", end='')
print(stack, "\t <- top")
print("top 항목 :\t", end='')
print(peek())
push('pear')
print("배 push 후:\t", end='')
print(stack, "\t <- top")
pop()
push('grape')
print("pop(), 포도 push 후:\t", end='')
print(stack, "\t <- top")
