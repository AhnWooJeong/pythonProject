'''
파일 명: Ex22-3-InsertionSort.py

삽입정렬(Insertion Sort)
    리스트의 모든 요소를 앞에서 부터 차례대로
    이미 정렬된 부분과 비교하여 자신의 위치를 찾아 삽입
'''

def insertion_sort(arr):

    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

# 실행코드
arr = [6, 5, 3, 1, 2, 4]
print(insertion_sort(arr))



















