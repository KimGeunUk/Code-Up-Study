#단어를 1개 입력받는다.
#입력받은 단어(영어)의 각 문자를
#한줄에 한 문자씩 분리해 출력한다.
#ex) BOY -> 'B', 'O', 'Y'

a = input()
for i in range(len(a)):
  print("'{}'".format(a[i]))

b = input()
for i in b:
  print("'" + i + "'")
  
