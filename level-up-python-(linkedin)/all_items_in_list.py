
#  This function returns all indices of a specified item in a list or nested lists. 


def all_items_in_list(input_list, item):
    indices = []
    for idx, elm in enumerate(input_list):
        if elm == item:
            indices.append([idx])
        elif isinstance(elm, list):
            nested_idx = all_items_in_list(elm, item)
            if nested_idx:
                for n_idx in nested_idx:
                    indices.append([idx] + n_idx)
    return indices



if __name__ == "__main__":
    sample_list = [1, 2, 3, 4, 5]
    print(all_items_in_list(sample_list, 2))
    print(all_items_in_list(sample_list, 6))

    sample_list_2 = [3, [2, 3], 4, [3, 3, 5]]
    print(all_items_in_list(sample_list_2, 3))

    sample_list_3 = [1, [2, [3, 4]], 4]
    print(all_items_in_list(sample_list_3, 4))