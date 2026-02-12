n = int(input())

def square(n):
    num = 1  # 시작 숫자

    for _ in range(n):
        for _ in range(n):
            print(num, end=" ")
            num += 1
            
            if num == 10:  # 9 다음에는 1로
                num = 1
        print()  # 줄바꿈

square(n)
