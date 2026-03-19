def count_unique_elements(my_list: list) -> int:
    return len(set(my_list))

def remove_duplicates(my_list: list) -> list:
    result = []
    seen = set()
    for x in my_list:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result

def reverse_list(my_list: list) -> list:
    return my_list[::-1]

def max_value(my_list: list) -> int:
    m = my_list[0]
    for x in my_list:
        if x > m:
            m = x
    return m

def min_value(my_list: list) -> int:
    m = my_list[0]
    for x in my_list:
        if x < m:
            m = x
    return m

def sum_values(my_list: list) -> int:
    total = 0
    for x in my_list:
        total += x
    return total

def average(my_list: list) -> float:
    return sum(my_list) / len(my_list)

def find_index(my_list: list, element: int) -> int:
    for i in range(len(my_list)):
        if my_list[i] == element:
            return i
    return -1

def is_sorted(my_list: list) -> bool:
    for i in range(1, len(my_list)):
        if my_list[i] < my_list[i-1]:
            return False
    return True

def count_frequency(my_list: list, element: int) -> int:
    count = 0
    for x in my_list:
        if x == element:
            count += 1
    return count

def find_mode(my_list: list) -> int:
    freq = {}
    for x in my_list:
        freq[x] = freq.get(x, 0) + 1
    mode = my_list[0]
    for k in freq:
        if freq[k] > freq[mode]:
            mode = k
    return mode

def remove_all(my_list: list, element: int) -> list:
    return [x for x in my_list if x != element]

def rotate_left(my_list: list, k: int) -> list:
    k = k % len(my_list)
    return my_list[k:] + my_list[:k]

def rotate_right(my_list: list, k: int) -> list:
    k = k % len(my_list)
    return my_list[-k:] + my_list[:-k]

def find_intersection(list1: list, list2: list) -> list:
    return [x for x in list1 if x in list2]

def find_union(list1: list, list2: list) -> list:
    return list(set(list1) | set(list2))

def find_difference(list1: list, list2: list) -> list:
    return [x for x in list1 if x not in list2]