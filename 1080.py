#1, 2, 3 ... 을 계속 더해 나갈 때,
#그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지
#계속 더하는 프로그램을 작성해보자.

a = int(input())
b = 0

for i in range(1,a):
  b += i
  if b>=a:
    print(i)
    break

# 정확한 풀이
d = 0
c = 0

while c<a:
  d += 1
  c += d

print(d)