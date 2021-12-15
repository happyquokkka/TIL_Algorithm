# 원형 큐 구현 백지복습

## 함수 선언부
# 큐가 꽉 차 있는지 확인하는 함수
def isQueueFull() :
    global size, wonqueue, front, rear
    if ((rear+1) % size == front) :
        return True
    else :
        return False

# 큐가 비어있는지 확인하는 함수
def isQueueEmpty() :
    global size, wonqueue, front, rear
    if (rear == front) :
        return True
    else : False

# 큐에 데이터를 삽입하는 작동
def enQueue(data) :
    global size, wonqueue, front, rear
    if (isQueueFull()) :
        print("큐가 꽉 찼습니다.")
        return
    rear = (rear+1) % size
    wonqueue[rear] = data

# 큐에서 데이터를 추출하는 작동
def deQueue() :
    global size, wonqueue, front, rear
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return None
    front = (front+1) % size
    data = wonqueue[front]
    wonqueue[front] = None
    return data

# 큐의 데이터를 확인하는 작동
def peek() :
    global size, wonqueue, front, rear
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return None
    return wonqueue[(front+1) % size]


## 전역변수 선언부
size = int(input("큐 크기를 입력하세요 : "))
wonqueue = [None for _ in range(size)]
front = rear = 0


## 메인
if __name__ == "__main__" :
    select = input("삽입(I)/ 추출(E)/ 확인(V)/ 종료(X) 중 하나를 선택 :")

    while (select != 'X' and select != 'x') :
        if select == 'I' or select == 'i' :
            data = input("입력할 데이터 :")
            enQueue(data)
            print("큐 상태 :", wonqueue)
            print("front :", front, "rear :", rear)
        elif select == 'E' or select == 'e' :
            data = deQueue()
            print("추출된 데이터 :", data)
            print("큐 상태 :", wonqueue)
            print("front :", front, "rear :", rear)
        elif select == 'V' or select == 'v' :
            data = peek()
            print("확인된 데이터 :", data)
            print("큐 상태 :", wonqueue)
            print("front :", front, "rear :", rear)
        else :
            print("입력이 잘못되었습니다.")

        select = input("삽입(I)/ 추출(E)/ 확인(V)/ 종료(X) 중 하나를 선택 :")

    print("프로그램을 종료합니다.")