#월이 입력될 때 계절 이름이 출력되도록 해보자.

a = int(input())

if a == 12 or a==1 or a==2:
  print("winter")
elif a== 3 or a== 4 or a== 5:
  print("spring")
elif a== 6 or a== 7 or a==8:
  print("summer")
elif a== 9 or a==10 or a==11:
  print("fall")