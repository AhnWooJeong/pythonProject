'''
파일 명:Ex20-3-O(n).py

O(N)
    선형 시간 복잡도, 입력 크기에 비례하여 시간이 걸리는 알고리즘
'''

def linear_search(arr, x):
    size = len(arr)

    for i in range(size):
        if arr[i] == x:
            return 1

    return -1   # 찾고자 하는 값이 없는 경우 -1

# 실행코드
arr = [1, 3, 4, 5, 9]
print(linear_search(arr, 5))













