#영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.

a = input()

for i in range(ord(a)-97+1):
  print(chr(97+i))

# 다른 방법

b = ord(a)
c = ord('a')

while c<=b:
  print(chr(c), end=' ')
  c += 1