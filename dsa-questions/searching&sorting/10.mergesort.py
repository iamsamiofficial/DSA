def merge(left,right):
    combined = []
    i = 0
    j = 0
    while i <len(left) and j <len(right):
        if left[i]<right[j]:
            combined.append(left[i])
            i+=1
        else:
            combined.append(right[j])
            j+=1
    while i<len(left):
        combined.append(left[i])
        i+=1
    while j < len(right):
        combined.append(right[j])
        j+=1
    return combined

def mergesort(list1):
    if len(list1) == 1:
        return list1

    middle = int(len(list1)/2)
    left = mergesort(list1[:middle])
    right = mergesort(list1[middle:])

    return merge(left,right)

merger = mergesort([8, 3, 2, 2, 6, 1, 6, 4])
print(merger)


