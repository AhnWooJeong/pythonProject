'''
파일 명: Ex06-3-while.py
'''
my_list = []
n = 1
while n != 0:
    n = int(input('정수를 입력하세요(종료는 0입니다.) >>>'))
    my_list.append(n)

my_list.pop()
print(my_list)