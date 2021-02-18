#정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력해보자.

a = int(input())

for i in range(a):
  print(a-1)
  a -= 1

#while문

while a>0:
  a-=1
  print(a)