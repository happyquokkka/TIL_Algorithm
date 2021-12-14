# 스택 완성

## 함수 선언부

# 스택이 꽉 차있는지 확인하는 함수
def isStackFull() :
    global size, stack, top
    if (top >= size-1) : # top의 위치가 len(stack)-1과 같다면 스택이 꽉 찬 상태
        return True
    else :
        return False

# 스택이 비었는지 확인하는 함수
def isStackEmpty() :
    global size, stack, top
    if (top == -1) : # top의 위치가 -1이라면 스택이 비어있는 상태
        return True
    else :
        return False

# 스택에 데이터를 삽입하는 함수
def push(data) :
    global size, stack, top
    if (isStackFull()) :
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

# 스택에서 데이터를 추출하는 함수
def pop() :
    global size, stack, top
    if (isStackEmpty()) :
        print("스택이 비었습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

# 스택에서 top 위치의 데이터를 확인하는 함수
def peek() :
    global size, stack, top
    if (isStackEmpty()) :
        print("스택이 비었습니다.")
        return None
    return stack[top]


## 전역변수 선언부
size = int(input("스택 크기를 입력하세요: "))
stack = [None for _ in range(size)]
top = -1


## 메인
if __name__ == "__main__" :
    select = input("삽입(I) / 추출(E) / 확인(Y) / 종료(X) 중 하나를 선택하시오 : ")

    while (select != 'X' and select != 'x') :
        if select == 'I' or select == 'i' :
            data = input("입력할 데이터: ")
            push(data)
            print("스택 상태: ", stack)
        elif select == 'E' or select == 'e' :
            data = pop()
            print("추출된 데이터 :", data)
            print("스택 상태: ", stack)
        elif select == 'Y' or select == 'y' :
            data = peek()
            print("확인된 데이터: ", data)
            print("스택 상태: ", stack)
        else :
            print("입력이 잘못됨")

        select = input("삽입(I) / 추출(E) / 확인(Y) / 종료(X) 중 하나를 선택하시오 : ")

    print("프로그램을 종료합니다.")
