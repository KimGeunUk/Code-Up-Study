#년월일을 출력하는 방법은 나라마다, 형식마다 조금씩 다르다.
#년월일(yyyy.mm.dd)를 입력받아,
#일월년(dd-mm-yyyy)로 출력해보자.

a,b,c = input().split('.')

print("{}-{}-{}".format(c,b,a))