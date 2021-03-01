#출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.

a = int(input())
b = input().split()

min = 99

for i in range(a):
  if int(b[i]) < min:
    min = int(b[i])  
print(min)
