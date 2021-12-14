# 자료구조
# data를 표현하고 저장하는 방법 & data를 저장할 수 있는 최적의 방법

# 프로그램 = 자료구조 + 알고리즘 (결과를 도출해내는 과정)
# 자료구조와 알고리즘을 몰라도 프로그램을 짤 수 있지만 방대한 데이터를 최적의 방법으로 저장, 처리
    # 최적의 알고리즘을 찾기 위해 자료구조를 활용
# 자료구조와 알고리즘은 수십년 동안 안 바뀐다! 그래서 코테에서 이 둘을 보는 것임!

# 자료구조의 분류
    # 선형
     # 큐
        # 선입선출
     # 스택
        # 선입후출
     # 리스트 []
        # 추가 append : 항상 리스트의 맨 끝에 추가됨 / 빈 공간을 마지막에 하나 만들고 그 자리에 값을 추가!
        # 삽입 insert : 빈 공간을 하나 만들고 값을 추가함! .insert(추가될 자리, 추가될 값)
        # 삭제 delete : 값을 삭제하고 다른 값들을 앞으로 땡기고 빈 공간을 삭제함
        # 리스트는 항상 꽉 채워져 있어야 함!


# 선형 리스트 함수 functions
# functions 함수부
# add 추가
def addData(name) :
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = name

# insert 삽입
def insertData(position, name) : #어떤 자리에? (position), 무슨 값? (name)
    # position 번째가 아니라 position 번지에 들어가는 것! (컴퓨터는 0번지가 첫 번째임!)
    katok.append(None)
    klen = len(katok)
    # 값들을 뒤로 민다
    for i in range(klen-1, position, -1) :
        katok[i] = katok[i-1]
    katok[position] = name

# delete 삭제
def delData(position) : # 몇 번째에 있는 애를 지우겠다
    klen = len(katok)
    katok[position] = None
    for i in range(position, klen-1) :
        katok[i] = katok[i+1]
    del(katok[klen-1])

# vari(variations) 변수부
katok = []
select = -1 # add 1, insert 2, delete 3, end 4 중 선택

# main 실행부
if __name__ == '__main__' :
    while select != 4 :
        select = int(input('숫자 입력 : '))
        if select == 1 :
            name = input('이름 입력 : ')
            addData(name)
            print(katok)
        elif select == 2 :
            position = int(input('자리 입력 : '))
            name = input('이름 입력 : ')
            insertData(position, name)
            print(katok)
        elif select == 3 :
            position = int(input('자리 입력 : '))
            delData(position)
            print(katok)
        elif select == 4 :
            print(katok)
            pass
        else :
            print('1에서 4까지만 입력하세요')

print(katok)


    # 비선형
     # 트리
     # 그래프






















######################################################################3






