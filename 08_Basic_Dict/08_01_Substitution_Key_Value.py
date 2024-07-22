def reverse(d):
    new_dict = {}
    for k, v in d.items():
        new_dict[v] = k
    return new_dict


def keys(d, v):
    result = []
    for key, value in d.items():
        if v == value:
            result.append(key) 
    return result

exec(input().strip())