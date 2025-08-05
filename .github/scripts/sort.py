#!/usr/bin/env python3.12
"""
排序程序 - 实现多种排序算法
"""

def bubble_sort(arr):
    """冒泡排序"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    """快速排序"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    """归并排序"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """归并两个已排序的数组"""
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    """主函数"""
    # 测试数据
    test_array = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42]
    
    print("原始数组:", test_array)
    print()
    
    # 冒泡排序
    bubble_result = bubble_sort(test_array.copy())
    print("冒泡排序结果:", bubble_result)
    
    # 快速排序
    quick_result = quick_sort(test_array.copy())
    print("快速排序结果:", quick_result)
    
    # 归并排序
    merge_result = merge_sort(test_array.copy())
    print("归并排序结果:", merge_result)
    
    # 使用Python内置排序
    builtin_result = sorted(test_array)
    print("内置排序结果:", builtin_result)

if __name__ == "__main__":
    main()