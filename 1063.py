#입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.

a,b = map(int, input().split())

if a>b:
  print(a)
else:
    print(b)

# 3항 연산자
print(a if a>b else b)
print(a>b and a or b)
