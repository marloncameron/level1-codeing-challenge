def combine_2_list(lst1, lst2):
    return [sub[item] for item in range(len(lst2))
            for sub in [lst1, lst2]]



lst1 = [11,22,33]
lst2 = [1,2,3]
print(combine_2_list(lst1, lst2))

