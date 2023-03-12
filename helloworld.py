import time

# get the start time
st = time.time()
#new one
# main program
#new one
def merge(left, right):
    if not len(left) or not len(right):
        return left or right
#please comment here
    result = []
    i, j = 0, 0
    while (len(result) < len(left) + len(right)):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result

#merge function
def mergesort(list):
    if len(list) < 2:
        return list

    middle = int(len(list) / 2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])

    return merge(left, right)


seq = [12, 11, 13, 5, 6, 7]
time.sleep(0.5)
print("Given array is")
print(seq);
print("\n")
print("Sorted array is")
print(mergesort(seq))

# get the end time
et = time.time()

# get the execution time
elapsed_time = (et - st)
print('Execution time:', elapsed_time, 'seconds')
