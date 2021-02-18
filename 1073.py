#0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단해보자.

a = input().split()

for i in a:
  if i=='0':
    break
  print(i)