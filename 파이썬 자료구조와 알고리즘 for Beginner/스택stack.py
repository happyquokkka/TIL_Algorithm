# 스택
# 스택 자료구조 : 한 쪽 끝이 막힌 형태
# 입구가 하나이기 때문에 먼저 들어간 것이 가장 나중에 나오는 구조 : 선입후출

# 스택 원리
# 스택 기본 구조
# push : 스택에 데이터를 삽입하는 작동
# pop : 스택에 데이터를 추출하는 작동
# top : 스택에 들어 있는 가장 위의 데이터


## 스택의 간단 구현

# 데이터 삽입
stack = [None, None, None, None, None] # 크기가 5칸인 스택 생성
top = -1 # top 초기값 설정

top += 1
stack[top] = "커피"

top += 1
stack[top] = "녹차"

top += 1
stack[top] = "꿀물"

print("----- 스택 상태 -----")
for i in range(len(stack)-1, -1, -1) :
    print(stack[i])

# 데이터 추출
stack = ["커피", "녹차", "꿀물", None, None]
top = 2

print("----- 스택 상태 -----")
for i in range(len(stack)-1, -1, -1) :
    print(stack[i])

print("---------------")
data = stack[top] # 제일 위에 있는 데이터 지정
stack[top] = None
top -= 1 # top을 밑으로 한 칸 내림
print("pop---->", data)

data = stack[top]
stack[top] = None
top -= 1
print("pop---->", data)

data = stack[top]
stack[top] = None
top -= 1
print("pop---->", data)
print("---------------")

print("----- 스택 상태 -----")
for i in range(len(stack)-1, -1, -1):
    print(stack[i])
print("-------------------")


## 스택의 일반 구현

# 스택 생성 및 초기화

size = 5
stack = [None for _ in range(size)]
top = -1

# 데이터 삽입
# 스택이 꽉 찼는지 확인 필요: top 값이 '스택 크기 -1'과 같다면 스택이 꽉 찬 상태

def isStackFull() :
    global size, stack, top
    if (top == size-1) :
        return True
    else :
        return False

size = 5
stack = ["커피", "녹차", "꿀물", "콜라", "환타"]
top = 4

print("스택이 꽉 찼는지 여부 ==>", isStackFull())
print("-------------------")

def push(data) :
    global size, stack, top
    if (isStackFull()) :
        print("스택이 꽉 찼습니다.")
        return
    top += 1
    stack[top] = data

size = 5
stack = ["커피", "녹차", "꿀물", "콜라", None]
top = 3

print(stack)
push("환타")
print(stack)
push("게토레이")
print("-------------------")

# 데이터 추출
# 스택이 비었는지 확인 필요 : top 값이 -1이라면 스택이 비어 있는 상태

def isStackEmpty() :
    global size, stack, top
    if (top == -1) :
        return True
    else :
        return False

size = 5
stack = [None for _ in range(size)]
top = -1

print("스택이 비었는지 여부 ==>", isStackEmpty())

def pop() :
    global size, stack, top
    if (isStackEmpty()) : # 디폴트값이 TRUE ( == True 안 해줘도 됨)
        print("스택이 비었습니다")
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

size = 5
stack = ["커피", None, None, None, None]
top = 0

print(stack) # ['커피', None, None, None, None]
retData = pop() # 함수 실행
print("추출한 데이터 ==>", retData)
print(stack) # [None, None, None, None, None]
retData = pop() # 함수 실행
print("-------------------")


# 데이터 확인
# top 위치의 데이터를 확인만 하고 스택에 그대로 두는 것 : peek(픽)

def peek() :
    global size, stack, top
    if (isStackEmpty()) :
        print("스택이 비었습니다.")
        return None # 스택이 비었다면(확인할 데이터가 없다면) 아무것도 return 하지 않음
    return stack[top] # 비어있지 않다면 현재 top의 위치에 해당하는 data return

size = 5
stack = ["커피", "녹차", "꿀물", None, None]
top = 2

print(stack)
retData = peek()
print("top의 data 확인 ==>", retData)
print(stack)
print("-------------------")


