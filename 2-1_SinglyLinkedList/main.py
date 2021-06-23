from slist import SList
if __name__ == '__main__':                              # 이 파이썬 파일(모듈)이 메인이면
    s = SList()                                         # 단순연결리스트 생성
    
    s.insert_front('orange')                            # orange
    s.insert_front('apple')                             # apple - orange
    s.insert_after('cherry', s.head.next)               # apple - orange - cherry
    s.insert_front('pear')                              # pear - apple - orange - cherry
    s.print_list()                                      
    # output : pear -> apple -> orange -> cherry
    
    print('cherry는 %d번째' % s.search('cherry'))       
    # output : cherry 는 3번째

    print('kiwi는', s.search('kiwi'))     
    # output : None
    
    print('배 다음 노드 삭제 후 :\t\t', end = '')       # 마지막'\n'(개행)이 아닌 ''
    s.delete_after(s.head)                              # head가 참조하는 pear의 after 삭제
    s.print_list()
    # output : 배 다음 노드 삭제 후 : pear -> orange -> cherry
    
    print('첫 노드 삭제 후 :\t\t', end = '')
    s.delete_front()
    s.print_list()                                      
    # output : 첫 노드 삭제 후 : orange -> cherry
    
    print('첫 노드로 망고, 딸기, 삽입 후 :\t', end = '')
    s.insert_front('mango')
    s.insert_front('strawberry')
    s.print_list()                                      
    # output : 첫 노드로 망고, 달기 삽입 후 : strawberry -> mango -> orange -> cherry
   
    print('오렌지 다음 노드 삭제 후:\t', end = '')
    s.delete_after(s.head.next.next)
    s.print_list()
    # output : 오렌지 다음 노드 삭제 후 : strawberry -> mango -> orange
