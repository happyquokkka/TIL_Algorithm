## 함수
# 스택이 꽉 차있는지 확인하는 함수
def isStackFull() :
    global size, stack, top
    if (top >= size-1) :
        return True
    else :
        return False

# 스택이 비어있는지 확인하는 함수
def isStackEmpty() :
    global size, stack, top
    if (top == -1) :
        return True
    else :
        return False

# 데이터 삽입 작동
def push(data) :
    global size, stack, top
    if (isStackFull()) :
        print("스택이 꽉 찼습니다.")
        return None
    top += 1
    stack[top] = data

# ✔ 데이터 추출 작동
def pop() :
    global size, stack, top
    if (isStackEmpty()) :
        print("스택이 비었습니다.")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data # 어느 값을 삭제(추출)했는지 return

# 데이터 확인 작동
def peek() :
    global size, stack, top
    if (isStackEmpty()) :
        print("스택이 비었습니다.")
        return None
    return stack[top]


## 전역변수 선언부
size = 5
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
