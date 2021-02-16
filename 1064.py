#입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.

a,b,c = map(int, input().split())

# 3항 연산자 숏코딩
# 가운데에서부터 시작
print((a if a<c else c) if a<b else (b if b<c else c))

# a<b ? a:b 
# 앞에 참이면 a 거짓이면 b