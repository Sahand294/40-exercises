def common_elements(list1,list2):
    common_elements = []
    for i in list1:
        if i in list2:
            common_elements.append(i)
    return set(common_elements)
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(common_elements(list1,list2))
