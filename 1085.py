#필요한 저장 용량을 계산하는 프로그램을 작성해보자.

a, b, c, d = map(int,input().split())

byte = a*b*c*d/8
kb = byte/1024
mb = kb/1024

print('%.1f MB' %mb)