# 큐 구현 백지복습!

## 함수 선언부
# 큐가 꽉 차있는지 확인하는 함수
def isQueueFull() :
    global size, queue, front, rear
    if (rear != size-1) :
        return False
    elif (front == -1) and (rear == size-1) :
        return True
    else :
        for i in range(front+1, size) :
            front[i-1] = front[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

# 큐가 비어있는지 확인하는 함수
def isQueueEmpty() :
    global size, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

# 큐에 데이터를 삽입하는 함수
def enQueue(data) :
    global size, queue, front, rear
    if (isQueueFull()) :
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

# 큐에서 데이터를 추출하는 함수
def deQueue() :
    global size, queue, front, rear
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

# 큐에서 데이터를 확인하는 함수
def peek() :
    global size, queue, front, rear
    if (isQueueEmpty()) :
        print("큐가 비었습니다.")
        return None
    return queue[front+1]

## 전역변수 선언부
size = int(input("큐 크기를 입력하세요 : "))
queue = [None for _ in range(size)]
front = rear = -1

## 메인
if __name__ == "__main__" :
    select = input("삽입(I)/ 추출(E)/ 확인(V)/ 종료(X) 중 하나 선택: ")

    while (select != 'X' and select != 'x') :
        if select == 'I' or select == 'i' :
            data = input("입력할 데이터 :")
            enQueue(data)
            print("큐 상태 :", queue)
        elif select == 'E' or select == 'e' :
            data = deQueue()
            print("추출된 데이터 :", data)
            print("큐 상태 :", queue)
        elif select == 'V' or select == 'v' :
            data = peek()
            print("확인된 데이터 :", data)
            print("큐 상태 :", queue)
        else :
            print("입력이 잘못되었습니다. 다시 입력해주세요.")

        select = input("삽입(I)/ 추출(E)/ 확인(V)/ 종료(X) 중 하나 선택: ")

    print("프로그램 종료")
