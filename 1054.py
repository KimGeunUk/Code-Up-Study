#두 개의 참(1) 또는 거짓(0)이 입력될 때,
#모두 참일 때에만 참을 출력하는 프로그램을 작성해보자.

a,b = map(int, input().split())

c = bool(a)
d = bool(b)

if c==1 & d==1:
  print(1)
else:
  print(0)

# 또는
print(int(c and d))
