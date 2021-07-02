class Clist:
    class _Node:
        def __init__(self, item, link):
            self.item = item
            self.next = link

    def __init__(self):
        self.last = None
        self.size = 0

    def no_items(self): return self.size
    def is_empty(self): return self.size == 0

    def insert(self, item):
        n = self._Node(item, None)                  # 새 노드 생성 후 n이 참조
        if self.is_empty():
            n.next = n                              # 새 노드는 자기 자신을 참조
            self.last = n                           # last는 새 노드 참조
        else:
            n.next = self.last.next                 # 새 노드는 첫 노드 참
            self.last.next = n                      # last가 참조하는 노드와 새 노드 연결
        self.size += 1


    def first(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        f = self.last.next                          # 첫 번째 노드를 참조하는 노드 생성 후
        return f.item                               # 새 노드의 item을 return

    def delete(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        x = self.last.next
        if self.size == 1:
            self.last = None
        else:
            self.last.next = x.next                 # last가 참조하는 노드가 두 번째 노드를 연결
        self.size -= 1
        return x.item

    def print_list(self):
        if self.is_empty():
            print("리스트 비어있음")
        else:
            f = self.last.next
            p = f
            while p.next != f:                      # 첫 노드 방문시 중단
                print(p.item, ' -> ', end='')
                p = p.next
            print(p.item)

class EmptyError(Exception):
    pass