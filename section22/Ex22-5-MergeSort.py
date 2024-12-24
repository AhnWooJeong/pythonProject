'''
파일 명: Ex22-5-MergeSort.py

병합정렬(Merge Sort)
    분할 정복 알고리즘의 일종으로, 리스트를 절반으로 나눈 후
    각각을 재귀적으로 합병 정렬하고, 다시 합치면서 정렬하는 알고리즘
'''

from heapq import merge
from unittest.mock import right


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    '''
    arr = [5, 2, 8, 6, 1, 9, 3, 7]

    '''
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []

    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result


# 실행코드
arr = [5, 2, 8, 6, 1, 9, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)