# 스스로 학습

# functions
def addData(name):
    katok.append(None)
    klen = len(katok)
    katok[klen-1] = name


def insertData(position, name):
    katok.append(None)
    klen = len(katok)
    for i in range(klen-1, position, -1) :
        katok[i] = katok[i-1]
    katok[position] = name

def delData(position):
    klen = len(katok)
    katok[position] = None
    for i in range(position, klen-1) :
        katok[i] = katok[i+1]
    del katok[klen-1]

# vari
katok = []
select = -1

# main
if __name__ == '__main__':
    while select != 4:
        select = int(input('숫자 입력 : '))
        if select == 1:
            name = input('이름 입력 : ')
            addData(name)
            print(katok)
        elif select == 2:
            position = int(input('자리 입력 : '))
            name = input('이름 입력 : ')
            insertData(position, name)
            print(katok)
        elif select == 3:
            position = int(input('자리 입력 : '))
            delData(position)
            print(katok)
        elif select == 4:
            print(katok)
            pass
        else:
            print('1에서 4까지만 입력하세요')

print(katok)