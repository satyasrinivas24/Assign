def find_largest_element(arr):
    
    largest = arr[0]
    for num in arr:
        
        if num > largest:
            largest = num
    return largest
my_arr = [45,67,53,88,445]
largest_element = find_largest_element(my_arr)
print(largest_element)