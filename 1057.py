#두 개의 참(1) 또는 거짓(0)이 입력될 때,
#참/거짓이 서로 같을 때에만 참이 계산되는 프로그램을 작성해보자.

a,b = map(int, input().split())

c = bool(a)
d = bool(b)

print(int(not c ^ d))

#또는
print(int(c == d))

#또는
print('%d' %(c==d))