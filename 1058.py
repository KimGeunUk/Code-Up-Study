#두 개의 참(1) 또는 거짓(0)이 입력될 때,
#모두 거짓일 때에만 참이 계산되는 프로그램을 작성해보자.

a,b = map(int, input().split())

c = bool(a)
d = bool(b)

print(int(c==0 and d==0))

#또는
print(int((not c) and (not d)))

#또는
print(int(not(c or d)))