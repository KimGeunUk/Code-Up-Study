#1부터 n까지, 1부터 m까지 숫자가 적힌 서로 다른 주사위 2개를 던졌을 때,
#나올 수 있는 모든 경우를 출력해보자.

a,b = map(str,input().split())

c = int(a)
d = int(b)

for i in range(1, c+1):
  for j in range(1, d+1):
    print("{} {}".format(i,j))
    print(c, d)