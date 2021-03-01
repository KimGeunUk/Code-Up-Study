#출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.

a = int(input())
b = input().split()

list = []

for i in range(a-1,-1,-1):
  list.append(b[i])
  print(list[-1], end=" ")

#또는
for i in range(a):
  list.append(int(b[i]))

i = a-1
while i>=0:
  print(list[i], end=" ")
  i -= 1