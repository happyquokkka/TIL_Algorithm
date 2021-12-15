### 원형 큐
# 큐의 처음과 끝이 연결된 구조
# 데이터가 많을 경우 선형 큐에서 발생하는 오버헤드 방지할 수 있음
# (데이터를 순차적으로 앞으로 당기지 않고, rear만 한 칸 늘려 데이터 삽입하면 되기 때문에)
# front와 rear의 초기값이 0

## 원형 큐 원리
# 원형 큐 생성 및 초기화
# size = 5
# wonqueue = [None for _ in range(size)]
# front = rear = 0

# 원형 큐가 빈 경우와 꽉 찬 경우
# 1. front와 rear가 동일하면 비어 있다는 의미
# 2. rear+1과 front가 같으면 꽉 차있다는 의미

# 원형 큐의 데이터 삽입과 추출
# 1. 데이터 삽입
# if (큐가 꽉 찼음) :
#   return
# rear = (rear+1) % 큐크기
# queue[rear] = "화사"
# 2. 데이터 추출
# if (큐가 비어있음) :
#   return
# front = (front+1) % 큐크기
# data = queue[front]
# queue[front] = None


## 원형 큐 구현
# 함수 선언부
def isQueueFull() :
    global size, wonqueue, front, rear
    if ((rear+1)%size == front) :
        return True
    else :
        return False

def isQueueEmpty() :
    global size, wonqueue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def enQueue(data) :
    global size, wonqueue, front, rear
    if (isQueueFull()) :
        print("큐가 꽉 찼습니다.")
        return
    else :
        rear = (rear+1) % size
        wonqueue[rear] = data

def deQueue() :
    global size, wonqueue, front, data
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return None
    else :
        front = (front+1) % size
        data = wonqueue[front]
        wonqueue[front] = None
        return data

def peek() :
    global size, wonqueue, front, rear
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return None
    else :
        return wonqueue[(front+1) % size]

# 전역변수 선언부
size = int(input("큐 크기를 입력하세요 :"))
wonqueue = [None for _ in range(size)]
front = rear = 0

# 메인 코드부
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