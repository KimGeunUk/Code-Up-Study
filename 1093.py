#출석 번호를 n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

a = int(input())
b = input().split()

list = []

for i in range(24):
  list.append(0)

for i in range(a):
  list[int(b[i])] += 1

for i in range(1,24):
  print(list[i], end=" ")
