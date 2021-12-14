# 전역변수 선언부
memory = []
pre, current, head = None, None, None
DataArray = ["기용", "윈터", "카리나", "닝닝", "지젤"]

# 함수 선언부
class Node() :
    def __init__(self) :
        self.data = None
        self.link = None

## node 출력
def printNode(start) :
    current = start
    print(current.data, end=' ')
    while current.link != None :
        current = current.link
        print(current.data, end=' ')
    print()

## insert
def insertData(findData, newData) :
    global pre, current, head

    # 맨 앞에 데이터 삽입
    if head.data == findData :
        node = Node()
        node.data = newData
        node.link = head
        head = node
        return

    # 중간에 데이터 삽입
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = newData
            node.link = pre.link
            pre.link = node
            return

    # 마지막에 데이터 삽입
    node = Node()
    node.data = newData
    current.link = node

## delete
def deleteData(findData) :
    global pre, head, current

    # 첫 번째 노드 삭제
    if head.data == findData :
        current = head
        head = current.link
        del current
        return

    # 중간 노드 삭제
    current = head
    while current.link != None :
        pre = current
        current = current.link
        if current.data == findData :
            pre.link = current.link
            del current
            return

# 메인
if __name__ == "__main__" :
    node = Node()
    node.data = DataArray[0]
    head = node
    memory.append(node)

    for data in DataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)


# 구현
# 전역변수 선언
select = -1
# 메인
while select != 3 :
    # 1: 삽입, 2: 삭제, 3: 종료, 이상한거: 다시 입력해주세요
    select = int(input("숫자를 입력하세요: "))
    if select == 1 :
        find = input("찾을 데이터를 입력하세요: ")
        insert = input("삽입할 데이터를 입력하세요: ")
        insertData(find, insert)
    elif select == 2 :
        delete = input("삭제할 데이터를 입력하세요: ")
        deleteData(delete)
    elif select == 3 :
        pass
    else :
        print("1에서 3의 숫자를 입력해주세요")
    printNode(head)