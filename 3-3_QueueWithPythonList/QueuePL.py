def add(item):      # 삽입 연산
    q.append(item)

def remove():       # 삭제 연산
    if len(q) != 0:
        item = q.pop(0)
        return item
