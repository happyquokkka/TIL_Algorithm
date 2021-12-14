# 단순 연결 리스트?
# 노드들이 물리적으로 떨어진 곳에 위치
# 각 노드의 번지도 순차적이지 않음
# 화살표로 표시된 연결(링크 link)을 따라가면 선형 리스트 순서와 같음

# 데이터를 삽입/삭제 시
# 단순 연결 리스트는 많은 작업이 필요하여 오버헤드가 발생하는 선형 리스트와 달리
# 해당 노드의 앞뒤 링크만 수정하면 되므로 오버헤드가 거의 발생하지 않음

# 단순 연결 리스트의 원리
# 노드 구조
# 단순 연결 리스트는 다음 데이터를 가리키는 링크가 더 필요
# 노드 Node : 데이터와 링크로 구성된 항목


# 노드 생성과 연결

# 1. 노드 생성
class Node() : # Node라는 데이터형을 만듦
    def __init__ (self) : # 데이터형을 생성할 때 자동으로 실행되는 부분
        # 데이터와 링크가 저장되는 부분
        self.data = None
        self.link = None

# 첫 번째 노드 생성
node1 = Node()
node1.data = "다현"
print(node1.data, end=' ')

# 2. 노드 연결 : 두 번째 노드를 생성하고 첫 번째 노드와 연결
node2 = Node()
node2.data = '정연'
node1.link = node2 # 첫 번째 노드의 링크에 두 번째 노드를 넣어 연결

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

# 원시적인 방법으로 출력
# print(node1.data, end=' ')
# print(node1.link.data, end=' ') # node1의 link에 연결된 node2의 data = '정연'
# print(node1.link.link.data, end=' ')
# print(node1.link.link.link.data, end=' ')
# print(node1.link.link.link.link.data, end=' ')



# 단순 연결 리스트의 간단 구현
# 25~29행의 노드의 처음부터 끝까지 출력하는 함수로 작성하기 위한 동작 과정
# 1. 첫 번째 노드를 현재(current) node로 지정하고, 현재 노드의 데이터인 다현 출력
# 2. 현재 노드의 링크가 비어 있지 않다면 현재 노드를 현재 노드의 링크가 가리키는 노드로 변경한 후 현재 노드의 데이터인 정연 출력
# 3. 앞의 2단계를 반복하다 현재 노드의 링크가 비어 있으면 종료

current = node1 # node1을 현재 노드로 지정
while current.link != None : # 현재 노드의 링크가 비어있지 않을 때까지 반복
    current = current.link # 현재 노드(current)는 현재 노드의 링크가 가리키는 노드로 반복하여 변경됨
    print(current.data, end=' ')
print('\r')



# 노드 삽입 : 중간에 데이터 삽입
# 1. 새 노드를 생성하고 데이터에 정문을 입력
# 2. 새 노드(정문 노드)의 링크에 정연 노드의 링크를 복사 / 정연 노드와 정문 노드 모두 쯔위 노드를 가리킴
# 3. 정연 노드의 링크에 정문 노드를 지정

node1 = Node()
node1.data = "다현"
print(node1.data, end=' ')

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

newNode = Node() # 삽입할 새 노드 생성
newNode.data = '정문'
newNode.link = node2.link # node2(정연 노드)의 링크가 가리키는 쯔위 노드를 새로운 노드의 링크에 연결
node2.link = newNode # newNode를 node2(정연 노드)의 링크로 연결

# 확인
current = node1
while current.link != None :
    current = current.link
    print(current.data, end=' ')
print('\r')



# 노드 삭제 : 중간 데이터 삭제
# 1. 삭제할 쯔위 노드의 링크를 바로 앞 정연노드의 링크로 복사한다. 그러면 정연 노드가 사나 노드를 가리킨다.
# 2. 쯔위 노드를 삭제한다.

node1 = Node()
node1.data = "다현"
print(node1.data, end=' ')

node2 = Node()
node2.data = '정연'
node1.link = node2

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

node2.link = node3.link # node3(쯔위 노드)의 링크에 연결된 node4를 node2의 링크로 연결
del(node3) # node3(쯔위 노드) 삭제

# 확인
current = node1
while current.link != None :
    current = current.link
    print(current.data, end=' ')


# 단순 연결 리스트의 일반 구현
# 헤드 head : 첫 번째 노드
# 현재 current : 지금 처리 중인 노드
# 이전 pre : 현재 처리 중인 노드의 바로 앞 노드
# 처음에는 모두 비어 있으면 되므로 다음과 같이 초기화
memory = []
head, current, pre = None, None, None

# 데이터 입력 과정
# 첫 번째 데이터 입력
node = Node()
node.data = dataArray[0]
head = node
memory.append(node)

# 두 번째 이후 데이터 입력
pre = node
node = Node()
node.data = data # 두 번째 이후 노드
preNode.link = node
memory.append(node)

# 클래스와 함수 선언부
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    if current == None :
        return
    print(current.data, end = ' ')
    while current.link != None :
        current = current.link
        print(current.data, end = ' ')
    print()

# 전역변수 선언부
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

# 메인코드부
if __name__ == "__main__" :
    node = Node() # 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:] : # 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)


# 노드 삽입 : 중간 노드 삽입
# 1. 헤드head에서 시작해서 현재current 노드가 사나인지 확인
# 2. 현재 노드를 이전(pre)노드로 지정하고 현재 노드를 다음 노드로 이동한다. 그리고 현재 노드가 사나인지 확인
# 3. 현재 노드가 사나일때까지 2단계 반복
# 4. 현재 노드가 사나라면 우선 새 노드(솔라)를 생성한 후 이전 노드의 링크를 새 노드의 링크로 지정
# 5. 이전 노드의 링크를 새 노드로 지정

current = head
while 마지막 노드까지 :
    pre = current # 현재 노드를 pre노드로 지정
    current = current.link # 현재 노드의 링크가 가리키는 노드를 현재 노드로 지정
    if current.data == "사나" : # 현재 노드가 사나일때까지
        node = Node() # 삽입할 새 노드 생성
        node.data = "솔라" # 새 노드의 데이터에 솔라 입력
        node.link = current # 새 노드의 링크를 현재 노드인 사나 노드에 연결
        pre.link = node # 이전 노드의 링크를 새 노드로 지정


# 노드 삽입 : 마지막 노드 삽입
# 1. 중간 노드 삽입 과정과 동일하므로 없는 데이터인 정문을 찾는다
# 2. 마지막 노드까지 정문을 찾지 못했다면 우선 새 노드를 생성한 후 현재 노드의 링크를 새 노드로 지정한다
node = Node()
node.data = "문별"
current.link = node

## 클래스와 함수 선언부
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, current, pre

    if head.data == findData :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head
    while current.link != None : # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    node = Node() # 마지막 노드 삽입
    node.data = insertData
    current.link = node

# 전역 변수 선언부
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

# 메인 코드부
if __name__ == "__main__" :
    node = Node() # 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:] : # 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)

    insertNode("다현", "화사")
    printNodes(head)

    insertNode("사나", "솔라")
    printNodes(head)

    insertNode("정문", "문별")
    printNodes(head)

# 노드 삭제 : 첫 번째 노드 삭제
current = head # 현재 노드를 삭제할 노드인 헤드와 동일하게 만듦
head = head.link # 헤드를 삭제할 노드(다현 노드)의 링크가 가리키던 정연 노드로 변경
del(current)

current = head
while # 마지막 노드까지 :
    pre = current
    current = current.link
    if current.data == "쯔위" :
        pre.link = current.link
        del(current)

# 노드 삭제 함수의 완성
class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    if current == None:
        return
    print(current.data, end=' ')
    while current.link != None:
        current = current.link
        print(current.data, end=' ')
    print()

def deleteNode(deleteData) :
    global memory, head, current, pre

    if head.data == deleteData : # 첫 번째 노드 삭제
        current = head
        head = head.link
        del(current)
        return

    current = head  # 첫 번째 외 노드 삭제
    while current.link != None :
        pre = current
        current = current.link
        if current.data == deleteData :
            pre.link = current.link
            del(current)
            return

# 전역 변수 선언부
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

# 메인 코드부
if __name__ == "__main__" :
    node = Node() # 첫 번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:] : # 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)

    deleteNode("다현")
    printNodes(head)

    deleteNode("쯔위")
    printNodes(head)

    deleteNode("지효")
    printNodes(head)

    deleteNode("정문")
    printNodes(head)