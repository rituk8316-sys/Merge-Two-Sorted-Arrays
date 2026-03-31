# Merge two sorted arrays

def merge_sorted_arrays(arr1, arr2):
    i = j = 0
    merged = []

    # Compare elements and merge
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Add remaining elements
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


# Input
array1 = [1, 3, 5, 7]
array2 = [2, 4, 6, 8]

# Function call
result = merge_sorted_arrays(array1, array2)

# Output
print("Merged array is:", result)
