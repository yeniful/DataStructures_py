from dlist import DList
if __name__ == '__main__':                              # 이 파이썬 파일(모듈)이 메인이면
    s = DList()                                         # 이중연결리스트 생성   head -> dummy1 <=> dummy2 <- tail

    s.insert_after(s.head, 'apple')                     # head -> apple <- tail
    s.insert_before(s.tail, 'orange')                   # head -> apple <=> orange <- tail
    s.insert_before(s.tail, 'cherry')                   # head -> apple <=> orange <=> cherry <- tail
    s.insert_after(s.head.next, 'pear')                 # head -> apple <=> pear <=> orange <=> cherry <- tail
    s.print_list()
    # output : apple <=> pear <=> orange <=> cherry

    print('마지막 노드 삭제 후 :\t', end = '')
    s.delete(s.tail.prev)
    s.print_list()
    # output : 마지막 노드 삭제 후 : apple <=> pear <=> orange
    
    print('맨 끝에 포도 삽입 후 :\t', end = '')
    s.insert_before(s.tail, 'grape')
    s.print_list()
    # output : 맨 끝에 포도 삽입 후 : apple <=> pear <=> orange <=> grape

    print('첫 노드 삭제 후 :\t', end = '') 
    s.delete(s.head.next)
    s.print_list()
    # output : 첫 노드 삭제 후 : pear <=> orange <=> grape
    
    print('첫 노드 삭제 후 :\t', end = '') 
    s.delete(s.head.next)
    s.print_list()
    # output : 첫 노드 삭제 후 : orange <=> grape

    print('첫 노드 삭제 후 :\t', end = '') 
    s.delete(s.head.next)
    s.print_list()
    # output : 첫 노드 삭제 후 : grape
    
    print('첫 노드 삭제 후 :\t', end = '') 
    s.delete(s.head.next)
    s.print_list()
    # output : 첫 노드 삭제 후 : 리스트 비어있음
