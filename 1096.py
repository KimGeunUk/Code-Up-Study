#바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
#n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.


list = [[0]*19 for i in range(19)]

#또는
m=[]
for i in range(20):
  m.append([])
  for j in range(20):
    m[i].append(0)

for i in range(19):
  for j in range(19):
    list[i][j] = 0

a=int(input())

for i in range(a):
  c,d = input().split()
  list[int(c)-1][int(d)-1] = 1

for i in range(19):
  for j in range(19):
    print(list[i][j], end=" ")
  print(" ")