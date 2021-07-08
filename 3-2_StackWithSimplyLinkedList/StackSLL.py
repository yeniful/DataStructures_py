class Node:                         # Node 클래스
    def __init__(self, item, link): # Node 생성자
        self.item = item
        self.next = link

def push(item):                 # 삽입
    global top
    global size
    top = Node(item, top)       # 새 노드 객체를 생성하여 연결리스트의 첫 노드로 삽입
    size += 1

def peek():
    if size != 0:
        return top.item

def pop():                          # 삭제 연산
    global top
    global size
    if size != 0:
        top_item = top.item
        top = top.next              # 연결리스트에서 top이 참조하던 노드 분리
        size -= 1
        return top_item

def print_stack():                  # stack 출력
    print('top -> \t', end='')
    p = top
    while p:
        if p.next != None:
            print(p.item, " -> ", end='')
        else:
            print(p.item, end='')
        p = p.next
    print()


# 초기화
top = None
size = 0

push('apple')
push('orange')
push('cherry')
print("사과, 오렌지, 체리 push 후:\t", end='')
print_stack()
print("top 항목 : ", end='')
print(peek())
push('pear')
print("배 push 후:\t\t", end='')
print_stack()
pop()
push('grape')
print("pop(), 포도 push 후:\t", end='')
print_stack()
