def merge_sorted(arr1, arr2):
    """
    Merge two sorted arrays into one sorted array.
    
    :param arr1: First sorted array
    :param arr2: Second sorted array
    :return: Merged sorted array
    """
    merged_array = []
    i, j = 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1
            
    # Append remaining elements
    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])
    
    return merged_array