# 트리 구조
# 회사 사장을 필두로 그 아래 직책들이 구성되어 있는 조직표 or 컴퓨터의 상위 폴더 안에 하위 폴더들이 계속 이어져 있는 구조
# 트리 자료구조 : 나무를 거꾸로 뒤집어 놓은 형태

# 이진 트리 : 모든 노드의 자식이 최대 2개인 트리(자식이 2개 이하로 구성)
# 이진 트리의 종류
# 포화 이진 트리, 완전 이진 트리, 평향 이진 트리

# 이진 트리 생성
class TreeNode() :
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None

node1 = TreeNode()
node1.data = "화사"

node2 = TreeNode()
node2.data = "솔라"
node1.left = node2

node3 = TreeNode()
node3.data = "문별"
node1.right = node3

node4 = TreeNode()
node4.data = "휘인"
node2.left = node4

node5 = TreeNode()
node5.data = "쯔위"
node2.right = node5

node6 = TreeNode()
node6.data = "선미"
node3.left = node6

print(node1.data, end=' ')
print()
print(node1.left.data, node1.right.data, end=' ')
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data)
print("---------------")

# 이진 트리의 순회
# 순회(traversal) : 이진 트리의 노드 전체를 한 번씩 방문하는 것
# 노드 데이터를 처리하는 순서에 따라 '전위 순회', '중위 순회', '후위 순회'로 분류

# 전위 순회 : 현재 노드 데이터 처리 -> 왼쪽 서브 트리로 이동 -> 오른쪽 서브 트리로 이동
# 중위 순회 : 왼쪽 서브 트리로 이동 -> 현재 노드 데이터 처리 -> 오른쪽 서브 트리로 이동
# 후위 순회 : 왼쪽 서브 트리로 이동 -> 오른쪽 서브 트리로 이동 -> 현재 노드 데이터 처리

# 이진 트리 순회 구현
def preorder(node) :
    if node == None :
        return
    print(node.data, end = '->')
    preorder(node.left)
    preorder(node.right)

def inorder(node) :
    if node == None :
        return
    inorder(node.left)
    print(node.data, end = '->')
    inorder(node.right)

def postorder(node) :
    if node == None :
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end = '->')

print('전위 순회 :', end=' ')
preorder(node1)
print('끝')
print('중위 순회 :', end=' ')
inorder(node1)
print('끝')
print('후위 순회 :', end=' ')
postorder(node1)
print('끝')
print('--------------------------------------')


# 이진 트리의 일반 구현

## 함수 선언부
class TreeNode() :
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None


## 전역변수 선언부
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] :
    node = TreeNode() # 노드 생성
    node.data = name # 노드에 데이터 입력
    current = root # 루트 노드를 현재 작업중인 노드로 설정
    while True : #무한반복
        if name < current.data : # 새로 생성한 노드가 현재 작업중인 노드의 데이터보다 값이 작다면
            if current.left == None : # 위의 조건을 만족하며, 현재 작업중인 노드의 왼쪽 링크가 비어있다면
                current.left = node
                break
            current = current.left # 새로 생성한 노드가 현재 작업중인 노드의 데이터보다 값이 작고, 현재 작업중인 노드의 왼쪽 링크가 비어있지 않은 경우
                                   # 현재 작업중인 노드를 그 노드의 왼쪽에 링크된 노드로 변경
        else :
            if current.right == None :
                current.right = node
                break
            current = current.right
    memory.append(node)

print("이진 탐색 트리 구성 완료!")

# 이진 탐색 트리의 검색 작동
## 함수 선언부
class TreeNode() :
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None


## 전역변수 선언부
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인

node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] :
    node = TreeNode()
    node.data = name
    current = root
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else :
            if current.right == None :
                current.right = node
                break
            current = current.right

memory.append(node)

# 이하는 이진 탐색 트리 검색 작동
findName = '마마무'

current = root
while True :
    if findName == current.data :
        print(findName, "을(를) 찾음")
        break
    elif findName < current.data :
        if current.left == None :
            print(findName, '이(가) 트리에 없음')
            break
        current = current.left
    else :
        if current.right == None :
            print(findName, '이(가) 트리에 없음')
            break
        current = current.right


# 이진 탐색 트리에서 데이터 삭제
# 1. 리프 노드(맨 아래쪽 노드)를 삭제하는 경우

## 함수 선언부
class TreeNode() :
    def __init__ (self) :
        self.left == None
        self.data == None
        self.right == None

## 전역변수 선언부
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크', '걸스데이', '트와이스']

## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] :
    node = TreeNode()
    node.data = name
    current = root
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else :
            if current.right == None :
                current.right = node
                break
            current = current.right

# 이하는 이진 탐색 트리에서 데이터를 삭제하는 작동



# 2. 자식 노드가 하나 있는 노드를 삭제하는 경우