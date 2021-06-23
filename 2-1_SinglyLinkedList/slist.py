class SList:
    class Node:                                     # Node Class 생성
        def __init__(self, item, link):             # Node 생성자
            self.item = item                        # 해당 Node item
            self.next = link                        # 다음 Node reference

    def __init__(self):                             # 단순연결리스트  생성자
        self.head = None                            # head 생성 후 초기화
        self.size = 0                               # 항목 수(size) 생성 후 초기화


    # size
    def size(self): return self.size                # return size

    # is_empty
    def is_empty(self): return self.size == 0       # size가 0이면 return true(1), 아니면 return false(0)

    # insert_front : 맨 앞(head 다음)에 삽입
    def insert_front(self, item):
        if self.is_empty():                         # true면 (비어있으면)
            self.head = self.Node(item, None)       # head가 참조하는 곳에 아무 것도 참조하지 않는 Node 생성
        else:                                       # false면 (비어있지 않으면)
            self.head = self.Node(item, self.head)  # head가 참조하는 Node 생성 후 head가 참조하던 Node를 참조하는 Node생성
        self.size += 1                              # SList의 size 1증가
       
    # insert_after : 특정 Node(p)의 next에 삽입
    def insert_after(self, item, p):
        p.next = SList.Node(item, None)             # p의 next가 가르키고 있는 곳에 아무 것도 가르키지 않는 Node 생성
        self.size += 1                              # SList의 size 1 증가
    
    # delete_front : 맨 앞(head 다음) 삭제 
    def delete_front(self):
        if self.is_empty():                         # true면 (비어있으면)
            raise EmptyError("Underflow")           # Underflow 에러 처리
        else:                                       # false면 (비어있지 않으면)
            self.head = self.head.next              # head가 두번 째 Node 참조
            self.size += 1                          # SList의 size 1 증가
            
    # delete_after : 특정 Node(prev) 삭제
    def delete_after(self, p):
        if self.is_empty():                         # ture면 (비어있으면)
            raise EmptyError("Underflow")           # Underflow 에러 처리
        temp = p.next                               # temp 변수 생성 후 p.next 할당
        p.next = temp.next                          # p가 참조하는 곳에 temp(p가 참조하는 것)가 참조하는 것 할당
        self.size -= 1                              # SList의 size 1 감소

    # search : SList 내 모든 Node 출력
    def search(self, target):
       p = self.head                                # head로부터 순차 탐색                    
       for i in range(self.size):
           if target == p.item: return i            # 찾으면 return i
           p = p.next                               # 비교 대상을 p에서 p의 next로 이동
       return None                                  # 탐색 실패

    # print
    def print_list(self):
        p = self.head                               # head로부터 순차 탐색
        while p:
            if p.next != None:                      # 마지막 원소일 때
                print(p.item, ' -> ', end = '')
            else:
                print(p.item)                       # 마지막 원소가 아닐 때
            p = p.next                              # p에서 p의 next로 이동



class EmptyError(Exception):                        #Underflow시 에러 처리
    pass
