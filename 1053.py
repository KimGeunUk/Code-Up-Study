#1(true, 참) 또는 0(false, 거짓) 이 입력되었을 때
#반대로 출력하는 프로그램을 작성해보자.

a = int(input())

if a==1:
  print(0)
else:
  print(1)

# 또는
b = bool(a)
print(int(not b))

