'''
파일 명: Ex20-7-O(n!).py

O(n!)
    팩토리얼 시간 복잡도, 순열을 구하는 알고리즘
'''

def permute(data, i, length):
    if i == length:
        print(''.join(data))
    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, length)
            data[i], data[j] = data[j], data[i]


# 실행코드
data = list('abcd')
permute(data, 0, len(data))




















