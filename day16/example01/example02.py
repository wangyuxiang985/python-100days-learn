"""
排序算法（选择、冒泡和归并)
"""

def select_sort(origin_items, comp=lambda x,y:x < y):
    """简单选择排序"""
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items

if __name__ == "__main__":
    tmp = [1, 2, 5, 2, 6, 1, 3]
    sort = select_sort(tmp)
    print(sort)