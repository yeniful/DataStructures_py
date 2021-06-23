from slist import SList
if __name__ == '__main__':                  # 이 파이썬 파일(모듈)이 메인이면
    s = SList()                             # 단순연결리스트 생성
    s.insert_front('orange')                # orange
    s.insert_front('apple')                 # apple - orange
    s.inser_after('cherry', s.head.next)    # cherry - apple - orange
    s.insert_front('pear')
    s.print('cherry는 %d번째 %s.search(''cherry)')  # cherrys는 1번째
