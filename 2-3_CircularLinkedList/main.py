from clist import Clist
if __name__ == '__main__':  # 이 파이썬 파일(모듈)이 메인이면
    s = Clist()             # 원형 연결리스트 생성
    s.insert('pear')        # pear
    s.insert('cherry')      # pear cherry
    s.insert('orange')      # pear cherry orange
    s.insert('apple')       # pear cherry orange apple
    s.print_list()          # output : pear -> cherry -> orange -> apple
    print('s의 길이 =', s.no_items())   # output : s의 길이 = 4
    print('s의 첫 항목 :', s.first())   # output : pear
    s.delete()
    print('첫 노드 삭제 후 :')         
    s.print_list()          # output :  첫 노드 삭제 후 : cherry -> orange -> apple
    print('s의 길이 =', s.no_items())   # output : s의 길이 = 3
    print('s의 첫 항목 :', s.first())   # output : cherry
    s.delete()
    print('첫 노드 삭제 후 :')          
    s.print_list()          # output :  첫 노드 삭제 후 : orange -> apple
    s.delete()
    print('첫 노드 삭제 후 :')          
    s.print_list()          # output :  첫 노드 삭제 후 : apple
    s.delete()
    print('첫 노드 삭제 후 :')          
    s.print_list()          # output : 첫 노드 삭제 후 : 리스트 비어있음
