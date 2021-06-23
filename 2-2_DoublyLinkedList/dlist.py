class DList:
    class Node:                                         # Node Class 생성
        def __init__(self, item, prev, link):           # Node 생성자
            self.item = item                            # 해당 Node item
            self.prev = prev                            # 해당 Node 앞 reference
            self.next = link                            # 해당 Node 뒤 reference
    
    def __init__(self):                                 # 이중연결리스트 생성자
        self.head = self.Node(None, None, None)         # head -> dummy1
        self.tail = self.Node(None, self.head, None)    # dummy1 <- dummy2 <- tail
        self.head.next = self.tail                      # head -> dummy1 <=> dummy2 <- tail
        self.size = 0                                   # size 초기화

    # size
    def size(self): return self.size

    # is_empty
    def is_empty(self): return self.size == 0

    # insert_before
    def insert_before(self, p, item):
        t = p.prev                                      # t <- p
        n = self.Node(item, t, p)                       # 새 노드 생성 후 n이 참조  t <- n -> p
        p.prev = n                                      # n <=> p
        t.next = n                                      # t <=> n
        self.size += 1                                  # DList의 size 1 증가 

    # insert_after
    def insert_after(self, p, item):
        t = p.next                                      # p -> t
        n = self.Node(item, p, t)                       # 새 노드 생성 후 n이 참조 p <- n -> t
        t.prev = n                                      # n <=> t
        p.next = n                                      # p <=> n
        self.size += 1                                  # DList의 size 1 증가

    # delete
    def delete(self, x):
        f = x.prev                                      # f <- x
        r = x.next                                      # x -> r
        f.next = r                                      # f -> r
        r.prev = f                                  # f <=> r
        self.size -= 1
        return x.item

    # print
    def print_list(self):
        if self.is_empty():
            print("리스트 비어있음")
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end = '')
                else:
                    print(p.item)
                p = p.next

class EmptyError(Exception):                            # Underflow시 예외 처리
    pass
