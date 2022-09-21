# code your iterative algorithm here


def binary_search(sorted_list, element):
    first = 0
    last = len(sorted_list) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if element == sorted_list[mid]:
            found = True
        else:
            if element < sorted_list[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


test_list = [5, 7, 8, 12, 14, 19, 22, 27, 30, 31, 86]

print(binary_search(test_list, 12))


def binary_search_recursive(sorted_list, element):
    length = len(sorted_list)
    if length == 0:
        return False

    f = 0
    l = length - 1
    mid = (f + l) // 2

    print(sorted_list)
    if element == sorted_list[mid]:
        return True
    else:
        if element < sorted_list[mid]:
            return binary_search_recursive(sorted_list[:(mid)], element)
        else:
            return binary_search_recursive(sorted_list[(mid + 1):], element)


print(binary_search_recursive(test_list, 12))


def binary_search_index_of(element, lst, ref=None):
    length = len(lst)
    if length == 0:
        return -1

    f = 0
    l = length - 1
    mid = (f + l) // 2
    ref = lst if ref is None else ref

    print(lst)
    if element == lst[mid]:
        return ref.index(lst[mid])
    else:
        if element < lst[mid]:
            return binary_search_index_of(element, lst[:(mid)], ref)
        else:
            return binary_search_index_of(element, lst[(mid + 1):], ref)


test_list_again = [5, 7, 8, 12, 14, 19, 22, 27, 30, 31, 86]
print(binary_search_index_of(14, test_list_again))
