#바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
#n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

#또는
m=[]
for i in range(19):
   m.append([])
   for j in range(19): 
     m[i].append(0)

for i in range(19):
  x=input().split()
  for j in range(19):    
    m[i][j]=int(x[j])

a=int(input())

for i in range(a):
  c,d = input().split()
  for j in range(19):
    if m[j][int(d)-1]==0:
      m[j][int(d)-1] =1
    else:
      m[j][int(d)-1] =0
  
    if m[int(c)-1][j]==0:
      m[int(c)-1][j]=1
    else:
      m[int(c)-1][j]=0
   

for i in range(19):
  for j in range(19):
    print(m[i][j], end=" ")
  print(" ")