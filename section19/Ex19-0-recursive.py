'''
파일 명: Ex19-0-recursive.py

재귀함수(Recursive Function)
    함수 내부에서 자기자신을 호출하는 함수

'''

def recursive_count_number(n):
    if(n <= 0):
        return
    print(n)
    recursive_count_number(n-1)

def count_number(n):
    while True:
        if(n <= 0):
            break
        print(n)
        n -= 1

# 실행코드
# recursive_count_number(5)
count_number(5)





















