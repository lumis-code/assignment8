def longest_consecutive(my_list: list[int]) -> int:
    s = set(my_list)
    longest = 0
    for num in s:
        if num - 1 not in s:
            current = num
            length = 1
            while current + 1 in s:
                current += 1
                length += 1
            longest = max(longest, length)
    return longest


def find_missing(my_list: list[int]) -> int:
    n = len(my_list) + 1
    expected = n * (n + 1) // 2
    return expected - sum(my_list)


def find_duplicate(my_list: list[int]) -> int:
    seen = set()
    for num in my_list:
        if num in seen:
            return num
        seen.add(num)


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = {}
    for word in words:
        key = ''.join(sorted(word))
        groups.setdefault(key, []).append(word)
    return list(groups.values())