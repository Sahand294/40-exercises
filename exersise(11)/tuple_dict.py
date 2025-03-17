def tuple_dict(input):
    d = {}
    for i in input:
        d[i[0]] = i[1]
    return d
input_list = [("a", 1), ("b", 2), ("c", 3)]
print(tuple_dict(input_list))