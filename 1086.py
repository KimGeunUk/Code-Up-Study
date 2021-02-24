#압축하지 않고 저장하기 위해 필요한 저장 용량을 계산하는 프로그램을 작성해 보자.

w, h, b= map(int,input().split())

byte = (w*h*b)/8
mb = byte / 1024 / 1024

print('%.2f MB' %mb)