# 이진탐색트리 (BST)
class BST :
    def __init__(self) :
        self.root = None

    def get_root(self) :
        return self.root

    def preorder_traverse(self, cur, f) : # 전위순회 : root -> 왼쪽 서브트리 -> 오른쪽 서브트리
        if not cur : # if node == None : 으로도 작성 가능!
            return
        f(cur.data)
        self.preorder_traverse(cur.left, f)
        self.preorder_traverse(cur.right, f)

class TreeNode : # 하나의 노드 클래스
    def __init__(self) :
        self.data = 0
        self.left = None
        self.right = None

class BST : # 이진탐색트리 클래스
    # BST의 루트 노드
    def __init__(self) :
        self.root = None

    # 루트 노드를 찾는 함수
    def get_root(self) :
        return self.root

    # 전위순회
    # f는 find...?
    def preorder_traverse(self, cur, f) :
        if not cur :
            return
        f(cur.data)
        self.preorder_traverse(cur.left, f)
        self.preorder_traverse(cur.right, f)

    def insert(self, data) :
        new_node = TreeNode() # 새 노드 생성
        new_node.data = data # 새 노드에 데이터 입력

        cur = self.root # 현재 작업중인 노드(current)를 root로 설정

        # 루트 노드가 없을 때
        if cur == None :
            self.root = new_node  # 루트 노드를 새 노드로 설정
            return

        # 삽입할 노드의 위치를 찾아 삽입
        while True :
            # parent는 현재 순회중인 노드의 부모 노드를 가리킴
            parent = cur
            # 삽입할 데이터가 현재 노드 데이터보다 작을 때
            if data < cur.data :
                cur = cur.left
                # 왼쪽 서브 트리가 None이면 새 노드를 위치시킨다.
                if not cur :
                    parent.left = new_node
                    return
            # 삽입할 데이터가 현재 노드 데이터보다 클 때
            else :
                cur = cur.right
                # 오른쪽 서브 트리가 None이면 새 노드를 위치시킨다.
                if not cur :
                    parent.right = new_node
                    return