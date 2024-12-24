'''
파일 명: Ex22-4-QuickSort.py

퀵 정렬(Quick Sort)
    분할 정복 알고리즘, 기준점(pivot)을 설정하고
    pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽으로 분할한 후
    각 부분 리스트에 대해 재귀적으로 퀵정렬을 수행하는 알고리즘

'''
from unittest.mock import right

from numpy.ma.core import equal


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left, right, equal = [], [], []

    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            equal.append(i)

    return quick_sort(left) + equal + quick_sort(right)

# 실행코드
arr = [6, 5, 3, 1, 2, 4]
print(quick_sort(arr))
















