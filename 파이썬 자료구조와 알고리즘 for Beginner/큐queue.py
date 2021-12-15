# 큐
# 큐 자료구조 : 입구와 출구가 따로 있는 원통 형태
# 먼저 들어간 것이 먼저 나오는 구조 : 선입선출

# 큐 원리
# 큐 기본 구조
# enQueue(인큐) : 큐에 데이터를 삽입하는 작동
# deQueue(데큐) : 데이터를 추출하는 작동
# front(머리) : 저장된 데이터 중 첫 번째 데이터
# rear(꼬리) : 저장된 데이터 중 마지막 데이터


## 큐의 간단 구현
# 큐 생성
queue = [None, None, None, None, None]
# 초기값
front = rear = -1
# 데이터 삽입 : enQueue
rear += 1 # rear를 한 칸 오른쪽으로 이동
queue[rear] = "화사"
rear += 1
queue[rear] = "솔라"
rear += 1
queue[rear] = "문별"

print("----- 큐 상태 -----")
print('[출구] <--', end=' ')
for i in range(0, len(queue), 1) :
    print(queue[i], end=' ')
print('<-- [입구]')

# 데이터 추출 : deQueue
# 큐에서 데이터 3개 추출

queue = ["화사", "솔라", "문별", None, None]
front = -1
rear = 2

print("----- 큐 상태 -----")
print('[출구] <--', end=' ')
for i in range(0, len(queue), 1) :
    print(queue[i], end=' ')
print('<-- [입구]')
print("-----------------------------------")

front += 1 # front를 한 칸 오른쪽으로 이동
data = queue[front]
queue[front] = None
print('deQueue -->', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)
print("-----------------------------------")

print("----- 큐 상태 -----")
print('[출구] <--', end=' ')
for i in range(0, len(queue), 1) :
    print(queue[i], end=' ')
print('<-- [입구]')
print("-----------------------------------")


## 큐의 일반 구현

# 큐 생성 및 초기화
size = 5
queue = [None for _ in range(size)]
front = rear = -1

# 데이터 삽입
# 큐가 꽉 찼는지 확인 필요 : rear 값이 '큐 크기-1'과 같다면 큐가 꽉 찬 상태

def isQueueFull() :
    global size, queue, front, rear
    if (rear == size-1) :
        return True
    else :
        return False

size = 5
queue = ["화사", "솔라", "문별", "휘인", "정문"]
front = -1
rear = 4

print("큐가 꽉 찼는지 여부:", isQueueFull())
print("-----------------------------------")

def enQueue(data) :
    global size, queue, front, rear
    if (isQueueFull()) :
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

size = 5
queue = ["화사", "솔라", "문별", "휘인", None]
front = -1
rear = 3

print(queue)
enQueue("정문")
print(queue)
enQueue("모니카")
print("-----------------------------------")

# 데이터 추출
# 큐가 비었는지 확인 필요 : front와 rear의 값이 같다면 큐가 비어 있는 상태

def isQueueEmpty() :
    global size, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

size = 5
queue = [None for _ in range(size)]
front = rear = -1

print("큐가 비었는지 여부:", isQueueEmpty())
print("-----------------------------------")

def deQueue() :
    global size, queue, front, rear
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

size = 5
queue = ["화사", None, None, None, None]
front = -1
rear = 0

print(queue)
retData = deQueue()
print("추출한 데이터:", retData)
print(queue)
retData = deQueue()
print("-----------------------------------")

# 데이터 확인
# 추출될 데이터를 큐에 그대로 두고 확인만 하는 것 : peek(픽)

def peek() :
    global size, queue, front, rear
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return None
    return queue[front+1]

size = 5
queue = ["화사", "솔라", "문별", None, None]
front = -1
rear = 2

print(queue)
retData = peek()
print("다음에 추출될 데이터 확인 :", retData)
print(queue)
print("-----------------------------------")


## 큐가 꽉 찼는지 확인하는 함수 개선 버전
def isQueueFull() :
    global size, queue, front, rear
    if (rear != size-1) :
        return False
    elif (rear == size-1) and (front == -1) :
        return True
    else :
        for i in range(front+1, size) :
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

size = 5
queue = [None, None, "문별", "휘인", "정문"]
front = 1
rear = 4

print("큐가 꽉 찼는지 여부 :", isQueueFull())
print("큐 상태 :", queue)
